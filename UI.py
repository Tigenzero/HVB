__author__ = 'mhull'
import wx
import Image
import os

class UI(wx.Frame):

    def __init__(self, parent, title):
            super(UI, self).__init__(parent, title=title, size=(420, 500))

            self.InitUI()
            self.Centre()
            self.Show()

    def InitUI(self):
        panel = wx.Panel(self)
        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)
        panel.SetBackgroundColour('#4f5049')
        vbox = wx.BoxSizer(wx.VERTICAL)
        wx_grinder = self.get_grinder_image("grinder.jpg")
        #self.imageCtrl = wx.StaticBitmap(self, -1, wx_grinder, (10, 5), (wx_grinder.GetWidth(), wx_grinder.GetHeight()))
        vbox.Add(wx.StaticBitmap(panel, -1, wx_grinder, (10, 10), (wx_grinder.GetWidth(), wx_grinder.GetHeight())), 0, wx.ALL, 5)
        #vbox.Add(self.imageCtrl, 0, wx.ALL, 5)
        #vbox.Add((15, 15))

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        #st1 = wx.StaticText(panel, label='Player Name')
        #st1.SetFont(font)
        #hbox1.Add(st1, flag=wx.RIGHT, border=8)
        cb = wx.ComboBox(panel, size=(200, 0), name="player_config")
        cb.SetEditable(False)
        hbox1.Add(cb, flag=wx.EXPAND | wx.RIGHT)
        browse_button = wx.Button(panel, label="Configure")
        hbox1.Add(browse_button, flag=wx.LEFT, border=10)
        vbox.Add(hbox1, flag=wx.LEFT | wx.TOP, border=10)


        #hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        #st2 = wx.StaticText(panel, label='Matching Classes')
        #st2.SetFont(font)
        #hbox2.Add(st2)
        #vbox.Add(hbox2, flag=wx.LEFT | wx.TOP, border=10)

        #vbox.Add((-1, 10))

        #hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        #tc2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        #hbox3.Add(tc2, proportion=1, flag=wx.EXPAND)
        #vbox.Add(hbox3, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND,
        #    border=10)

        #vbox.Add((-1, 25))

        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        cb1 = wx.CheckBox(panel, label='Auto Recover')
        cb1.SetFont(font)
        hbox4.Add(cb1)
        #cb2 = wx.CheckBox(panel, label='Nested Classes')
        #cb2.SetFont(font)
        #hbox4.Add(cb2, flag=wx.LEFT, border=10)
        #cb3 = wx.CheckBox(panel, label='Non-Project classes')
        #cb3.SetFont(font)
        #hbox4.Add(cb3, flag=wx.LEFT, border=10)
        sleep_min = wx.TextCtrl(panel, size=(20, 20))
        hbox4.Add(sleep_min, proportion=1, flag=wx.LEFT, border=30)

        font2 = font
        st2 = wx.StaticText(panel, label='-')
        font2.SetPointSize(20)
        st2.SetFont(font2)
        hbox4.Add(st2, border=10)

        sleep_max = wx.TextCtrl(panel, size=(20, 20))
        hbox4.Add(sleep_max, proportion=1, flag=wx.LEFT, border=30)

        st2 = wx.StaticText(panel, label='Sleep')
        st2.SetFont(font)
        hbox4.Add(st2, flag=wx.LEFT, border=10)

        vbox.Add(hbox4, flag=wx.LEFT, border=10)

        #vbox.Add((-1, 25))

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(panel, label='Ok', size=(70, 30))
        hbox5.Add(btn1)
        btn2 = wx.Button(panel, label='Close', size=(70, 30))
        hbox5.Add(btn2, flag=wx.LEFT|wx.BOTTOM, border=5)
        vbox.Add(hbox5, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)

        panel.SetSizer(vbox)
        panel.Refresh()

    def get_grinder_image(self, filename):
        #wx_bmap = wx.EmptyBitmap(1, 1)     # Create a bitmap container object. The size values are dummies.
        wx_bmap = wx.Image(os.getcwd() + "\\images\\" + filename, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        #wx_bmap.LoadFile(os.getcwd() + "\\images\\" + filename, wx.BITMAP_TYPE_ANY)   # Load it with a file image.
        return wx_bmap

if __name__ == '__main__':

    app = wx.App()
    UI(None, title='Grind Buster')
    app.MainLoop()

#app = wx.App(False) #Create a new app, dont redirect stdout/stderr to a window
#frame = wx.Frame(None, wx.ID_ANY, "Grind Buster") #a frame is a top-level window
#frame.Show(True)    #show the frame

#app.MainLoop()