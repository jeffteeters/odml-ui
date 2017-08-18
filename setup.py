#!/usr/bin/env python

import os
import glob


# Use setuptools compulsarily, as the distutils doen't work out well for the 
# installation procedure. The 'install_requires' and 'data_files' have better
# support in setuptools.
from setuptools import setup

try:
    # only necessary for the windows build
    import py2exe
    kwargs.update({'console': ['odml-gui']})
except ImportError:
    py2exe = None

packages = [
    'odmlui',
    'odmlui.dnd',
    'odmlui.treemodel'
]

install_req = ["odml==1.3.*"]

data_files = [('share/pixmaps', glob.glob(os.path.join("images", "*"))),
              ('/usr/share/applications', ['odml.desktop'])
              ]

setup(name='odML-UI',
      version='1.3',
      description='odML Editor',
      author='Hagen Fritsch',
      author_email='fritsch+gnode@in.tum.de',
      url='http://www.g-node.org/projects/odml',
      packages=packages,
      options={
          'py2exe': {
              'packages': 'odml',
              'includes': 'cairo, pango, pangocairo, atk, gobject, gio, lxml, gzip, enum34',
          }
      },
      install_requires=install_req,
      scripts=['odml-gui'],
      data_files=data_files
      )
