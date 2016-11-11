import os
import wx
from util import factory
from Settings import Settings
from player.player_config import PlayerConfig
from user_interface.item_window import ItemWindow
from user_interface.util import get_help_file, display_message
class Window2(wx.Frame):
    skills = ["Empty", "Absorb", "Cure", "Haste", "Heartseeker", "Protection", "Regen", "Shadow_Veil", "Spark_Life",
              "Spirit_Shield", "Special", "Blind", "Weaken", "Sleep", "Drain"]

    def __init__(self, parent, title, combobox):
        super(Window2, self).__init__(parent, title=title, size=(440, 450))
        self.UIComboBox = combobox
        self.InitWindow2()
        self.Centre()
        self.Show(True)

    def InitWindow2(self):

        panel = wx.Panel(self)
        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)
        panel.SetBackgroundColour('#4f5049')
        # get currently selected player
        Window2.config_player = None
        self.current_player = self.UIComboBox.GetValue()
        if self.current_player == "new":
            Window2.config_player = factory(NewPlayer)
            Window2.config_player.skills = []
            Window2.config_player.premium = []
            Window2.config_player.special_attack = []
            Window2.config_player.items = []
        else:
            for player in Settings.Player_List:
                if player.name == self.current_player:
                    Window2.config_player = player
        print self.get_skill(Window2.config_player, 3)
        # Main Box
        vbox = wx.BoxSizer(wx.VERTICAL)
        # First Row Box
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        # Name Box and Input
        st2 = wx.StaticText(panel, label='Name:')
        st2.SetFont(font)
        hbox1.Add(st2)
        self.name = wx.TextCtrl(panel, size=(100, 20))
        self.name.SetValue(Window2.config_player.name.__str__())
        hbox1.Add(self.name, flag=wx.LEFT, border=15)
        # Style Box
        st3 = wx.StaticText(panel, label='Style: ')
        st3.SetFont(font)
        hbox1.Add(st3, flag=wx.LEFT, border=15)
        style_names = ["Dual Wield", "1 Handed", "2 Handed", "Mage", "Niken"]
        self.style_cb = wx.ComboBox(panel, size=(90, 20), name="Style", choices=style_names)
        self.style_cb.SetEditable(False)
        self.style_cb.SetSelection(Window2.config_player.style)
        hbox1.Add(self.style_cb, flag=wx.LEFT, border=10)
        vbox.Add(hbox1, flag=wx.LEFT | wx.TOP, border=10)
        # Second Row Box
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        # Sleep Settings
        st2 = wx.StaticText(panel, label='Sleep Range')
        st2.SetFont(font)
        hbox2.Add(st2, flag=wx.LEFT)
        st2 = wx.StaticText(panel, label='Min:')
        st2.SetFont(font)
        hbox2.Add(st2, flag=wx.LEFT, border=15)
        self.sleep_min = wx.TextCtrl(panel, size=(30, 20))
        self.sleep_min.SetValue(Window2.config_player.min_sleep.__str__())
        hbox2.Add(self.sleep_min, proportion=1, flag=wx.LEFT, border=5)
        st2 = wx.StaticText(panel, label='Max: ')
        st2.SetFont(font)
        hbox2.Add(st2, flag=wx.LEFT, border=20)
        self.sleep_max = wx.TextCtrl(panel, size=(30, 20))
        self.sleep_max.SetValue(Window2.config_player.max_sleep.__str__())
        hbox2.Add(self.sleep_max, proportion=1, flag=wx.LEFT, border=5)
        # Spirit Check Box
        self.spirit_checkbox = wx.CheckBox(panel, label='Spirit')
        self.spirit_checkbox.SetFont(font)
        self.spirit_checkbox.SetValue(Window2.config_player.spirit)
        hbox2.Add(self.spirit_checkbox, flag=wx.LEFT, border=30)
        # Insertion of Second Row Box
        vbox.Add(hbox2, flag=wx.LEFT | wx.TOP, border=10)
        # Third Row Box
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        # Skill text
        st3 = wx.StaticText(panel, label='Skills: ')
        st3.SetFont(font)
        hbox3.Add(st3)
        st3 = wx.StaticText(panel, label='Premium: ')
        st3.SetFont(font)
        hbox3.Add(st3, flag=wx.LEFT, border=250)
        vbox.Add(hbox3, flag=wx.LEFT | wx.TOP, border=10)
        # Skill Boxes
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        st = wx.StaticText(panel, label='1: ')
        st.SetFont(font)
        hbox4.Add(st)
        self.skill_cb1 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        self.skill_cb1.SetEditable(False)
        self.skill_cb1.SetSelection(self.get_skill(Window2.config_player, 0))
        # print "skill received for first skill is {} and player name is {}".format(self.get_skill(Window2.config_player, 0), Window2.config_player.name)
        hbox4.Add(self.skill_cb1, flag=wx.LEFT, border=10)

        st = wx.StaticText(panel, label='9: ')
        st.SetFont(font)
        hbox4.Add(st, flag=wx.LEFT, border=20)
        self.skill_cb9 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        self.skill_cb9.SetEditable(False)
        self.skill_cb9.SetSelection(self.get_skill(Window2.config_player, 8))
        hbox4.Add(self.skill_cb9, flag=wx.LEFT, border=10)

        self.premium_cb1 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        self.premium_cb1.SetEditable(False)
        self.premium_cb1.SetSelection(self.get_premium(Window2.config_player, 0))
        hbox4.Add(self.premium_cb1, flag=wx.LEFT, border=30)

        # Inserstion of Row Box
        vbox.Add(hbox4, flag=wx.LEFT | wx.TOP, border=10)

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        st = wx.StaticText(panel, label='2: ')
        st.SetFont(font)
        hbox5.Add(st)
        self.skill_cb2 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        self.skill_cb2.SetEditable(False)
        self.skill_cb2.SetSelection(self.get_skill(Window2.config_player, 1))
        hbox5.Add(self.skill_cb2, flag=wx.LEFT, border=10)

        st = wx.StaticText(panel, label='10: ')
        st.SetFont(font)
        hbox5.Add(st, flag=wx.LEFT, border=20)
        self.skill_cb10 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        self.skill_cb10.SetEditable(False)
        self.skill_cb10.SetSelection(self.get_skill(Window2.config_player, 9))
        hbox5.Add(self.skill_cb10, flag=wx.LEFT, border=2)

        self.premium_cb2 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        self.premium_cb2.SetEditable(False)
        self.premium_cb2.SetSelection(self.get_premium(Window2.config_player, 1))
        hbox5.Add(self.premium_cb2, flag=wx.LEFT, border=30)

        # Inserstion of Row Box
        vbox.Add(hbox5, flag=wx.LEFT | wx.TOP, border=10)

        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        st = wx.StaticText(panel, label='3: ')
        st.SetFont(font)
        hbox6.Add(st)
        self.skill_cb3 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        self.skill_cb3.SetEditable(False)
        self.skill_cb3.SetSelection(self.get_skill(Window2.config_player, 2))
        hbox6.Add(self.skill_cb3, flag=wx.LEFT, border=10)

        st = wx.StaticText(panel, label='11: ')
        st.SetFont(font)
        hbox6.Add(st, flag=wx.LEFT, border=20)
        self.skill_cb11 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        self.skill_cb11.SetEditable(False)
        self.skill_cb11.SetSelection(self.get_skill(Window2.config_player, 10))
        hbox6.Add(self.skill_cb11, flag=wx.LEFT, border=2)

        self.premium_cb3 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        self.premium_cb3.SetEditable(False)
        self.premium_cb3.SetSelection(self.get_premium(Window2.config_player, 2))
        hbox6.Add(self.premium_cb3, flag=wx.LEFT, border=30)

        # Inserstion of Row Box
        vbox.Add(hbox6, flag=wx.LEFT | wx.TOP, border=10)

        hbox7 = wx.BoxSizer(wx.HORIZONTAL)
        st = wx.StaticText(panel, label='4: ')
        st.SetFont(font)
        hbox7.Add(st)
        self.skill_cb4 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        self.skill_cb4.SetEditable(False)
        self.skill_cb4.SetSelection(self.get_skill(Window2.config_player, 3))
        hbox7.Add(self.skill_cb4, flag=wx.LEFT, border=10)

        st = wx.StaticText(panel, label='12: ')
        st.SetFont(font)
        hbox7.Add(st, flag=wx.LEFT, border=20)
        self.skill_cb12 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        self.skill_cb12.SetEditable(False)
        self.skill_cb12.SetSelection(self.get_skill(Window2.config_player, 11))
        hbox7.Add(self.skill_cb12, flag=wx.LEFT, border=2)

        self.premium_cb4 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        self.premium_cb4.SetEditable(False)
        self.premium_cb4.SetSelection(self.get_premium(Window2.config_player, 3))
        hbox7.Add(self.premium_cb4, flag=wx.LEFT, border=30)

        # Inserstion of Row Box
        vbox.Add(hbox7, flag=wx.LEFT | wx.TOP, border=10)

        hbox8 = wx.BoxSizer(wx.HORIZONTAL)
        st = wx.StaticText(panel, label='5: ')
        st.SetFont(font)
        hbox8.Add(st)
        self.skill_cb5 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        self.skill_cb5.SetEditable(False)
        self.skill_cb5.SetSelection(self.get_skill(Window2.config_player, 4))
        hbox8.Add(self.skill_cb5, flag=wx.LEFT, border=10)

        st = wx.StaticText(panel, label='13: ')
        st.SetFont(font)
        hbox8.Add(st, flag=wx.LEFT, border=20)
        self.skill_cb13 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        self.skill_cb13.SetEditable(False)
        self.skill_cb13.SetSelection(self.get_skill(Window2.config_player, 12))
        hbox8.Add(self.skill_cb13, flag=wx.LEFT, border=2)

        item_btn = wx.Button(panel, label='Items', size=(100, 20))
        item_btn.Bind(wx.EVT_BUTTON, self.set_items)
        hbox8.Add(item_btn, flag=wx.LEFT, border=30)

        # Inserstion of Row Box
        vbox.Add(hbox8, flag=wx.LEFT | wx.TOP, border=10)

        hbox11 = wx.BoxSizer(wx.HORIZONTAL)
        st = wx.StaticText(panel, label='6: ')
        st.SetFont(font)
        hbox11.Add(st)
        self.skill_cb6 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        self.skill_cb6.SetEditable(False)
        self.skill_cb6.SetSelection(self.get_skill(Window2.config_player, 5))
        hbox11.Add(self.skill_cb6, flag=wx.LEFT, border=10)

        st = wx.StaticText(panel, label='14: ')
        st.SetFont(font)
        hbox11.Add(st, flag=wx.LEFT, border=20)
        self.skill_cb14 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        self.skill_cb14.SetEditable(False)
        self.skill_cb14.SetSelection(self.get_skill(Window2.config_player, 13))
        hbox11.Add(self.skill_cb14, flag=wx.LEFT, border=2)

        # Inserstion of Row Box
        vbox.Add(hbox11, flag=wx.LEFT | wx.TOP, border=10)

        hbox12 = wx.BoxSizer(wx.HORIZONTAL)
        st = wx.StaticText(panel, label='7: ')
        st.SetFont(font)
        hbox12.Add(st)
        self.skill_cb7 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        self.skill_cb7.SetEditable(False)
        self.skill_cb7.SetSelection(self.get_skill(Window2.config_player, 6))
        hbox12.Add(self.skill_cb7, flag=wx.LEFT, border=10)

        st = wx.StaticText(panel, label='15: ')
        st.SetFont(font)
        hbox12.Add(st, flag=wx.LEFT, border=20)
        self.skill_cb15 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        self.skill_cb15.SetEditable(False)
        self.skill_cb15.SetSelection(self.get_skill(Window2.config_player, 14))
        hbox12.Add(self.skill_cb15, flag=wx.LEFT, border=2)

        # Inserstion of Row Box
        vbox.Add(hbox12, flag=wx.LEFT | wx.TOP, border=10)

        hbox13 = wx.BoxSizer(wx.HORIZONTAL)
        st = wx.StaticText(panel, label='8: ')
        st.SetFont(font)
        hbox13.Add(st)
        self.skill_cb8 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        self.skill_cb8.SetEditable(False)
        self.skill_cb8.SetSelection(self.get_skill(Window2.config_player, 7))
        hbox13.Add(self.skill_cb8, flag=wx.LEFT, border=10)

        st = wx.StaticText(panel, label='16: ')
        st.SetFont(font)
        hbox13.Add(st, flag=wx.LEFT, border=20)
        self.skill_cb16 = wx.ComboBox(panel, size=(100, 20), choices=self.skills)
        self.skill_cb16.SetEditable(False)
        self.skill_cb16.SetSelection(self.get_skill(Window2.config_player, 15))
        hbox13.Add(self.skill_cb16, flag=wx.LEFT, border=2)

        # Inserstion of Row Box
        vbox.Add(hbox13, flag=wx.LEFT | wx.TOP, border=10)

        # Last Box
        hbox9 = wx.BoxSizer(wx.HORIZONTAL)
        quick_btn1 = wx.Button(panel, label='Save', size=(180, 30))
        quick_btn1.Bind(wx.EVT_BUTTON, self.save)
        hbox9.Add(quick_btn1, flag=wx.LEFT, border=5)
        # Start Grindfest Button
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

    def set_items(self, event):
        ItemWindow(wx.GetApp().TopWindow, title="Item Config", config_player=Window2.config_player).Show()

    def save(self, event):
        # TODO: refactor and put in separate method
        print "saving"
        print "looking for {}".format(self.current_player)
        fpath = 'Player.txt'
        if os.path.isfile("Player.txt"):
            print('File Found! Looking for Player')
            with open(fpath, 'r+') as f:
                lines = f.readlines()
                f.seek(0)
                f.truncate()
                name_found = False
                for line in lines:
                    line_split = line.split(':')
                    if (line_split[0] == "name" and line_split[1].rstrip("\n") == self.current_player) or name_found:
                        name_found = True
                        if line_split[0] == "name":
                            line = "name:{}{}".format(self.name.GetValue(), "\n")
                        elif line_split[0] == "style":
                            line = "style:{}{}".format(self.get_player_style(), "\n")
                        elif line_split[0] == "items":
                            line = "items:{}{}".format(self.get_converted_items(), "\n")
                        elif line_split[0] == "special":
                            line = "special:{}{}".format(self.get_player_special(), "\n")
                        elif line_split[0] == "premium":
                            line = "premium:{}{}".format(self.get_player_premium(), "\n")
                        elif line_split[0] == "skills":
                            line = "skills:{}{}".format(self.get_player_skills(), "\n")
                        elif line_split[0] == "spirit":
                            line = "spirit:{}{}".format(self.spirit_checkbox.GetValue(), "\n")
                        elif line_split[0] == "min_sleep":
                            line = "min_sleep:{}{}".format(self.sleep_min.GetValue(), "\n")
                        elif line_split[0] == "max_sleep":
                            line = "max_sleep:{}{}".format(self.sleep_max.GetValue(), "\n")

                    f.write(line)
                if not name_found:
                    print "name not found, creating new player"
                    line = "name:{}".format(self.name.GetValue())
                    f.write(line + "\n")
                    line = "style:{}".format(self.get_player_style())
                    f.write(line + "\n")
                    line = "items:{}".format(Window2.config_player.items)
                    f.write(line + "\n")
                    line = "special:{}".format(self.get_player_special())
                    f.write(line + "\n")
                    line = "premium:{}".format(self.get_player_premium())
                    f.write(line + "\n")
                    line = "skills:{}".format(self.get_player_skills())
                    f.write(line + "\n")
                    line = "spirit:{}".format(self.spirit_checkbox.GetValue())
                    f.write(line + "\n")
                    line = "min_sleep:{}".format(self.sleep_min.GetValue())
                    f.write(line + "\n")
                    line = "max_sleep:{}".format(self.sleep_max.GetValue())
                    f.write(line)

        else:
            with open(fpath, 'wb') as f:
                print "file not found!"
                line = "name:{}".format(self.name.GetValue())
                f.write("%s\n" % line)
                line = "style:{}".format(self.get_player_style())
                f.write("%s\n" % line)
                line = "items:{}".format(Window2.config_player.items)
                f.write("%s\n" % line)
                line = "special:{}".format(self.get_player_special())
                f.write("%s\n" % line)
                line = "premium:{}".format(self.get_player_premium())
                f.write("%s\n" % line)
                line = "skills:{}".format(self.get_player_skills())
                f.write("%s\n" % line)
                line = "spirit:{}".format(self.spirit_checkbox.GetValue())
                f.write("%s\n" % line)
                line = "min_sleep:{}".format(self.sleep_min.GetValue())
                f.write("%s\n" % line)
                line = "max_sleep:{}".format(self.sleep_max.GetValue())
                f.write("%s\n" % line)
        config = PlayerConfig()
        config.get_player_config()
        Settings.Player_List = config.player_list
        # TODO: Test if this works
        self.UIComboBox.Clear()
        if len(Settings.Player_List) > 0:
            for player in Settings.Player_List:
                self.UIComboBox.Append(player.name)
        self.UIComboBox.Append("new")
        self.UIComboBox.SetSelection(0)

        self.Destroy()

    def cancel(self, event):
        self.Destroy()

    def close_window(self):
        self.Destroy()

    def display_help(self, event):
        help_doc = get_help_file("configure_help.txt")
        display_message(help_doc)

    def get_skill(self, player, skill):
        try:
            return self.lookup_skill(player.skills[skill])
        except:
            return 0

    def get_converted_items(self):
        tuple_list = Window2.config_player.items
        item_list = []
        for item in tuple_list:
            item_list.append(item)
        return item_list

    def get_player_style(self):
        style_names = ["Dual Wield", "1 Handed", "2 Handed", "Mage", "Niken"]
        style = self.style_cb.GetValue()
        for i in range(0, len(style_names)):
            if style == style_names[i]:
                return i

    def get_player_skills(self):
        return [self.skill_cb1.GetValue().encode('utf-8'), self.skill_cb2.GetValue().encode('utf-8'),
                self.skill_cb3.GetValue().encode('utf-8'), self.skill_cb4.GetValue().encode('utf-8'),
                self.skill_cb5.GetValue().encode('utf-8'), self.skill_cb6.GetValue().encode('utf-8'),
                self.skill_cb7.GetValue().encode('utf-8'), self.skill_cb8.GetValue().encode('utf-8'),
                self.skill_cb9.GetValue().encode('utf-8'), self.skill_cb10.GetValue().encode('utf-8'),
                self.skill_cb11.GetValue().encode('utf-8'), self.skill_cb12.GetValue().encode('utf-8'),
                self.skill_cb13.GetValue().encode('utf-8'), self.skill_cb14.GetValue().encode('utf-8'),
                self.skill_cb15.GetValue().encode('utf-8'), self.skill_cb16.GetValue().encode('utf-8')]

    def get_player_special(self):
        skills = self.get_player_skills()
        special = []
        for i in range(0, len(skills) - 1):
            if skills[i] == "Special":
                special.append(i)
        return special

    def get_player_premium(self):
        return [self.premium_cb1.GetValue().encode('utf-8'), self.premium_cb2.GetValue().encode('utf-8'),
                self.premium_cb3.GetValue().encode('utf-8'), self.premium_cb4.GetValue().encode('utf-8')]

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


class NewPlayer:
    name = ""
    style = 0
    spirit = False
    # 0 = Health, 1 = Mana, 2 = Spirit, 9 = used
    items = () #main character
    special_attack = []
    premium = []
    skills = []
    auto_cast = ["Spark_Life", "Absorb"]
    min_sleep = 0.5
    max_sleep = 2.5