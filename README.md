# endocal

endocal is a compact GUI application for optical distortion calibration of endoscopes. It uses the [OpenCV camera calibration module](http://docs.opencv.org/2.4/doc/tutorials/calib3d/camera_calibration/camera_calibration.html) under the hood.

endocal was developed by Dzhoshkun I. Shakir as part of the [GIFT-Surg project](http://www.gift-surg.ac.uk/) at the [Translational Imaging Group](http://cmictig.cs.ucl.ac.uk/) in the [Centre for Medical Image Computing](http://www.ucl.ac.uk/cmic/homepage) at [University College London (UCL)](http://www.ucl.ac.uk/).

# License
Copyright (c) 2016, [University College London](http://www.ucl.ac.uk/). endocal is available as free open-source software under a BSD 3-Clause Licence.

# Features

* Lightweight, compact GUI application for optical distortion calibration of endoscopes
* Command-line application for generating [ASCII DXF files](http://www.autodesk.com/techpubs/autocad/acadr14/dxf/) for use in calibration target fabrication (translated from Matlab scripts developed by Daniil I. Nikitichev)

# System requirements
* [OpenCV 2.4](http://docs.opencv.org/2.4/doc/tutorials/introduction/table_of_content_introduction/table_of_content_introduction.html)
* [pip](https://pip.pypa.io/en/stable/installing/)
* For online calibration, frame-grabber hardware supported by [OpenCV](http://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture)

# Installation
1. Install endocal by running `pip install endocal`.
1. Test your installation by running `endocal-test`:
   * See [this screenshot](endocal/res/screenshot-start.png) for what to expect on launching the application.
   * To perform an optical distortion calibration, follow the instructions shown in red on top of the window. While acquiring calibration data, detected calibration pattern blobs will be emphasized with a virtual overlay as in [this screenshot](endocal/res/screenshot-detection.png).
   * All data for each calibration will be saved in the sub-folder of a folder called `tmp-sample_001`, created within the current folder. These include:
      * Calibration parameters saved as `calibration.yml`
      * Frames used for calibration saved as indexed image files, e.g. `frame_009.jpg`
   * After performing a calibration, the application will automatically show the undistorted images to the right as shown in [this screenshot](endocal/res/screenshot-undistort.png).

# Removing
`pip uninstall endocal`

# How to use

## Calibration

`endocal --help` shows details of what input parameters are expected. Examples include:

* Using all frames stored as indexed files e.g. `frame_009.jpg`:
```
endocal --pattern-specs 3 11 3 1 --output-folder ./calibration-results --input /data/offline/frame_%03d.jpg
```

* Using online video stream from a frame-grabber (attached to an endoscope) that is mounted as `/dev/video0` on Linux:
```
endocal --input 0 --pattern-specs 3 11 3 1 --output-folder ./calibration-results
```

* Using a `700 x 700` sub-frame of the whole endoscopic video frame (`1920 x 1080`):
```
endocal --input 0 --pattern-specs 3 11 3 1 --output-folder ./calibration-results --roi 620 200 700 700
```

## ASCII DXF file generation

For instance to generate an asymmetric grid of circles each with a diameter of `1 mm` to be etched by a laser cutter with a beam width of `45 μm` (microns):
```
dxf --laser-beam-width 45 --diameter 1 --output-file output.dxf
```
Here the grid is saved to file `output.dxf` and the corresponding (ellipse) legend to `output-legend.dxf` (legend filename always inferred from main DXF filename).

# Supported platforms
endocal was tested only on Linux (Ubuntu 14.04 LTS) so far. However it is highly likely that it will work on other platforms as well, due to the small number of dependencies.
