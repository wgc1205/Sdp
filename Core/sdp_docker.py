#!/usr/bin/env python
#-*- coding=utf8 -*-
__author__ = 'saintic'
__date__ = '2015-10-19'
__version__ = 'sdp1.1'
__doc__ = 'docker functions, for images, for containers'

try:
  import docker
except ImportError as errmsg:
  print __file__, 'import docker module failed, because %s' % errmsg

class Sdocker():
  '''Operation docker, json format'''
  def __init__(self, **kw):
    pass

  def docker_create(self, image):
    cid = docker.Client(base_url='unix://var/run/docker.sock',version='auto',timeout=30)
    cid.create_container(image="yorko/webserver:v1",stdin_open=True,tty=True,command="",volumes=['/data'],ports=[80,22],name="webserver11")

