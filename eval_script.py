#!/usr/bin/env python

import os
import sys
import time
import argparse
import re


#READ VIDEO FILES
f = open('vidlist.txt','r');
vidfiles = f.readlines();
f.close()

print(vidfiles[0]);

bbox=[]
#READ CORRESPONDING ANNOTATION FILES
f = open('annofile.txt','r')
for filename in f:
	a = filename.rstrip('\n');
	f1=open(a);
	lines = f1.readlines();
	imgname = lines[0].rstrip('\n');
	imgnum = map(int,re.findall('\d+',imgname));
	boundingbox = lines[2];
	bbox.append(boundingbox.rstrip('\n'))			
f.close()

print("Wrote video paths to file.. Running the evaluation code")

for i in range(len(vidfiles)):
	bbox_ = map(int,(map(float,bbox[i].split())));
	command = 'python run.py --bbox=' + str(bbox_[0]) + ',' + str(bbox_[1]) + ','+ str(bbox_[2]) + ',' + str(bbox_[3]) + ' --skip ' + str(imgnum[0]-1) + ' --output-dir ./output/ ' + vidfiles[i].rstrip('\n') + '/{:05d}.png';
	print(command)
	try:
 		os.system(command)
	except Exception, e:
		print e
		continue


	

