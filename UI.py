__author__ = 'mhull'
import wx

app = wx.App(False) #Create a new app, dont redirect stdout/stderr to a window
frame = wx.Frame(None, wx.ID_ANY, "Grind Buster") #a frame is a top-level window
frame.Show(True)    #show the frame

app.MainLoop()