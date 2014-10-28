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



addr  = '/dev/ttyUSB0'  # serial port to read data from
baud  = 115200            # baud rate for serial port
location =os.path.normpath("/home/z3/Z3/Customers/KSI/Box_3/Top_layer")

fname = 245   # log file to save data in, serial number
fmode = 'a'             # log file mode = append
flag=0
fstart="DDR OK"
fend="TEST PASS"
testFail="TEST FAIL" # have to add a case when test fails clear flag and
                     # print warning

##
## TO DO: add mac address check for session, as whole to avoid double check for
                     ##module
##Also, when the serial number is decreased from 100 to 99 a zero 099 is cut off.
##Have to pay special attention to this.
##If serial number is increased there will be a digit added when going from 99 to 100


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
            fname=fname-1
            flag=0
            outf.close() #close the previous file
			
			
        with open((location+str(fname)+".log"),fmode) as outf:
            if x.find(fstart)!=-1:
                ts = time.time()
                outf.write("\n\n\n["+datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')+"]\n\n\n")  # timestamp at the beginning of the file 
            print (x,end='')    # echo line of text on-screen
##            outf.write("["+str(datetime.datetime.utcnow())+"]"+x)       # write line of text to file]
            outf.write(x)
            outf.flush()        # make sure it actually gets written out
