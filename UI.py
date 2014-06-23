__author__ = 'mhull'
import wx
import os
import logging
import code
import Settings
import Players

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
        UI.cb = wx.ComboBox(panel, size=(200, 0), name="player_config", choices=player_names)
        UI.cb.SetEditable(False)
        UI.cb.SetSelection(0)
        UI.cb.Bind(wx.EVT_COMBOBOX, self.set_player)
        UI.set_player(self, event=wx.EVT_COMBOBOX)
        hbox1.Add(UI.cb, flag=wx.EXPAND | wx.RIGHT)
        #Player Configuration Button
        browse_button = wx.Button(panel, label="Configure", size=(75, 20))
        browse_button.Bind(wx.EVT_BUTTON, self.configure_character)

        hbox1.Add(browse_button, flag=wx.LEFT, border=10)
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
        """#Sleep Settings
        st2 = wx.StaticText(panel, label='Sleep Range')
        st2.SetFont(font)
        hbox2.Add(st2, flag=wx.LEFT, border=20)
        st2 = wx.StaticText(panel, label='Min:')
        st2.SetFont(font)
        hbox2.Add(st2, flag=wx.LEFT, border=15)
        self.sleep_min = wx.TextCtrl(panel, size=(30, 20))
        self.sleep_min.SetValue(Settings.min_sleep.__str__())
        self.sleep_min.Bind(wx.EVT_TEXT, self.edit_sleep, self.sleep_min)
        hbox2.Add(self.sleep_min, proportion=1, flag=wx.LEFT, border=5)
        st2 = wx.StaticText(panel, label='Max: ')
        st2.SetFont(font)
        hbox2.Add(st2, flag=wx.LEFT, border=20)
        self.sleep_max = wx.TextCtrl(panel, size=(30, 20))
        self.sleep_max.SetValue(Settings.max_sleep.__str__())
        self.sleep_max.Bind(wx.EVT_TEXT, self.edit_sleep, self.sleep_max)
        hbox2.Add(self.sleep_max, proportion=1, flag=wx.LEFT, border=5)"""
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
            #display_message("min_sleep is now {}. max_sleep is now {}".format(Settings.min_sleep, Settings.max_sleep))
        #else:
            #display_message("Minimum Sleep needs to be greater than 0 and less than Maxiumum Sleep")

    def end_of_game(self):
        display_message("Bot has Ended")

    def configure_character(self, event):
        #Save for Later
        Window2(wx.GetApp().TopWindow, title="Player Config").Show()
        """stats = "Name: " + Settings.Player.name + "\n"
        stats = stats + "Style: " + str(Settings.Player.style) + "\n"
        stats = stats + "Premium: " + str(Settings.Player.premium) + "\n"
        stats = stats + "Skills: " + str(Settings.Player.skills) + "\n"
        stats = stats + "Special Attack: " + str(Settings.Player.special_attack) + "\n"
        display_message(stats)"""

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

def factory(aClass, *args):
    return aClass(*args)

class Window2(wx.Frame):
    skills = ["Empty", "Absorb", "Cure", "Haste", "Heartseeker", "Protection", "Regen", "Shadow_Veil", "Spark_Life", "Spirit_Shield", "Special", "Blind", "Weaken", "Sleep", "Drain"]
    def __init__(self, parent, title):
            super(Window2, self).__init__(parent, title=title, size=(440, 450))
            self.InitWindow2()
            self.Centre()
            self.Show(True)


    def InitWindow2(self):
        
        panel = wx.Panel(self)
        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)
        panel.SetBackgroundColour('#4f5049')
        #get currently selected player
        config_player = None
        current_player = UI.cb.GetValue()
        if current_player == "new":
            config_player = factory(Players.Player)
        else:
            for player in Settings.Player_List:
                if player.name == current_player:
                    config_player = player
        #Main Box
        vbox = wx.BoxSizer(wx.VERTICAL)
        #First Row Box
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        #Name Box and Input
        st2 = wx.StaticText(panel, label='Name:')
        st2.SetFont(font)
        hbox1.Add(st2)
        self.name = wx.TextCtrl(panel, size=(100, 20))
        self.name.SetValue(config_player.name.__str__())
        hbox1.Add(self.name, flag=wx.LEFT, border=15)
        #Style Box
        st3 = wx.StaticText(panel, label='Style: ')
        st3.SetFont(font)
        hbox1.Add(st3, flag=wx.LEFT, border=15)
        style_names = ["Dual Wield", "1 Handed", "2 Handed", "Niken", "Mage"]
        Window2.style_cb = wx.ComboBox(panel, size=(90, 20), name="Style", choices=style_names)
        Window2.style_cb.SetEditable(False)
        Window2.style_cb.SetSelection(config_player.style)
        hbox1.Add(Window2.style_cb, flag=wx.LEFT, border=10)
        vbox.Add(hbox1, flag=wx.LEFT | wx.TOP, border=10)
        #Second Row Box
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        #Sleep Settings
        st2 = wx.StaticText(panel, label='Sleep Range')
        st2.SetFont(font)
        hbox2.Add(st2, flag=wx.LEFT)
        st2 = wx.StaticText(panel, label='Min:')
        st2.SetFont(font)
        hbox2.Add(st2, flag=wx.LEFT, border=15)
        self.sleep_min = wx.TextCtrl(panel, size=(30, 20))
        self.sleep_min.SetValue(config_player.min_sleep.__str__())
        hbox2.Add(self.sleep_min, proportion=1, flag=wx.LEFT, border=5)
        st2 = wx.StaticText(panel, label='Max: ')
        st2.SetFont(font)
        hbox2.Add(st2, flag=wx.LEFT, border=20)
        self.sleep_max = wx.TextCtrl(panel, size=(30, 20))
        self.sleep_max.SetValue(config_player.max_sleep.__str__())
        hbox2.Add(self.sleep_max, proportion=1, flag=wx.LEFT, border=5)
        #Spirit Check Box
        self.recover_checkbox = wx.CheckBox(panel, label='Spirit')
        self.recover_checkbox.SetFont(font)
        self.recover_checkbox.SetValue(config_player.spirit)
        hbox2.Add(self.recover_checkbox, flag=wx.LEFT, border=30)
        #Insertion of Second Row Box
        vbox.Add(hbox2, flag=wx.LEFT | wx.TOP, border=10)
        #Third Row Box
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        #Skill text
        st3 = wx.StaticText(panel, label='Skills: ')
        st3.SetFont(font)
        hbox3.Add(st3)
        st3 = wx.StaticText(panel, label='Premium: ')
        st3.SetFont(font)
        hbox3.Add(st3, flag=wx.LEFT, border=250)
        vbox.Add(hbox3, flag=wx.LEFT | wx.TOP, border=10)
        #Skill Boxes
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        st = wx.StaticText(panel, label='1: ')
        st.SetFont(font)
        hbox4.Add(st)
        Window2.skill_cb1 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        Window2.skill_cb1.SetEditable(False)
        Window2.skill_cb1.SetSelection(self.get_skill(config_player, 0))
        hbox4.Add(Window2.skill_cb1, flag=wx.LEFT, border=10)

        st = wx.StaticText(panel, label='9: ')
        st.SetFont(font)
        hbox4.Add(st, flag=wx.LEFT, border=20)
        Window2.skill_cb9 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        Window2.skill_cb9.SetEditable(False)
        Window2.skill_cb9.SetSelection(self.get_skill(config_player, 8))
        hbox4.Add(Window2.skill_cb9, flag=wx.LEFT, border=10)

        Window2.premium_cb1 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        Window2.premium_cb1.SetEditable(False)
        Window2.premium_cb1.SetSelection(self.get_premium(config_player, 0))
        hbox4.Add(Window2.premium_cb1, flag=wx.LEFT, border=30)

        #Inserstion of Row Box
        vbox.Add(hbox4, flag=wx.LEFT | wx.TOP, border=10)
        
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        st = wx.StaticText(panel, label='2: ')
        st.SetFont(font)
        hbox5.Add(st)
        Window2.skill_cb2 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        Window2.skill_cb2.SetEditable(False)
        Window2.skill_cb2.SetSelection(self.get_skill(config_player, 1))
        hbox5.Add(Window2.skill_cb2, flag=wx.LEFT, border=10)

        st = wx.StaticText(panel, label='10: ')
        st.SetFont(font)
        hbox5.Add(st, flag=wx.LEFT, border=20)
        Window2.skill_cb10 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        Window2.skill_cb10.SetEditable(False)
        Window2.skill_cb10.SetSelection(self.get_skill(config_player, 9))
        hbox5.Add(Window2.skill_cb10, flag=wx.LEFT, border=2)

        Window2.premium_cb2 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        Window2.premium_cb2.SetEditable(False)
        Window2.premium_cb2.SetSelection(self.get_premium(config_player, 1))
        hbox5.Add(Window2.premium_cb2, flag=wx.LEFT, border=30)

        #Inserstion of Row Box
        vbox.Add(hbox5, flag=wx.LEFT | wx.TOP, border=10)
        
        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        st = wx.StaticText(panel, label='3: ')
        st.SetFont(font)
        hbox6.Add(st)
        Window2.skill_cb3 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        Window2.skill_cb3.SetEditable(False)
        Window2.skill_cb3.SetSelection(self.get_skill(config_player, 2))
        hbox6.Add(Window2.skill_cb3, flag=wx.LEFT, border=10)

        st = wx.StaticText(panel, label='11: ')
        st.SetFont(font)
        hbox6.Add(st, flag=wx.LEFT, border=20)
        Window2.skill_cb11 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        Window2.skill_cb11.SetEditable(False)
        Window2.skill_cb11.SetSelection(self.get_skill(config_player, 10))
        hbox6.Add(Window2.skill_cb11, flag=wx.LEFT, border=2)

        Window2.premium_cb3 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        Window2.premium_cb3.SetEditable(False)
        Window2.premium_cb3.SetSelection(self.get_premium(config_player, 2))
        hbox6.Add(Window2.premium_cb3, flag=wx.LEFT, border=30)

        #Inserstion of Row Box
        vbox.Add(hbox6, flag=wx.LEFT | wx.TOP, border=10)

        hbox7 = wx.BoxSizer(wx.HORIZONTAL)
        st = wx.StaticText(panel, label='4: ')
        st.SetFont(font)
        hbox7.Add(st)
        Window2.skill_cb4 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        Window2.skill_cb4.SetEditable(False)
        Window2.skill_cb4.SetSelection(self.get_skill(config_player, 3))
        hbox7.Add(Window2.skill_cb4, flag=wx.LEFT, border=10)

        st = wx.StaticText(panel, label='12: ')
        st.SetFont(font)
        hbox7.Add(st, flag=wx.LEFT, border=20)
        Window2.skill_cb11 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        Window2.skill_cb11.SetEditable(False)
        Window2.skill_cb11.SetSelection(self.get_skill(config_player, 11))
        hbox7.Add(Window2.skill_cb11, flag=wx.LEFT, border=2)

        Window2.premium_cb4 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        Window2.premium_cb4.SetEditable(False)
        Window2.premium_cb4.SetSelection(self.get_premium(config_player, 3))
        hbox7.Add(Window2.premium_cb4, flag=wx.LEFT, border=30)

        #Inserstion of Row Box
        vbox.Add(hbox7, flag=wx.LEFT | wx.TOP, border=10)

        hbox8 = wx.BoxSizer(wx.HORIZONTAL)
        st = wx.StaticText(panel, label='5: ')
        st.SetFont(font)
        hbox8.Add(st)
        Window2.skill_cb5 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        Window2.skill_cb5.SetEditable(False)
        Window2.skill_cb5.SetSelection(self.get_skill(config_player, 4))
        hbox8.Add(Window2.skill_cb5, flag=wx.LEFT, border=10)

        st = wx.StaticText(panel, label='13: ')
        st.SetFont(font)
        hbox8.Add(st, flag=wx.LEFT, border=20)
        Window2.skill_cb12 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        Window2.skill_cb12.SetEditable(False)
        Window2.skill_cb12.SetSelection(self.get_skill(config_player, 12))
        hbox8.Add(Window2.skill_cb12, flag=wx.LEFT, border=2)
        
        #Inserstion of Row Box
        vbox.Add(hbox8, flag=wx.LEFT | wx.TOP, border=10)
        
        hbox11 = wx.BoxSizer(wx.HORIZONTAL)
        st = wx.StaticText(panel, label='6: ')
        st.SetFont(font)
        hbox11.Add(st)
        Window2.skill_cb6 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        Window2.skill_cb6.SetEditable(False)
        Window2.skill_cb6.SetSelection(self.get_skill(config_player, 5))
        hbox11.Add(Window2.skill_cb6, flag=wx.LEFT, border=10)

        st = wx.StaticText(panel, label='14: ')
        st.SetFont(font)
        hbox11.Add(st, flag=wx.LEFT, border=20)
        Window2.skill_cb13 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        Window2.skill_cb13.SetEditable(False)
        Window2.skill_cb13.SetSelection(self.get_skill(config_player, 13))
        hbox11.Add(Window2.skill_cb13, flag=wx.LEFT, border=2)
        
        #Inserstion of Row Box
        vbox.Add(hbox11, flag=wx.LEFT | wx.TOP, border=10)
        
        hbox12 = wx.BoxSizer(wx.HORIZONTAL)
        st = wx.StaticText(panel, label='7: ')
        st.SetFont(font)
        hbox12.Add(st)
        Window2.skill_cb7 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        Window2.skill_cb7.SetEditable(False)
        Window2.skill_cb7.SetSelection(self.get_skill(config_player, 6))
        hbox12.Add(Window2.skill_cb7, flag=wx.LEFT, border=10)

        st = wx.StaticText(panel, label='15: ')
        st.SetFont(font)
        hbox12.Add(st, flag=wx.LEFT, border=20)
        Window2.skill_cb14 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        Window2.skill_cb14.SetEditable(False)
        Window2.skill_cb14.SetSelection(self.get_skill(config_player, 14))
        hbox12.Add(Window2.skill_cb14, flag=wx.LEFT, border=2)
        
        #Inserstion of Row Box
        vbox.Add(hbox12, flag=wx.LEFT | wx.TOP, border=10)
        
        
        hbox13 = wx.BoxSizer(wx.HORIZONTAL)
        st = wx.StaticText(panel, label='8: ')
        st.SetFont(font)
        hbox13.Add(st)
        Window2.skill_cb8 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        Window2.skill_cb8.SetEditable(False)
        Window2.skill_cb8.SetSelection(self.get_skill(config_player, 7))
        hbox13.Add(Window2.skill_cb8, flag=wx.LEFT, border=10)

        st = wx.StaticText(panel, label='16: ')
        st.SetFont(font)
        hbox13.Add(st, flag=wx.LEFT, border=20)
        Window2.skill_cb15 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        Window2.skill_cb15.SetEditable(False)
        Window2.skill_cb15.SetSelection(self.get_skill(config_player, 15))
        hbox13.Add(Window2.skill_cb15, flag=wx.LEFT, border=2)
        
        #Inserstion of Row Box
        vbox.Add(hbox13, flag=wx.LEFT | wx.TOP, border=10)

        #Last Box
        hbox9 = wx.BoxSizer(wx.HORIZONTAL)
        quick_btn1 = wx.Button(panel, label='Save', size=(180, 30))
        quick_btn1.Bind(wx.EVT_BUTTON, self.save)
        hbox9.Add(quick_btn1, flag=wx.LEFT, border=5)
        #Start Grindfest Button
        btn2 = wx.Button(panel, label='Cancel', size=(180, 30))
        btn2.Bind(wx.EVT_BUTTON, self.cancel)
        hbox9.Add(btn2, flag=wx.LEFT, border=30)
        vbox.Add(hbox9, flag=wx.LEFT | wx.TOP, border=10)

        hbox10 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(panel, label='Help', size=(400, 30))
        btn1.Bind(wx.EVT_BUTTON, self.display_help)
        hbox10.Add(btn1, flag=wx.RIGHT | wx.LEFT, border=5)
        vbox.Add(hbox10, flag=wx.LEFT | wx.TOP, border=5)

        panel.SetSizer(vbox)
        panel.Refresh()

    def save(self):
        print "saving"

    def cancel(self):
        print "closing window"

    def display_help(self):
        print "displaying help"
    def get_skill(self, player, skill):
        try:
            return self.lookup_skill(player.skills[skill])
        except:
            return 0
        
    def get_premium(self, player, premium):
        try:
            return self.lookup_skill(player.premium[premium])
        except:
            return 0
    
    def lookup_skill(self, skill):
        for i in range(0, len(self.skills)):
            if self.skills[i] == skill:
                return i
        return 0