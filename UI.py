__author__ = 'mhull'
import wx
import Image
import os
import logging
import code
import Settings


class UI(wx.Frame):

    def __init__(self, parent, title):
            super(UI, self).__init__(parent, title=title, size=(420, 450))
            self.InitUI()
            self.Centre()
            self.Show(True)

    def InitUI(self):
        panel = wx.Panel(self)
        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)
        panel.SetBackgroundColour('#4f5049')
        vbox = wx.BoxSizer(wx.VERTICAL)
        wx_grinder = self.get_grinder_image("grinder.jpg")
        vbox.Add(wx.StaticBitmap(panel, -1, wx_grinder, (10, 10), (wx_grinder.GetWidth(), wx_grinder.GetHeight())), 0, wx.ALL, 5)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        player_names = []
        if len(Settings.Player_List) > 0:
            for player in Settings.Player_List:
                player_names.append(player.name)
        player_names.append("new")
        self.cb = wx.ComboBox(panel, size=(200, 0), name="player_config", choices=player_names)
        self.cb.SetEditable(False)
        self.cb.SetSelection(0)
        self.cb.Bind(wx.EVT_COMBOBOX, self.set_player)
        self.set_player(event=wx.EVT_COMBOBOX)
        hbox1.Add(self.cb, flag=wx.EXPAND | wx.RIGHT)
        browse_button = wx.Button(panel, label="Configure", size=(75, 20))
        browse_button.Bind(wx.EVT_BUTTON, self.configure_character)

        hbox1.Add(browse_button, flag=wx.LEFT, border=10)
        vbox.Add(hbox1, flag=wx.LEFT | wx.TOP, border=10)
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        self.recover_checkbox = wx.CheckBox(panel, label='Auto Recover')
        self.recover_checkbox.SetFont(font)
        self.recover_checkbox.SetValue(Settings.recover)
        self.recover_checkbox.Bind(wx.EVT_CHECKBOX, self.autorecover, self.recover_checkbox)
        hbox4.Add(self.recover_checkbox)
        st2 = wx.StaticText(panel, label='Sleep Range')
        st2.SetFont(font)
        hbox4.Add(st2, flag=wx.LEFT, border=20)
        st2 = wx.StaticText(panel, label='Min:')
        st2.SetFont(font)
        hbox4.Add(st2, flag=wx.LEFT, border=15)
        self.sleep_min = wx.TextCtrl(panel, size=(30, 20))
        self.sleep_min.SetValue(Settings.min_sleep.__str__())
        self.sleep_min.Bind(wx.EVT_TEXT, self.edit_sleep, self.sleep_min)
        hbox4.Add(self.sleep_min, proportion=1, flag=wx.LEFT, border=5)
        st2 = wx.StaticText(panel, label='Max: ')
        st2.SetFont(font)
        hbox4.Add(st2, flag=wx.LEFT, border=20)
        self.sleep_max = wx.TextCtrl(panel, size=(30, 20))
        self.sleep_max.SetValue(Settings.max_sleep.__str__())
        self.sleep_max.Bind(wx.EVT_TEXT, self.edit_sleep, self.sleep_max)
        hbox4.Add(self.sleep_max, proportion=1, flag=wx.LEFT, border=5)
        vbox.Add(hbox4, flag=wx.LEFT | wx.TOP, border=10)

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        quick_btn1 = wx.Button(panel, label='Quick Start', size=(100, 20))
        quick_btn1.Bind(wx.EVT_BUTTON, self.launch_game)
        hbox5.Add(quick_btn1)
        btn2 = wx.Button(panel, label='Start Grindfest', size=(100, 20))
        btn2.Bind(wx.EVT_BUTTON, self.launch_grindfest)
        hbox5.Add(btn2, flag=wx.LEFT, border=30)
        vbox.Add(hbox5, flag=wx.TOP | wx.LEFT, border=10)

        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(panel, label='Start Arena', size=(100, 20))
        btn1.Bind(wx.EVT_BUTTON, self.launch_arena)
        hbox6.Add(btn1)
        self.start_arena = wx.ComboBox(panel, size=(150, 0), name="Starting Arena", choices=Settings.Arenas)
        self.start_arena.SetEditable(False)
        self.start_arena.SetSelection(0)
        hbox6.Add(self.start_arena, flag=wx.EXPAND | wx.LEFT, border=10)
        self.end_arena = wx.ComboBox(panel, size=(150, 0), name="Ending Arena", choices=Settings.Arenas)
        self.end_arena.SetEditable(False)
        self.end_arena.SetSelection(21)
        hbox6.Add(self.end_arena, flag=wx.EXPAND | wx.RIGHT | wx.LEFT, border=10)
        vbox.Add(hbox6, flag=wx.LEFT | wx.TOP, border=10)

        hbox7 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(panel, label='Help', size=(400, 30))
        btn1.Bind(wx.EVT_BUTTON, self.display_help)
        hbox7.Add(btn1, flag=wx.RIGHT, border=10)
        vbox.Add(hbox7, flag=wx.LEFT | wx.TOP, border=10)

        panel.SetSizer(vbox)
        panel.Refresh()

    def get_grinder_image(self, filename):
        #wx_bmap = wx.EmptyBitmap(1, 1)     # Create a bitmap container object. The size values are dummies.
        wx_bmap = wx.Image(os.getcwd() + "\\images\\" + filename, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        #wx_bmap.LoadFile(os.getcwd() + "\\images\\" + filename, wx.BITMAP_TYPE_ANY)   # Load it with a file image.
        return wx_bmap

    def display_help(self, event):
        logging.debug("Help Activated")

    def get_value(self, event):
        dial = wx.MessageDialog(None, self.cb.GetValue(), "Info", wx.OK)
        dial.ShowModal()
        logging.debug(self.cb.GetValue())

    def set_player(self, event):
        Settings.Player = None
        current_player = self.cb.GetValue()
        for player in Settings.Player_List:
            if player.name == current_player:
                Settings.Player = player
                #dial = wx.MessageDialog(None, "Settings Changed. Player is now " + Settings.Player[0], "Info", wx.OK)
                #dial.ShowModal()

    def player_validate(self):
        try:
            if len(Settings.Player.name) > 0:
                return True
        except:
            display_message("PLAYER NOT VALID")
            return False

    def launch_game(self, event):
        if self.player_validate():
            code.startGame()
            self.end_of_game()

    def launch_grindfest(self, event):
        if self.player_validate():
            code.start_grindfest()
            self.end_of_game()

    #UNFINISHED
    def launch_arena(self, event):
        start = self.start_arena.GetValue()
        end = self.end_arena.GetValue()
        start_num = 0
        end_num = 21
        for i in range(0, len(Settings.Arenas)):
            if start == Settings.Arenas[i]:
                start_num = i
                #display_message("start arena found")
            if end == Settings.Arenas[i]:
                end_num = i
                #display_message("end arena found")

        if self.player_validate():
            code.start_arena(start_num + 1, end_num + 1)
            self.end_of_game()

    def autorecover(self, event):
        if self.recover_checkbox.GetValue():
            Settings.recover = True
        else:
            Settings.recover = False
        #display_message("Autorecover is now {}".format(Settings.recover))

    def edit_sleep(self, event):
        if 0 < float(self.sleep_min.GetValue()) < float(self.sleep_max.GetValue()):
            Settings.min_sleep = float(self.sleep_min.GetValue())
            Settings.max_sleep = float(self.sleep_max.GetValue())
            display_message("min_sleep is now {}. max_sleep is now {}".format(Settings.min_sleep, Settings.max_sleep))
        else:
            display_message("Minimum Sleep needs to be greater than 0 and less than Maxiumum Sleep")

    def end_of_game(self):
        display_message("Bot has Ended")

    def configure_character(self, event):
        Window2(wx.GetApp().TopWindow, title="Player Config").Show()


if __name__ == '__main__':

    app = wx.App()
    UI(None, title='Grind Buster')
    app.MainLoop()


def display_message(value):
    dial = wx.MessageDialog(None, value, "Info", wx.OK)
    dial.ShowModal()

#app = wx.App(False) #Create a new app, dont redirect stdout/stderr to a window
#frame = wx.Frame(None, wx.ID_ANY, "Grind Buster") #a frame is a top-level window
#frame.Show(True)    #show the frame

#app.MainLoop()

class Window2(wx.Frame):

    def __init__(self, parent, title):
            super(Window2, self).__init__(parent, title=title, size=(420, 450))
            self.InitWindow2()
            self.Centre()
            self.Show(True)
    def InitWindow2(self):
        panel = wx.Panel(self)
        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)
        panel.SetBackgroundColour('#4f5049')
        vbox = wx.BoxSizer(wx.VERTICAL)