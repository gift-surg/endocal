Here we highlight the issues encountered during installation / use of endocal, together with possible solutions. If you experience other issues, please report those by opening a new issue on the issue tracker.

### PyYAML problems

#### package directory 'lib3/yaml' does not exist
Solution: install PyYAML separately with `pip install pyyaml`.

#### (On Windows) The system cannot find the file specified
The error log would look like this:

```
[...]
copying lib3\yaml\serializer.py -> build\lib.win-amd64-3.5\yaml
copying lib3\yaml\tokens.py -> build\lib.win-amd64-3.5\yaml
copying lib3\yaml\__init__.py -> build\lib.win-amd64-3.5\yaml
running build_ext
creating build\temp.win-amd64-3.5
creating build\temp.win-amd64-3.5\Release
checking if libyaml is compilable
error: [WinError 2] The system cannot find the file specified
```

Solution:

1. Download the wheel (e.g. `PyYAML-3.11-cp27-cp27m-win_amd64.whl` - choose the right one by inspecting the Python and platform version encoded in the file name) from the [Unofficial Windows Binaries for Python Extension Packages](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyyaml).
1. Install the downloaded wheel, e.g. `pip install PyYAML-3.11-cp27-cp27m-win_amd64.whl`.

### ImportError: numpy.core.multiarray failed to import
Solution: install numpy separately with `pip install --upgrade numpy`.

### Installing OpenCV3 on Mac OS X
1. Install [Homebrew](http://brew.sh/)
1. Install OpenCV3 by running the following commands:
  1. `brew tap homebrew/science`
  1. `brew install opencv3 --with-contrib --with-tbb --with-python3 --with-ffmpeg`

### Installing and using OpenCV3 on Windows
1. Download the binary installer from http://opencv.org/downloads.html.
1. Extract it to e.g. `C:\OpenCV\OpenCV310`.
1. Add the following directories to the system `PATH`:
   * `C:\OpenCV\OpenCV310\build\python\2.7\x64`
   * `C:\OpenCV\OpenCV310\build\bin`
1. Add `C:\OpenCV\OpenCV310\build\python\2.7\x64` to `PYTHONPATH` (create `PYTHONPATH` if it does not exist).
