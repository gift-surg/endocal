# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog][keep-a-changelog]
and this project adheres to [PEP440 date-based versioning][pep440-date].

[keep-a-changelog]: http://keepachangelog.com/en/1.0.0/
[pep440-date]: https://www.python.org/dev/peps/pep-0440/#support-for-date-based-version-identifiers

## [Unreleased]

## [18.02.13]
### Added
* Support for specifying the maximum nr. of frames to use for calibration
* A new sample calibration dataset
* Support for saving per-view and average re-projection errors

### Fixed
* Swapped image dimensions when feeding frames into camera calibration
* Wrong indexing of saved calibration frames
* Saving of frames not used for calibration

## [16.08.08]
### Added
* Support for Python 3
* Support for OpenCV 3
* Troubleshooting hints
* Graceful handling of unavailable OpenCV

## 16.07.22
### Added
* Optical distortion calibration using OpenCV 2 and Python 2
* Graphical interface for data acquisition and camera calibration
* Generation of ASCII DXF files for calibration target fabrication

[Unreleased]: https://github.com/gift-surg/endocal/compare/v18.02.13...HEAD
[18.02.13]: https://github.com/gift-surg/endocal/compare/v16.08.08...v18.02.13
[16.08.08]: https://github.com/gift-surg/endocal/compare/v16.07.22...v16.08.08

