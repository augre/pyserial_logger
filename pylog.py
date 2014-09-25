#!/usr/bin/python
# get lines of text from serial port, save them to a file

from __future__ import print_function
import serial, io

addr  = 16  # serial port to read data from
baud  = 115200            # baud rate for serial port
fname = 1   # log file to save data in
fmode = 'a'             # log file mode = append

with serial.Serial(addr,baud) as pt:
    spb = io.TextIOWrapper(io.BufferedRWPair(pt,pt,1),
        encoding='ascii', errors='ignore', newline='\r',line_buffering=True)
    #spb.readline()  # throw away first line; likely to start mid-sentence (incomplete)
    while (1):
        with open(str(fname),fmode) as outf:
            x = spb.readline()  # read one line of text from serial port
            print (x,end='')    # echo line of text on-screen
            outf.write(x)       # write line of text to file
            outf.flush()        # make sure it actually gets written out
        if x.find("TEST FAIL"):
            fname=fname+1
        else:
            pass



