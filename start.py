#!/usr/bin/env python
#-*- coding=utf8 -*-
__author__ = 'saintic'
__date__ = '2015-10-13'
__doc__ = 'Entry file, all the start.'
__version__ = 'sdp1.1'

import sys,os
from Core.sdp_conf import read_conf
from Core.sdp_func import genpasswd
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_CONF = os.path.join(BASE_DIR,'sdp.conf')
APPS = ("mongodb", "mysql", "redis", "memcache")
WEBS = ("nginx", "tengine", "httpd", "lighttpd", "tomcat", "resin")

#get variables from sdp.conf, format is dict.
GLOBAL_CONF = read_conf(BASE_CONF, 'globals')
REDIS_CONF = read_conf(BASE_CONF, 'redis')
DOCKER_CONF = read_conf(BASE_CONF, 'docker')

#set global variables
LANG = GLOBAL_CONF['LANG']
SDP_HOME = GLOBAL_CONF['SDP_HOME']
SDP_DATA_HOME = GLOBAL_CONF['SDP_DATA_HOME']
SDP_USER_DATA_HOME = os.path.join(SDP_DATA_HOME, str(GLOBAL_CONF['SDP_USER_DATA_HOME']))
SDP_LOGS_DATA_HOME = os.path.join(SDP_DATA_HOME, str(GLOBAL_CONF['SDP_LOGS_DATA_HOME']))
SDP_UC = os.path.join(SDP_DATA_HOME, str(GLOBAL_CONF['SDP_UC']))

#set redis variables
REDIS_HOST = REDIS_CONF['host']
REDIS_PORT = REDIS_CONF['port']
REDIS_DB = REDIS_CONF['db']
REDIS_PASSWORD = REDIS_CONF['password']

#set docker variables
DOCKER_IMG_PRE = DOCKER_CONF['image_prefix']
DOCKER_REGISTRY = DOCKER_CONF['DockerRegistry']

#get parameters
user_name = sys.argv[1]
user_passwd = genpasswd()
user_service = sys.argv[2]
user_email = sys.argv[3]
user_code = ''
userinfo=(user_name, user_passwd, user_service, user_email)

def main(*U):
  if not isinstance(U, (tuple))
    raise TypeError('Bad operand type, ask a tuple.')


if __name__ == "__main__":
  if len(sys.argv) != 4:
    print "Usage:user service email"

