#!/usr/bin/env python
#-*- coding=utf8 -*-
__author__ = 'saintic'
__date__ = '2015-10-13'
__doc__ = 'Entry file, all the start.'
__version__ = 'sdp1.1'

import sys,os,re
from Core.sdp_conf import read_conf
from Core.sdp_funs import genpasswd
from subprocess import call
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_CONF = os.path.join(BASE_DIR,'sdp.conf')
APPS = ("mongodb", "mysql", "redis", "memcache", "tair")
WEBS = ("nginx", "tengine", "httpd", "lighttpd", "tomcat", "resin")
PORTS = []

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
DOCKER_PUSH = DOCKER_CONF['Push']
DOCKER_IMG_PRE = DOCKER_CONF['Img_prefix']
DOCKER_REGISTRY = DOCKER_CONF['DockerRegistry']

def main():
  global user_name, user_passwd, user_service, user_email

  if len(sys.argv) == 5:
    user_name = str(sys.argv[1])
    user_passwd = str(genpasswd())
    user_time = int(sys.argv[2])
    user_service = str(sys.argv[3])
    user_email = str(sys.argv[4])
    for i in (user_name, user_passwd, user_service, user_email):
      if not isinstance(i, (str)): raise TypeError('Bad Type, ask string.');sys.exit(3)
    if not isinstance(user_time, (int)) or user_time <= 0: raise TypeError('Bad Type, ask number.');sys.exit(3)
    if re.match(r'([0-9a-zA-Z\_*\.*\-*]+)@([a-zA-Z0-9\-*\_*\.*]+)\.([a-zA-Z]+$)', user_email) == None: print "Mail format error.";sys.exit(3)
  else:
    print "\033[0;31;40mUsage:user time service email\033[0m"
    sys.exit(1)

  if user_service in WEBS:
    call(['python ' + os.path.join(BASE_DIR, 'Web.py')], shell=True)
  elif user_service in APPS:
    call(['python ' + os.path.join(BASE_DIR, 'App.py')], shell=True)
  else:
    print "Unsupported service type."
    sys.exit(2)

if __name__ == "__main__":
  main()
