# PyYAML problems

## `package directory 'lib3/yaml' does not exist`
Solution: install PyYAML separately with `pip install pyyaml`.

## (Windows) `[WinError 2] The system cannot find the file specified`
Solution:
1. Download the wheel (e.g. `PyYAML-3.11-cp27-cp27m-win_amd64.whl` - choose the right one by inspecting the Python and platform version) from the [Unofficial Windows Binaries for Python Extension Packages](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyyaml)
1. Install the wheel, e.g. `pip install PyYAML-3.11-cp27-cp27m-win_amd64.whl`

# `ImportError: numpy.core.multiarray failed to import`
Solution: install numpy separately with `pip install --upgrade numpy`.

# Installing OpenCV3 on Mac OS X
1. Install [Homebrew](http://brew.sh/)
1. Install OpenCV3 by running:
   1. `brew tap homebrew/science`
   1. `brew install opencv3 --with-contrib --with-tbb --with-python3 --with-ffmpeg`

# Installing and using OpenCV3 on Windows
1. Download the [binary installer](http://opencv.org/downloads.html)
1. Extract it to e.g. `C:\OpenCV\OpenCV310`.
1. Add the following directories to the system `PATH`:
   * `C:\OpenCV\OpenCV310\build\python\2.7\x64`
   * `C:\OpenCV\OpenCV310\build\bin`
1. Add `C:\OpenCV\OpenCV310\build\python\2.7\x64` to `PYTHONPATH` (create `PYTHONPATH` if it does not exist).
