#!/usr/bin/env python

import shlex
import subprocess

def run_command(command):
    """given shell command, returns stdout and stderr"""
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')

command = shlex.split('/bin/systemctl status nslcd.service')

for line in run_command(command):
  if "dead" in line:
    print("Restarting the nslcd.service...")
    cmd = shlex.split('systemctl start nslcd.service')
    run_command(cmd)
