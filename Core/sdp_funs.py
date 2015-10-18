#!/usr/bin/env python
#coding:utf8

def genpasswd(L=15):
  if not isinstance(L, (int)):
    raise TypeError('Bad operand type, ask Digital.')
  from random import Random
  stri = ''
  chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
  length = len(chars) - 1
  random = Random()
  for i in range(L):
    stri+=chars[random.randint(0, length)]
  return stri


