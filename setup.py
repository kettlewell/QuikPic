#!/usr/bin/env python

from setuptools import setup

setup(name='QuikPic',
      version='0.1',
      description='Safely de-duplicate and sort files',
      author='Matthew Kettlewell',
      author_email='matt@kettlewell.net',
      packages=['QuikPic'],
      entry_points={
        'console_scripts': [
            'quikpick= quickpic.sort:main'
        ]
      },
      install_requires=['exifread'],
      url='https://github.com/kettlewell/QuikPic',
      license='MIT,
      keywords='photography photo sort',
)

