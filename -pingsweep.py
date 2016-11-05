#!/usr/bin/python

###############################################
# Simple local subnet ping sweeper 
# Author: u.ilhan24@gmail.com
###############################################

import os
import re
import sys

showline = re.compile(r"(\d) received")
verdict = ("Offline","Online","Alive")

# ping sweep of the local C class subnet 192.168.1./24 
for host in range(1,254):
	ip = "192.168.1."+str(host)
	shootping = os.popen("ping -c 1 "+ip, "r")
	print ip,
	sys.stdout.flush()
	while 1:
		line = shootping.readline()
		if not line:break
		outcome = re.findall(showline, line)
		if outcome:
			print verdict[int(outcome[0])]
