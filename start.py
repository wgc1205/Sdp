#!/usr/bin/env python
#-*- coding=utf8 -*-
__author__ = 'saintic'
__date__ = '2015-10-13'
__doc__ = 'Entry file, all the start.'
__version__ = 'sdp1.1'

import sys,os,configobj
from Core.sdp_conf import read_conf
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
BASE_CONF=os.path.join(BASE_DIR,'sdp.conf')
GLOBAL_CONF=read_conf(BASE_CONF, 'globals')
REDIS_CONF=read_conf(BASE_CONF, 'redis')
DOCKER_CONF=read_conf(BASE_CONF, 'docker')
print GLOBAL_CONF,REDIS_CONF,DOCKER_CONF



