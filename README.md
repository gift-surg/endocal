endocal
-------

endocal is a cross-platform, compact GUI application for the optical distortion calibration of fluid-immersed endoscopes. It uses the [OpenCV][opencv] camera calibration module.

endocal was developed by Dzhoshkun I. Shakir as part of the [GIFT-Surg project][giftsurg] at the [Translational Imaging Group][tig] in the [Centre for Medical Image Computing][cmic] at [University College London (UCL)][ucl].

License
-------

Copyright (c) 2016, [University College London][ucl]. endocal is available as free open-source software under a BSD 3-Clause Licence.

Features
--------

* Lightweight, compact GUI application for optical distortion calibration of endoscopes
* Command-line application for generating [ASCII DXF files](http://www.autodesk.com/techpubs/autocad/acadr14/dxf/) for use in calibration target fabrication (translated from Matlab scripts developed by Daniil I. Nikitichev)

System requirements
-------------------

* [OpenCV][opencv]
* [pip](https://pip.pypa.io/en/stable/installing/)
* (Online calibration) Video source supported by [OpenCV][opencv_docs] (see esp. the OpenCV tutorials related to video IO)

How to install / remove
-----------------------

**Note:** Please check out [these hints](doc/issues.md) if you encounter any issues with endocal.

To install: `pip install endocal`.

To test your installation type: `endocal-test`:

* See [this screenshot](endocal/res/screenshot-start.png) for what to expect on launching the application.
* To perform an optical distortion calibration, follow the instructions shown in red on top of the window. While acquiring calibration data, detected calibration pattern blobs will be emphasized with a virtual overlay as in [this screenshot](endocal/res/screenshot-detection.png).
* All data for each calibration will be saved in the sub-folder of a folder called `tmp-sample_001`, created within the current folder. These include:
  * Calibration parameters saved as `calibration.yml`
  * Frames used for calibration saved as indexed image files, e.g. `frame_009.jpg`
* After performing a calibration, the application will automatically show the undistorted images to the right as shown in [this screenshot](endocal/res/screenshot-undistort.png).

To remove: `pip uninstall endocal`.

How to use
----------

**Calibration:** `endocal --help` shows details of what input parameters are expected. Examples include:
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

**ASCII DXF file generation:** For instance to generate an asymmetric grid of circles each with a diameter of `1 mm` to be etched by a laser cutter with a beam width of `45 μm` (microns):
```
dxf --laser-beam-width 45 --diameter 1 --output-file output.dxf
```
Here the grid is saved to file `output.dxf` and the corresponding (ellipse) legend to `output-legend.dxf` (legend filename always inferred from main DXF filename).

Supported platforms
-------------------

endocal was tested so far on:

* Linux: Ubuntu 14.04.3 LTS 64-bit, elementary OS Freya 0.3.2 64-bit
* Mac OS X: El Capitan 10.11.3
* Windows: 10 Professional 64-bit

It is highly likely that it will work on other platforms as well, due to the small number of dependencies.

Funding
-------

This work was supported through an Innovative Engineering for Health award by the [Wellcome Trust][wellcometrust] [WT101957], the [Engineering and Physical Sciences Research Council (EPSRC)][epsrc] [NS/A000027/1] and a [National Institute for Health Research][nihr] Biomedical Research Centre [UCLH][uclh]/UCL High Impact Initiative.


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
