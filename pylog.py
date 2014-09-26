#!/usr/bin/python
# get lines of text from serial port, save them to a file

from __future__ import print_function
import serial, io
import datetime



addr  = 16  # serial port to read data from
baud  = 115200            # baud rate for serial port
fname = 1   # log file to save data in
fmode = 'a'             # log file mode = append
flag=0
fstart="DDR OK"
fend="TEST FAIL"

with serial.Serial(addr,baud) as pt:
    spb = io.TextIOWrapper(io.BufferedRWPair(pt,pt,1),
        encoding='ascii', errors='ignore', newline='\r',line_buffering=True)
    
    while (1):
        with open(str(fname),fmode) as outf:
            if x.find(fend)!=-1:
                flag=1
            if x.find(fstart)!=-1 and flag==1:
                fname=fname+1
                flag=0
            x = spb.readline()  # read one line of text from serial port
            print (x,end='')    # echo line of text on-screen
            outf.write("["+str(datetime.datetime.utcnow())+"]"+x)       # write line of text to file
            outf.flush()        # make sure it actually gets written out

        else:
            pass



