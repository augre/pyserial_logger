#!/usr/bin/python
# -*- coding: cp1252 -*-

# get lines of text from serial port, save them to a file

#this line uses print as a function like inpython 3
from __future__ import print_function


import serial, io
import time
import datetime
import os
import sys



addr  = 8  # serial port to read data from
baud  = 115200            # baud rate for serial port
location =os.path.normpath("C:/Z3/customers/ADLINK_Sonosite/Logs/30002201142310")

fname = 1   # log file to save data in, serial number
fmode = 'a'             # log file mode = append
flag=0
fstart="Update Image Detected"
fend="Preloading gstreamer components"
testEnd="="




with serial.Serial(addr,baud) as pt:
    spb = io.TextIOWrapper(io.BufferedRWPair(pt,pt,1),
        encoding='ascii', errors='ignore', newline='\r',line_buffering=True)
    
    while (1):
        x = spb.readline()  # read one line of text from serial port
        if x.find(fend)!=-1:
            flag=1
            print('\n\nFlag Set\n\n', file=sys.stderr)
            pt.write('\n')

            
        elif x.find(fstart)!=-1 and flag==1:
            fname=fname+1
            flag=0
			
			
        with open((location+str(fname)+".log"),fmode) as outf:
            if x.find(fstart)!=-1:
                ts = time.time()
                outf.write("\n\n\n["+datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')+"]\n\n\n")  # timestamp at the beginning of the file 
            print (x,end='')    # echo line of text on-screen
##            outf.write("["+str(datetime.datetime.utcnow())+"]"+x)       # write line of text to file]
            outf.write(x)
            outf.flush()        # make sure it actually gets written out
