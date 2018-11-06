from setuptools import setup

setup(
    name='roman',
    entry_points={
        'console_scripts': {
            'int_to_roman = src.cli.roman:int_to_roman',
            'roman_to_int = src.cli.roman:roman_to_int'
        }
    },
    install_requires=['flask>=1.0'])
