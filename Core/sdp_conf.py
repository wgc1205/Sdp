#!/usr/bin/env python
#-*- coding=utf8 -*-
__author__ = 'saintic'
__date__ = '2015-10-13'
__doc__ = 'read config, refuse write'
__version__ = 'sdp1.1'

def read_conf(items):
  '''Read configuration information.'''
  import os,configobj
  iniconf=configobj.ConfigObj(os.path.join(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0], 'sdp.conf'))
  try:
    return iniconf[items]
  except:
    print 'Get configuration information failure.'
    return 1

if __name__ == '__main__':
  read_conf('globals')

