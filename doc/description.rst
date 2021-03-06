endocal is a cross-platform, compact GUI application for the optical distortion calibration of fluid-immersed
endoscopes. It uses the `OpenCV`_ camera calibration module.

endocal was developed by Dzhoshkun I. Shakir as part of the `GIFT-Surg project`_ at the
`Translational Imaging Group`_ in the `Centre for Medical Image Computing`_ at
`University College London (UCL)`_.

.. _`GIFT-Surg project`: http://www.gift-surg.ac.uk
.. _`Translational Imaging Group`: http://cmictig.cs.ucl.ac.uk
.. _`Centre for Medical Image Computing`: http://cmic.cs.ucl.ac.uk
.. _`University College London (UCL)`: http://www.ucl.ac.uk

Features
--------

* Lightweight, compact GUI application for optical distortion calibration of endoscopes
* Command-line application for generating `ASCII DXF files`_ for use in calibration target fabrication (translated\
  from Matlab scripts developed by Daniil I. Nikitichev)

The detailed changelog is available on `GitHub`_.

.. _`ASCII DXF files`: http://www.autodesk.com/techpubs/autocad/acadr14/dxf/
.. _`GitHub`: https://github.com/gift-surg/endocal/blob/master/CHANGELOG.md

System requirements
-------------------

* `Python`_
* `pip`_
* `OpenCV`_ (installed with `Python`_ support)
* For live calibration: a video source `supported by OpenCV`_ (see esp. the OpenCV tutorials related
  to video IO)
* `PyYAML`_
* `NumPy`_
* So far endocal has been tested on the following operating systems:

  - Ubuntu 16.04.3 LTS 64-bit
  - Ubuntu 14.04.3 LTS 64-bit
  - elementary OS Freya 0.3.2 64-bit
  - macOS Sierra 10.12.6
  - OS X El Capitan 10.11.3
  - Windows 10 Professional 64-bit

.. _`Python`: https://www.python.org/
.. _`pip`: https://pip.pypa.io/en/stable/installing/
.. _`supported by OpenCV`: http://docs.opencv.org/
.. _`PyYAML`: https://github.com/yaml/pyyaml
.. _`NumPy`: http://www.numpy.org/
.. _`OpenCV`: http://opencv.org/

Installation
------------

Installing endocal
^^^^^^^^^^^^^^^^^^

``pip install endocal``

Testing your installation
^^^^^^^^^^^^^^^^^^^^^^^^^

* Launch the test application by running ``endocal-test``.
* `This screenshot`_ shows you what to expect on launching the application.
* To perform an optical distortion calibration, follow the instructions shown in red on top of the application window.
* While acquiring calibration data, detected calibration pattern blobs will be emphasized with a virtual overlay as
  in `this acquisition-mode screenshot`_.
* All data for each calibration will be saved in a human-readably time-stamped, uniquely-named folder within a root 
  folder named ``tmp-sample_002`` created within the folder where the application was launched.
  For instance ``tmp-sample_002/2018-02-08-11-03-19-AHDHO`` for a calibration run on 8 February 2018 at 11:03 am.
  The saved data includes:

  * A `YAML`_ file named ``calibration.yml`` with the computed calibration parameters
  * Frames used for calibration saved as indexed image files, e.g. ``frame_009.jpg``

* After performing a calibration, the application will automatically show the undistorted images in real time to the
  right of the application window as in `this undistortion-mode screenshot`_.

.. _`This screenshot`: https://github.com/gift-surg/endocal/blob/master/endocal/res/screenshot-start.png
.. _`this acquisition-mode screenshot`: https://github.com/gift-surg/endocal/blob/master/endocal/res/screenshot-detection.png
.. _`YAML`: http://yaml.org/
.. _`this undistortion-mode screenshot`: https://github.com/gift-surg/endocal/blob/master/endocal/res/screenshot-undistort.png

Uninstalling endocal
^^^^^^^^^^^^^^^^^^^^

``pip uninstall endocal``

Usage
-----

Calibration
^^^^^^^^^^^

``endocal --help`` shows details of what input parameters are expected. Some examples are provided below:

* Offline calibration by using all frames saved as indexed image files in a ``/data/offline`` folder:

.. code-block:: sh

  endocal --pattern-specs 3 11 3 1 --output-folder ./calibration-results --input /data/offline/frame_%03d.jpg

* Live calibration using a real-time video stream from an endoscope provided by a frame-grabber (assuming the 
  frame-grabber is `mounted`_ as ``/dev/video0``):

.. code-block:: sh

  endocal --input 0 --pattern-specs 3 11 3 1 --output-folder ./calibration-results

.. _`mounted`: https://help.ubuntu.com/community/Webcam

* Using a ``700 x 700`` sub-frame of the whole endoscopic video frame (whose full size is e.g. ``1920 x 1080``):

.. code-block:: sh

  endocal --input 0 --pattern-specs 3 11 3 1 --output-folder ./calibration-results --roi 620 200 700 700

ASCII DXF file generation
^^^^^^^^^^^^^^^^^^^^^^^^^

``dxf --help`` shows details of what input parameters are expected.

For instance to generate an asymmetric grid of circles each with a diameter of ``1 mm`` to be etched by a laser
cutter with a beam width of ``45 μm`` (microns):

.. code-block:: sh

  dxf --laser-beam-width 45 --diameter 1 --output-file output.dxf

Here the grid is saved to file ``output.dxf`` and the corresponding (ellipse) legend to ``output-legend.dxf`` (legend
filename always inferred from main DXF filename).

Troubleshooting
^^^^^^^^^^^^^^^

Please check out `these hints`_ in case you encounter any issues with endocal.

.. _`these hints`: https://github.com/gift-surg/endocal/blob/master/doc/issues.md

Licensing and copyright
-----------------------

Copyright (c) 2016, `University College London`_. endocal is available as free open-source software under a
BSD 3-Clause Licence.

.. _`University College London`: http://www.ucl.ac.uk

Acknowledgements
----------------

This work was supported through an Innovative Engineering for Health award by the `Wellcome Trust`_
[WT101957], the `Engineering and Physical Sciences Research Council (EPSRC)`_ [NS/A000027/1] and a
`National Institute for Health Research`_ Biomedical Research Centre `UCLH`_/UCL High Impact Initiative.


.. _`National Institute for Health Research`: http://www.nihr.ac.uk
.. _`UCLH`: http://www.uclh.nhs.uk
.. _`Engineering and Physical Sciences Research Council (EPSRC)`: http://www.epsrc.ac.uk
.. _`Wellcome Trust`: http://www.wellcome.ac.uk
