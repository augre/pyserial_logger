#!/usr/bi/env python
# -*- coding: cp1252 -*-

##If wxPython is controlling the standard streams, then text sent to the streams via
##any mechanism—including a print statement or a system traceback—is redirected
##to a separate wxPython frame. Text sent to the streams before the wxPython application
##begins or after it ends is, of course, processed normally.

import wx
import sys

class Frame(wx.Frame):
    def __init__(self,parent, id, title):
        print "Frame __init__"
        wx.Frame.__init__(self, parent, id, title)


class App(wx.App):
    def __init__(self, redirect, filename=None):
        print "App __init__"
        wx.App.__init__(self, redirect, filename)

    def OnInit(self):
        print "OnInit"
        self.frame=Frame(parent=None, id=-1, title='Startup')
        self.frame.Show()
        self.SetTopWindow(self.frame)
        print >> sys.stderr, "A pretend error message"
        return True

    def OnExit(self):
        print "onexit"

if __name__=="__main__":
    app=App(redirect=True)
    print "before MainLoop"
    app.MainLoop()
    print "After MainLoop"


##Gondolom ez akkor lehet hasznos ha peldaul mar exe van belole es nincsen tobbe konzol.
