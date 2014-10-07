#!/usr/bin/env python
# -*- coding: cp1252 -*-
##The first line in the file is now a shebang line. It looks like a Python comment,
##which it is, but on some operating systems, such as Linux and Unix, the shebang
##tells the operating system how to find the interpreter that will execute the program
##file. If this program file was then given executable privileges (using the
##chmod command, for example) we could run the program from the operating system
##command line by simply supplying the program name:
##% spare.py
##The shebang line is a convenience for Unix and Mac OS X users and is simply
##ignored on other platforms. Even if you aren’t using one of those systems, it’s
##polite to include it on a script that might be executed cross-platform.


"""Spare.py is a starting point for a wxPython program."""

##We added a module docstring (documentation string). When the first statement in
##a module is a string, that string becomes the docstring for the module and is
##stored in the module’s __doc__ attribute. You can access the docstring in your
##code, some development environments, and even the Python interpreter running
##in interactive mode:
##>>> import spare
##>>> print spare.__doc__
##Spare.py is a starting point for simple wxPython programs.
##>>>


import datetime
import wx

print datetime.datetime.utcnow()

class Frame(wx.Frame):
    pass

class App(wx.App):

    def __init__(self):
        """
        Notice that we didn’t define an __init__() method for our application class. In
        Python, this means that the parent method, wx.App.__init__(), is automatically
        invoked on object creation. This is a good thing. If you define an __init__()
        method of your own, don’t forget to call the __init__() of the base class, like this:
        """
        wx.App.__init__(self)

    def OnInit(self):
        self.frame=Frame(parent=None, title='spare')
        self.frame.Show()
        self.SetTopWindow(self.frame)
        ##Inside the OnInit() method we called the App class’s own SetTopWindow()
        ##method, passing it our newly created frame instance. We didn’t have to define the
        ##SetTopWindow() method because it was inherited from the wx.App parent class. It’s
        ##an optional method that lets wxPython know which frame or dialog should be
        ##considered the main one. A wxPython program can have several frames, with one
        ##designated as the top window for the application. In this case the choice was easy
        ##since we have but one frame.
        return True

if __name__ == '__main__':
    app=App()
    app.MainLoop()

