import datetime
import wx

print datetime.datetime.utcnow()

class App(wx.App):

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

