import os
import sys
from pathlib import Path

from setuptools import find_packages, setup

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()

setup(
    name='sweet',
    version="0.0.1",
    author='abzicht',
    author_email='abzicht@gmail.com',
    description=('Split threads to single tweets'),
    long_description=read('readme.md'),
    license='mit',
    include_package_data=False,
    packages=find_packages(),
    entry_points={'console_scripts': [
        'sweet=sweet.script:main',
    ]},
    install_requires=['argparse'],
)
