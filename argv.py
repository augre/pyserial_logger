import os
import sys, getopt

class Config:
   def __init__(self, argv=sys.argv[1:]):
      self.argv=argv
   ##    serial
      self.baudrate = 115200
      self.port = 8

   ##    file
      self.location="C:/Z3/customers/" #+ customer name/serial beginning
      self.name=0 #serial number end
      self.mode='a' #append to file
   def cmdInputs(self):
      
      try:
   ## no : after h because no arg needs to be specified for help       
         opts, args = getopt.getopt(self.argv,"hb:p:l:f:") 
   ##      print opts
   ##      print args
      except getopt.GetoptError:
         print 'test.py -b <baudrate> -p <port number> -l <path> -f <filename>'
         print 'defaults: ', self.baudrate, self.port, self.location, self.name
         sys.exit(2)
      for opt, arg in opts:
         print opt, arg
         if opt == '-h':
            print 'test.py -b <baudrate> -p <port number> -l <path> -f <filename>'
            print 'defaults: ', self.baudrate, self.port, self.location, self.name
            sys.exit()
         elif opt in ("-b", "--baudrate"):
            self.baudrate = arg
         elif opt in ("-p", "--port"):
            self.port = arg
         elif opt in ("-l", "--location"):
            self.location = self.location+arg
         elif opt in ("-f", "--name"):
            self.name = arg
##      print 'baud is: ', self.baudrate
##      print 'port is: ', self.port
##      print 'location is: ', self.location
##      print 'name is: ', self.name
   def writeConfig(self):
      f=open('config', 'w')
      f.write("baudrate %s\nport %s\nlocation %s\nname %s" % (str(self.baudrate), str(self.port), self.location, str(self.name)))
      f.closed
   def readConfig(self):
      with open('config', 'r') as f:
         opts=f.read()
         opts=opts.split("\n")
         for opt in opts:
            if opt.split()[0]=='baudrate':
               self.baudrate=opt.split()[1]
               print(self.baudrate)
            elif opt.split()[0]=='port':
               self.port=opt.split()[1]
               print(self.port)
            elif opt.split()[0]=='location':
               self.location=opt.split()[1]
               print(self.location)
            elif opt.split()[0]=='name':
               self.name=opt.split()[1]
               print(self.name)
if __name__ == "__main__":
    a=Config()
    a.cmdInputs()


