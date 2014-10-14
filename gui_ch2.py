#!/usr/bi/env python
# -*- coding: cp1252 -*-

##If wxPython is controlling the standard streams, then text sent to the streams via
##any mechanism—including a print statement or a system traceback—is redirected
##to a separate wxPython frame. Text sent to the streams before the wxPython application
##begins or after it ends is, of course, processed normally.


##If the redirect parameter is True, then the second parameter, filename,
##can also be set. If so, output is redirected to a file with that name, rather than to
##the wxPython frame.

##will cause all the redirected lines to be sent to a file named output. The App
##__init_ and after MainLoop messages will still be sent to the console, however,
##because they occur outside of the time period where the wx.App object has control
##of the streams.

import wx
import sys

class Frame(wx.Frame):
    def __init__(self,parent, id, title):
        print "Frame __init__"
        print wx.ID_LOWEST, wx.ID_HIGHEST
        wx.Frame.__init__(self, parent, id, title, size=(300,100))

        #added close button
        panel=wx.Panel(self)
        button=wx.Button(panel, label="close", pos=(125,10), size=(50,50))
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)
        #self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def OnCloseMe(self, event):
        self.Close(True)
        

    def OnCloseWindow(self, event):
        self.Destroy()


class App(wx.App):
    def __init__(self, redirect, filename=None):
        print "App __init__"
        wx.App.__init__(self, redirect, filename)
        #application to continue after the last window
        #closes
        #self.SetExitOnFrameDelete(False)
        

    def OnInit(self):
        print "OnInit"
        self.frame=Frame(parent=None, id=-1, title='Startup')
        self.frame.Show()
        print self.frame.GetId()
        self.SetTopWindow(self.frame)
        print >> sys.stderr, "A pretend error message"
        return True

    def OnExit(self):
        print "onexit"

if __name__=="__main__":
    app=App(redirect=False)
    print "before MainLoop"
    app.MainLoop()
    print "After MainLoop"


##Gondolom ez akkor lehet hasznos ha peldaul mar exe van belole es nincsen tobbe konzol.
