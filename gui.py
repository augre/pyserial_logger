# -*- coding: cp1252 -*-
import datetime
import wx

print datetime.datetime.utcnow()

class App(wx.App):
    """
Notice that we didn’t define an __init__() method for our application class. In
Python, this means that the parent method, wx.App.__init__(), is automatically
invoked on object creation. This is a good thing. If you define an __init__()
method of your own, don’t forget to call the __init__() of the base class, like this:
"""

    def __init__(self):
        wx.App.__init__(self)

    def OnInit(self):
        frame=wx.Frame(parent=None, title='Bare')
        frame.Show(False)
        while(str(datetime.datetime.utcnow()).find("21:26:")!=-1):
            print "in the loop"
            print datetime.datetime.utcnow()
            frame.Show()

        print "out of the loop"
        print datetime.datetime.utcnow()
        frame.Show(False)
        return True

app=App()
app.MainLoop()

