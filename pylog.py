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
import argv

config=argv.Config()
config.cmdInputs()
##config.writeConfig()
config.readConfig()





addr  = config.port  # serial port to read data from
baud  = config.baudrate            # baud rate for serial port
location =os.path.normpath(config.location)

fname = config.name   # log file to save data in, serial number
fmode = config.mode             # log file mode = append

print(addr, baud, location, fname, fmode)

flag=0
fstart="DM385-GP rev 1.0"
fend="TEST PASS"
testFail="TEST FAIL" # have to add a case when test fails clear flag and
                     # print warning
stopBoot="factory jumper detected"
promt="Z3-DM385"
com1="run update-env\n"
com1Flag=0
com1Success="Writing to Nand... done"
com1SuccessFlag=0
com2="run update-ubifs-all\n"
com2Flag=0
updateSuccess="*** UPDATE SUCCESS ****"
updateFlag=0


##
## TO DO: add mac address check for session, as whole to avoid double check for
                     ##module


with serial.Serial(addr,baud) as pt:
    spb = io.TextIOWrapper(io.BufferedRWPair(pt,pt,1),
        encoding='ascii', errors='ignore', newline='\r',line_buffering=True)
    
    while (1):
        x = spb.readline()  # read one line of text from serial port
        if x.find(fend)!=-1:
            flag=1
            print('\n\nFlag Set\n\n', file=sys.stderr)
            pt.write('\n')

        elif x.find(stopBoot)!=-1 and updateFlag==0:
            print('\n\nSTOP BOOT\n\n', file=sys.stderr)
            pt.write('S')
            pt.write('\n')
            
        if x.find(promt)!=-1 and com1Flag==0:
            print('\n\nPROMT com1\n\n', file=sys.stderr)
            pt.write(com1)
            com1Flag=1
            
        if x.find(com1Success)!=-1 and com1Flag==1 and com2Flag==0:
            print('\n\ncom1SuccessFlag\n\n', file=sys.stderr)
            com1SuccessFlag=1
            pt.write('\n')
            
        if x.find(promt)!=-1 and com1Flag==1 and com1SuccessFlag==1 and updateFlag==0:
            print('\n\nPROMT com2\n\n', file=sys.stderr)
            pt.write(com2)
            com2Flag=1

        if x.find(updateSuccess)!=-1 and com2Flag==1:
            updateFlag=1
            
            
        elif x.find(fstart)!=-1 and flag==1:
            fname=fname-1
            flag=0
            com1Flag=0
            com2Flag=0
            updateFlag=0
            com1SuccessFlag=0
            outf.close() #close the previous file
			
			
        with open((location+str(fname)+".log"),fmode) as outf:
            print('=', file=sys.stderr)
            if x.find(fstart)!=-1:
                ts = time.time()
                outf.write("\n\n\n["+datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')+"]\n\n\n")  # timestamp at the beginning of the file 
            print (x,end='')    # echo line of text on-screen
##            outf.write("["+str(datetime.datetime.utcnow())+"]"+x)       # write line of text to file]
            outf.write(x)
            outf.flush()        # make sure it actually gets written out
