# MacOS Menu Bar CPU Temperature Display
using [RUMPS](https://github.com/jaredks/rumps) and [osx-cpu-temp](https://github.com/lavoiesl/osx-cpu-temp)

## How to build
```
pip install rumps py2app setuptools

python3 setup.py py2app --resources osx-cpu-temp
```