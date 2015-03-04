#!/usr/bin/python
# -*- coding: cp1252 -*-

#use print as a function like in python 3
from __future__ import print_function

import serial, io
import time
import datetime
import os
import sys

##
## TO DO: add mac address check for session, as whole to avoid double check for
                     ##module
class Test:
    def __init__(self, location="C:/Z3/customers/KSI/", last3Digits, direction="down"):
        self.location=os.path.normpath(location)
        self.fStart="DDR OK"
        self.fEnd="TEST PASS"
        self.testFail="TEST FAIL"
        self.doneFlag=0
        self.direction=direction
        self.last3Digits=last3Digits

    def passed(self, line):
        if line.find(self.fEnd)!=-1:
            self.doneFlag=1
            return 1
        else:
            return 0

    def newModule(self, line):
        if line.find(self.fStart)!=-1 and doneFlag:
            self.doneFlag=0
            return 1
        else: 
            return 0
    
    def changeFName(self):
        if self.direction=="down":
            self.last3Digits=self.last3Digits-1
            return 1
        elif self.direction=="up"
            self.last3Digits=self.last3Digits+1
            return 1
        else:
            return 0

    def timeStamp(self):
        ts=time.time()
        return "\n\n\n["+datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')+"]\n\n\n"


if __name__ == '__main__':
    addr  = 8               # serial port to read data from
    baud  = 115200          # baud rate for serial port

    fmode = 'a'             # log file mode = append

    m=Test("path....", 100, "down")

    with serial.Serial(addr,baud) as pt:
        spb = io.TextIOWrapper(io.BufferedRWPair(pt,pt,1),
            encoding='ascii', errors='ignore', newline='\r',line_buffering=True)
    
        while (1):
            line = spb.readline()
            if m.passed(line):
                print('\n\nFlag Set\n\n', file=sys.stderr)
            
            elif m.newModule(line):
                m.changeFName()
			
            with open((m.location+str(m.last3Digits)+".log"),fmode) as outf:
                if m.newModule(line):
                    outf.write(m.timestamp())
                print (line,end='')
                outf.write(line)
                outf.flush()
