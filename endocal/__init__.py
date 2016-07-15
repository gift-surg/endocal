#!/usr/bin/env python

from argparse import ArgumentParser
from cv2 import VideoCapture, imshow, waitKey, putText, FONT_HERSHEY_PLAIN,\
    drawChessboardCorners
from numpy import zeros, uint8
import calibration

KEY_QUIT = 27
KEY_TOGGLE_ACQUISITION = ord(calibration.State.KEYS[calibration.State.ACQUIRING])
KEY_ABORT_ACQUISITION = ord(calibration.State.KEYS[calibration.State.CORRECTING])


def __frame_size(video_source_desc):
    cap = VideoCapture(video_source_desc)
    ret, tmp_image = cap.read()
    cap.release()
    if not ret:
        raise RuntimeError('Could not read ' + str(video_source_desc))
    return [0, 0, tmp_image.shape[1], tmp_image.shape[0]]


def main():
    # parse arguments
    parser = ArgumentParser()
    parser.add_argument('--input', type=str,
                        help='Video file, video folder or device id (e.g. 1 for /dev/video1)',
                        required=True)
    parser.add_argument('--calibration-file', type=str,
                        help='YAML file with calibration parameters',
                        required=False)
    parser.add_argument('--output-folder', type=str,
                        help='Where to log results',
                        required=True)
    parser.add_argument('--roi', nargs=4, type=int,
                        help='Sub-frame specs: <x> <y> <width> <height>',
                        required=False)
    parser.add_argument('--pattern-specs', nargs=4, type=float,
                        help='Calibration pattern dimensions: <rows> <cols> '
                             '<row_spacing> <col_spacing> (rows a.k.a. width, '
                             'cols a.k.a. height)',
                        required=True)
    args = parser.parse_args()

    # do work
    try:
        video_source_desc = int(args.input)
    except ValueError:
        video_source_desc = args.input

    roi = __frame_size(video_source_desc)

    pattern_specs = tuple(args.pattern_specs)
    calibrator = calibration.Calibrator(pattern_specs=pattern_specs,
                                        file_path=args.calibration_file,
                                        # i.e. None handled internally:
                                        roi=args.roi,
                                        full=roi)
    if args.roi:
        roi = args.roi
    state = calibration.State(calibrator)
    source = VideoCapture(video_source_desc)
    file_io = calibration.FileIO(args.output_folder)

    if not source.isOpened():
        raise RuntimeError('Could not open ' + args.input)

    frame = zeros((roi[3], 2 * roi[2], 3), dtype=uint8)
    while True:
        ret, image = source.read()
        if not ret:
            source = VideoCapture(video_source_desc)
            continue
        image = image[roi[1]:roi[1]+roi[3],
                      roi[0]:roi[0]+roi[2]]
        frame[0:roi[3], roi[2]:2*roi[2]] = zeros(image.shape)
        if state.is_correcting():
            ret, corrected_image = calibrator.correct(image)
            if ret:
                frame[0:roi[3], roi[2]:2*roi[2]] = corrected_image
        elif state.is_acquiring():
            ret, blobs = calibrator.append(image, file_io.next_image())
            if ret:
                drawChessboardCorners(image, calibrator.pattern_dims, blobs, ret)
        elif state.is_calibrating():
            if calibrator.done():
                state.correcting()

        frame[0:roi[3], 0:roi[2]] = image
        putText(frame, state.what(), (30, 30), FONT_HERSHEY_PLAIN, 2, (0, 0, 255))
        imshow('Optical distortion calibration', frame)

        # user input
        key = waitKey(50)
        if (0xFF & key == KEY_QUIT) or image.size == 0:
            break
        elif 0xFF & key == KEY_TOGGLE_ACQUISITION:
            if state.is_correcting():
                file_io.new_session()
                source.release()
                source = VideoCapture(video_source_desc)
                calibrator.reset()
                state.acquiring()
            elif state.is_acquiring():
                if calibrator.can():
                    calibrator.start(file_io.calibration())
                    state.calibrating()
                else:
                    calibrator.reset()
                    state.correcting()
        elif 0xFF & key == KEY_ABORT_ACQUISITION:
            if state.is_acquiring():
                calibrator.reset()
                state.correcting()

    source.release()
