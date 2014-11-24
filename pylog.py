#!/usr/bin/python
# -*- coding: cp1252 -*-

# get lines of text from serial port, save them to a file




import serial, io
import time
import datetime
import os
import sys, getopt


def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print 'Input file is "', inputfile
   print 'Output file is "', outputfile





if __name__ == "__main__":
   main(sys.argv[1:])
   
   addr  = '/dev/ttyUSB0'  # serial port to read data from
   baud  = 115200            # baud rate for serial port
   location =os.path.normpath("/home/z3/Z3/Customers/Carmanah/0365M051446100")
   fname = 92   # log file to save data in, serial number
   fmode = 'a'             # log file mode = append
   flag=0
   fstart="PSP 2.10.00.08 v0.1"
   fend="# davi"

   with serial.Serial(addr,baud) as pt:
    spb = io.TextIOWrapper(io.BufferedRWPair(pt,pt,1),
        encoding='ascii', errors='ignore', newline='\r',line_buffering=True)
    
    while (1):
        x = spb.readline()  # read one line of text from serial port
        if x.find(fend)!=-1:
            flag=1
            print >> sys.stderr, '\n\nFlag Set\n\n'
            pt.write('\r')

            
        elif x.find(fstart)!=-1 and flag==1:
            fname=fname-1
            flag=0
			
			
        with open((location+str(fname)+".log"),fmode) as outf:
            if x.find(fstart)!=-1:
                ts = time.time()
                outf.write("\n\n\n["+datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')+"]\n\n\n")  # timestamp at the beginning of the file 
            print x    # echo line of text on-screen
##            outf.write("["+str(datetime.datetime.utcnow())+"]"+x)       # write line of text to file]
            outf.write(x)
            outf.flush()        # make sure it actually gets written out