# MacOS Menu Bar CPU Temperature Display
Very basic CPU temperature display in macOS menu bar using [RUMPS](https://github.com/jaredks/rumps) and [osx-cpu-temp](https://github.com/lavoiesl/osx-cpu-temp). Expand to your tastes.

![Screenshot of final menu bar item](https://github.com/niklaskoopmann/macos-temperature-rumps/blob/main/screenshot.png?raw=true)

## How to build
```
pip install rumps py2app setuptools

python3 setup.py py2app --resources osx-cpu-temp
```
