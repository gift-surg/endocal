# endocal

endocal is a cross-platform, compact GUI application for the optical distortion calibration of fluid-immersed
endoscopes. It uses the [OpenCV][opencv] camera calibration module.

endocal was developed by Dzhoshkun I. Shakir as part of the [GIFT-Surg project][giftsurg] at the
[Translational Imaging Group][tig] in the [Centre for Medical Image Computing][cmic] at
[University College London (UCL)][ucl].

## Features

* Lightweight, compact GUI application for optical distortion calibration of endoscopes
* Command-line application for generating [ASCII DXF files](http://www.autodesk.com/techpubs/autocad/acadr14/dxf/)
for use in calibration target fabrication (translated from Matlab scripts developed by Daniil I. Nikitichev)

The detailed changelog is available on [GitHub][changelog].

[changelog]: CHANGELOG.md

## System requirements

* [Python][python]
* [pip][pip]
* [OpenCV][opencv] (installed with [Python][python] support)
* For live calibration: a video source supported by [OpenCV][opencv_docs] (see esp. the OpenCV tutorials related
to video IO)
* [PyYAML][pyyaml]
* [NumPy][numpy]
* So far endocal has been tested on the following operating systems:

  - Ubuntu 16.04.3 LTS 64-bit
  - Ubuntu 14.04.3 LTS 64-bit
  - elementary OS Freya 0.3.2 64-bit
  - macOS Sierra 10.12.6
  - OS X El Capitan 10.11.3
  - Windows 10 Professional 64-bit

## Installation

#### Installing endocal

`pip install endocal`

#### Testing your installation

* Launch the test application by running `endocal-test`.
* [This screenshot](endocal/res/screenshot-start.png) shows you what to expect on launching the application.
* To perform an optical distortion calibration, follow the instructions shown in red on top of the application window.
* While acquiring calibration data, detected calibration pattern blobs will be emphasized with a virtual overlay as
in [this acquisition-mode screenshot](endocal/res/screenshot-detection.png).
* All data for each calibration will be saved in a human-readably time-stamped, uniquely-named folder within a root 
folder named `tmp-sample_002` created within the folder where the application was launched.
For instance `tmp-sample_002/2018-02-08-11-03-19-AHDHO` for a calibration run on 8 February 2018 at 11:03 am.
The saved data includes:
  * A [YAML][yaml] file named `calibration.yml` with the computed calibration parameters
  * Frames used for calibration saved as indexed image files, e.g. `frame_009.jpg`
* After performing a calibration, the application will automatically show the undistorted images in real time to the right of the application window as in [this undistortion-mode screenshot](endocal/res/screenshot-undistort.png).

#### Uninstalling endocal

`pip uninstall endocal`

## Usage

#### Calibration

`endocal --help` shows details of what input parameters are expected. Some examples are provided below:

* Offline calibration by using all frames saved as indexed image files in a `/data/offline` folder:

```sh
endocal --pattern-specs 3 11 3 1 --output-folder ./calibration-results --input /data/offline/frame_%03d.jpg
```

* Live calibration using a real-time video stream from an endoscope provided by a frame-grabber (assuming the 
frame-grabber is [mounted as `/dev/video0` on Linux][ubuntu-webcam]):

```sh
endocal --input 0 --pattern-specs 3 11 3 1 --output-folder ./calibration-results
```

* Using a `700 x 700` sub-frame of the whole endoscopic video frame (whose full size is e.g. `1920 x 1080`):

```sh
endocal --input 0 --pattern-specs 3 11 3 1 --output-folder ./calibration-results --roi 620 200 700 700
```

#### ASCII DXF file generation

`dxf --help` shows details of what input parameters are expected.

For instance to generate an asymmetric grid of circles each with a diameter of `1 mm` to be etched by a laser
cutter with a beam width of `45 μm` (microns):

```sh
dxf --laser-beam-width 45 --diameter 1 --output-file output.dxf
```

Here the grid is saved to file `output.dxf` and the corresponding (ellipse) legend to `output-legend.dxf` (legend
filename always inferred from main DXF filename).

#### Troubleshooting

Please check out [these hints](doc/issues.md) in case you encounter any issues with endocal.

## Licensing and copyright

Copyright (c) 2016, [University College London][ucl]. endocal is available as free open-source software under a
BSD 3-Clause Licence.

## Acknowledgements

This work was supported through an Innovative Engineering for Health award by the [Wellcome Trust][wellcometrust]
[WT101957], the [Engineering and Physical Sciences Research Council (EPSRC)][epsrc] [NS/A000027/1] and a
[National Institute for Health Research][nihr] Biomedical Research Centre [UCLH][uclh]/UCL High Impact Initiative.


[tig]: http://cmictig.cs.ucl.ac.uk
[giftsurg]: http://www.gift-surg.ac.uk
[cmic]: http://cmic.cs.ucl.ac.uk
[ucl]: http://www.ucl.ac.uk
[nihr]: http://www.nihr.ac.uk/research
[uclh]: http://www.uclh.nhs.uk
[epsrc]: http://www.epsrc.ac.uk
[wellcometrust]: http://www.wellcome.ac.uk
[opencv]: http://opencv.org/
[opencv_docs]: http://docs.opencv.org/
[python]: https://www.python.org/
[pip]: https://pip.pypa.io/en/stable/installing/
[yaml]: http://yaml.org/
[pyyaml]: https://github.com/yaml/pyyaml
[numpy]: http://www.numpy.org/
[ubuntu-webcam]: https://help.ubuntu.com/community/Webcam
