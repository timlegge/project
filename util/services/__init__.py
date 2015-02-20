#!/usr/bin/env python

import subprocess

def restart(name):
	if name is None:
		return
	command = ['/sbin/service', name, 'restart'];
	#shell=FALSE for sudo to work.
	subprocess.call(command, shell=False)

def stop(name):
	if name is None:
		return
	command = ['/sbin/service', name, 'stop'];
	#shell=FALSE for sudo to work.
	subprocess.call(command, shell=False)
