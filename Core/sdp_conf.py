#!/usr/bin/env python
#-*- coding=utf8 -*-
__author__ = 'saintic'
__date__ = '2015-10-13'
__doc__ = 'read config, refuse write'
__version__ = 'sdp1.1'


import os
from configobj import ConfigObj
Root=os.getcwd()
def read_conf():
  config_file=Root+'/../sdp.conf'
  print config_file

read_conf()
