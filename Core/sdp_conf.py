#!/usr/bin/env python
#-*- coding=utf8 -*-
__author__ = 'saintic'
__date__ = '2015-10-13'
__doc__ = 'read config, refuse write'
__version__ = 'sdp1.1'

def read_conf(f,i):
  if not isinstance(f, (str)):
        raise TypeError('Bad operand type, ask a file.')
  if not isinstance(i, (str)):
        raise TypeError('bad operand type, ask string.')
  from configobj import ConfigObj
  try:
    return ConfigObj(f)[i]
  except:
    print 'Get configuration information failure.'
    return 1

