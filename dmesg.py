#!/usr/bin/python

import subprocess
import sys
import os
import time

def run_command(command):
  """given shell command, returns stdout and stderr"""
  p = subprocess.Popen(command,
		       stdout=subprocess.PIPE,
		       stderr=subprocess.STDOUT)
  return iter(p.stdout.readline, b'')

command = '/usr/bin/dmesg -T'.split()

todaydate = time.strftime("%d-%m-%y")
filename = 'dmesg.txt' + todaydate
sys.stdout=open(filename,"a")

for line in run_command(command):
  print(line.strip())
sys.stdout.close()
