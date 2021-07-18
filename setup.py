from setuptools import setup

APP = ['temps.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'thermometer.icns',
    'plist': {
        'CFBundleShortVersionString': '0.2.0',
        'LSUIElement': True,
    },
    'packages': ['rumps', 'subprocess'],
}

setup(
    app=APP,
    name='CPU-Temperatur',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'], install_requires=['rumps']
)