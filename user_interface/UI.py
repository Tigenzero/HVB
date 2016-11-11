__author__ = 'mhull'
import wx
import os
import logging
from Settings import Settings
from round_manager import MasterControl
from user_interface.window_2 import Window2
from user_interface.util import display_message, get_help_file
from player.player_config import PlayerConfig

class UI(wx.Frame):

    def __init__(self, parent, title):
            super(UI, self).__init__(parent, title=title, size=(420, 450))
            self.InitUI()
            self.Centre()
            self.Show(True)

    def InitUI(self):
        panel = wx.Panel(self)
        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)
        panel.SetBackgroundColour('#4f5049')
        #main box
        vbox = wx.BoxSizer(wx.VERTICAL)
        #Picture Panel
        wx_grinder = self.get_grinder_image("grinder.jpg")
        vbox.Add(wx.StaticBitmap(panel, -1, wx_grinder, (10, 10), (wx_grinder.GetWidth(), wx_grinder.GetHeight())), 0, wx.ALL, 5)
        #First Row Box
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        #Player Configuration combobox
        player_names = []
        if len(Settings.Player_List) > 0:
            for player in Settings.Player_List:
                player_names.append(player.name)
        player_names.append("new")
        self.cb = wx.ComboBox(panel, size=(200, 0), name="player_config", choices=player_names)
        self.cb.SetEditable(False)
        self.cb.SetSelection(0)
        self.cb.Bind(wx.EVT_COMBOBOX, self.set_player)
        UI.set_player(self, event=wx.EVT_COMBOBOX)
        hbox1.Add(self.cb, flag=wx.EXPAND | wx.RIGHT)
        #Player Configuration Button
        browse_button = wx.Button(panel, label="Configure", size=(75, 20))
        browse_button.Bind(wx.EVT_BUTTON, self.configure_character)
        hbox1.Add(browse_button, flag=wx.LEFT, border=10)
        #Player Delete Button
        delete_button = wx.Button(panel, label="Delete", size=(75, 20))
        delete_button.Bind(wx.EVT_BUTTON, self.delete_character)
        hbox1.Add(delete_button, flag=wx.LEFT, border=10)
        #Insertion of First Row Box
        vbox.Add(hbox1, flag=wx.LEFT | wx.TOP, border=10)
        #Second Row Box
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        #Auto Recover Checkbox
        self.recover_checkbox = wx.CheckBox(panel, label='Auto Recover')
        self.recover_checkbox.SetFont(font)
        self.recover_checkbox.SetValue(Settings.recover)
        self.recover_checkbox.Bind(wx.EVT_CHECKBOX, self.autorecover, self.recover_checkbox)
        hbox2.Add(self.recover_checkbox)
        #Insertion of Second Row Box
        vbox.Add(hbox2, flag=wx.LEFT | wx.TOP, border=10)
        #Third Row Box
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        #Start Game Button
        quick_btn1 = wx.Button(panel, label='Quick Start', size=(100, 20))
        quick_btn1.Bind(wx.EVT_BUTTON, self.launch_game)
        hbox3.Add(quick_btn1)
        #Start Grindfest Button
        btn2 = wx.Button(panel, label='Start Grindfest', size=(100, 20))
        btn2.Bind(wx.EVT_BUTTON, self.launch_grindfest)
        hbox3.Add(btn2, flag=wx.LEFT, border=30)
        #Insertion of Third Row Box
        vbox.Add(hbox3, flag=wx.TOP | wx.LEFT, border=10)
        #Fourth Row Box
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        #Start Arena Button
        btn1 = wx.Button(panel, label='Start Arena', size=(100, 20))
        btn1.Bind(wx.EVT_BUTTON, self.launch_arena)
        hbox4.Add(btn1)
        #Start Arena Combobox 1
        self.start_arena = wx.ComboBox(panel, size=(150, 0), name="Starting Arena", choices=Settings.Arenas)
        self.start_arena.SetEditable(False)
        self.start_arena.SetSelection(0)
        hbox4.Add(self.start_arena, flag=wx.EXPAND | wx.LEFT, border=10)
        #End Arena Combobox 2
        self.end_arena = wx.ComboBox(panel, size=(150, 0), name="Ending Arena", choices=Settings.Arenas)
        self.end_arena.SetEditable(False)
        self.end_arena.SetSelection(21)
        hbox4.Add(self.end_arena, flag=wx.EXPAND | wx.RIGHT | wx.LEFT, border=10)
        #Insertion Fourth Row Box
        vbox.Add(hbox4, flag=wx.LEFT | wx.TOP, border=10)
        #Fifth Row Box
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        #Help Button
        btn1 = wx.Button(panel, label='Help', size=(400, 30))
        btn1.Bind(wx.EVT_BUTTON, self.display_help)
        hbox5.Add(btn1, flag=wx.RIGHT, border=10)
        #Insertion of Fifth Row Box
        vbox.Add(hbox5, flag=wx.LEFT | wx.TOP, border=10)

        panel.SetSizer(vbox)
        panel.Refresh()

    def get_grinder_image(self, filename):
        #wx_bmap = wx.EmptyBitmap(1, 1)     # Create a bitmap container object. The size values are dummies.
        wx_bmap = wx.Image(os.getcwd() + "\\images\\" + filename, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        #wx_bmap.LoadFile(os.getcwd() + "\\images\\" + filename, wx.BITMAP_TYPE_ANY)   # Load it with a file image.
        return wx_bmap

    def display_help(self, event):
        logging.debug("Help Activated")
        help_doc = get_help_file("help.txt")
        display_message(help_doc)

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
            if len(Settings.Player.name) > 0 and Settings.Player.name == self.cb.GetValue():
                return True
        except:
            display_message("PLAYER NOT VALID")
            return False

    def launch_game(self, event):
        if self.player_validate():
            master = MasterControl()
            master.start()
            self.end_of_game()

    def launch_grindfest(self, event):
        if self.player_validate():
            master = MasterControl(1)
            master.start()
            #code.start_grindfest()
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
            master = MasterControl(2, start_num + 1, end_num + 1)
            master.start()
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
            #display_message("min_sleep is now {}. max_sleep is now {}".format(Settings.min_sleep, Settings.max_sleep))
        #else:
            #display_message("Minimum Sleep needs to be greater than 0 and less than Maxiumum Sleep")

    def end_of_game(self):
        display_message("Bot has Ended")

    def configure_character(self, event):
        #Save for Later
        Window2(wx.GetApp().TopWindow, title="Player Config", combobox=self.cb).Show()
        #get_character_stats()

    def delete_character(self, event):
        name = self.cb.GetValue()
        message = "WARNING: Are you sure you want to delete {}?".format(name)
        dial = wx.MessageDialog(None, message, "Character Delete", wx.YES_NO)
        if dial.ShowModal() == wx.ID_YES:
            rewrite_player_file(name)
            config = PlayerConfig()
            config.get_player_config()
            Settings.Player_List = config.player_list
            self.cb.Clear()
            if len(Settings.Player_List) > 0:
                print len(Settings.Player_List)
                for player in Settings.Player_List:
                    if not name == player.name:
                        self.cb.Append(player.name)
            self.cb.Append("new")
            self.cb.SetSelection(0)


if __name__ == '__main__':

    app = wx.App()
    UI(None, title='Grind Buster')
    app.MainLoop()


def rewrite_player_file(name):
    if name == "new":
        return
    fpath = os.getcwd() + "\\" + "Player.txt"
    if os.path.isfile("Player.txt"):
        with open(fpath, 'r+') as f:
            lines = f.readlines()
            f.seek(0)
            f.truncate()
            name_found = False
            for line in lines:
                line_split = line.split(':')
                if line_split[0] == "name":
                    if line_split[1].rstrip("\n") == name:
                        name_found = True
                    else:
                        name_found = False
                        f.write(line)
                elif name_found:
                    continue
                else:
                    f.write(line)
        f.close()


def get_character_stats():
        stats = "Name: " + Settings.Player.name + "\n"
        stats = stats + "Style: " + str(Settings.Player.style) + "\n"
        stats = stats + "Premium: " + str(Settings.Player.premium) + "\n"
        stats = stats + "Skills: " + str(Settings.Player.skills) + "\n"
        stats = stats + "Special Attack: " + str(Settings.Player.special_attack) + "\n"
        display_message(stats)

#app = wx.App(False) #Create a new app, dont redirect stdout/stderr to a window
#frame = wx.Frame(None, wx.ID_ANY, "Grind Buster") #a frame is a top-level window
#frame.Show(True)    #show the frame

#app.MainLoop()
