#!/usr/bin/env python

from distutils.core import setup

setup(name='Vimooglemenu',
      version='0.1',
      description='Vimeo-Google inspired top menu for django',
      author='Alan Domissy',
      author_email='vimooglemenu@geomarcomputers.com',
      url='http://geomarcomputers.github.com/Vimoogle-Menu',
      packages=['vimooglemenu', 'vimooglemenu.homepage'],
      scripts=['vimooglemenu/manage.py']
     )