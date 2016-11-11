import wx
import os
import logging


class ItemWindow(wx.Frame):
    items = ["Health Potion", "Magic Potion", "Spirit Potion", "Empty"]

    def __init__(self, parent, title, config_player):
            super(ItemWindow, self).__init__(parent, title=title, size=(325, 350))
            self.config_player = config_player
            self.init_item_window()
            self.Centre()
            self.Show(True)

    def init_item_window(self):
        """Creates the Item Window and puts all necessary pieces inside of it before showing.
        :return: None
        """
        # create item box Panel
        ItemWindow.item_list = []
        panel = wx.Panel(self)
        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)
        panel.SetBackgroundColour('#4f5049')
        # config_player = Window2.config_player
        print self.config_player.name
        # create vertical box to hold all horizontal boxes
        vbox = wx.BoxSizer(wx.VERTICAL)
        # creates first row horizontal box, holds text
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        #Skill text
        st3 = wx.StaticText(panel, label='Items: ')
        st3.SetFont(font)
        hbox3.Add(st3)
        vbox.Add(hbox3, flag=wx.LEFT | wx.TOP, border=10)
        #Skill Boxes
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        st = wx.StaticText(panel, label='1: ')
        st.SetFont(font)
        hbox4.Add(st)
        self.skill_cb1 = wx.ComboBox(panel, size=(100, 20), choices=self.items)
        self.skill_cb1.SetEditable(False)
        self.skill_cb1.SetSelection(self.get_item(self.config_player, 0))
        #print "skill received for first skill is {} and player name is {}".format(self.get_item(self.config_player, 0), self.config_player.name)
        hbox4.Add(self.skill_cb1, flag=wx.LEFT, border=10)

        st = wx.StaticText(panel, label='9: ')
        st.SetFont(font)
        hbox4.Add(st, flag=wx.LEFT, border=20)
        self.skill_cb9 = wx.ComboBox(panel, size=(100, 20), choices=self.items)
        self.skill_cb9.SetEditable(False)
        self.skill_cb9.SetSelection(self.get_item(self.config_player, 8))
        hbox4.Add(self.skill_cb9, flag=wx.LEFT, border=10)

        #Inserstion of Row Box
        vbox.Add(hbox4, flag=wx.LEFT | wx.TOP, border=10)

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        st = wx.StaticText(panel, label='2: ')
        st.SetFont(font)
        hbox5.Add(st)
        self.skill_cb2 = wx.ComboBox(panel, size=(100, 20), choices=self.items)
        self.skill_cb2.SetEditable(False)
        self.skill_cb2.SetSelection(self.get_item(self.config_player, 1))
        hbox5.Add(self.skill_cb2, flag=wx.LEFT, border=10)

        st = wx.StaticText(panel, label='10: ')
        st.SetFont(font)
        hbox5.Add(st, flag=wx.LEFT, border=20)
        self.skill_cb10 = wx.ComboBox(panel, size=(100, 20), choices=self.items)
        self.skill_cb10.SetEditable(False)
        self.skill_cb10.SetSelection(self.get_item(self.config_player, 9))
        hbox5.Add(self.skill_cb10, flag=wx.LEFT, border=2)


        #Inserstion of Row Box
        vbox.Add(hbox5, flag=wx.LEFT | wx.TOP, border=10)

        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        st = wx.StaticText(panel, label='3: ')
        st.SetFont(font)
        hbox6.Add(st)
        self.skill_cb3 = wx.ComboBox(panel, size=(100, 20), choices=self.items)
        self.skill_cb3.SetEditable(False)
        self.skill_cb3.SetSelection(self.get_item(self.config_player, 2))
        hbox6.Add(self.skill_cb3, flag=wx.LEFT, border=10)

        st = wx.StaticText(panel, label='11: ')
        st.SetFont(font)
        hbox6.Add(st, flag=wx.LEFT, border=20)
        self.skill_cb11 = wx.ComboBox(panel, size=(100, 20), choices=self.items)
        self.skill_cb11.SetEditable(False)
        self.skill_cb11.SetSelection(self.get_item(self.config_player, 10))
        hbox6.Add(self.skill_cb11, flag=wx.LEFT, border=2)


        #Inserstion of Row Box
        vbox.Add(hbox6, flag=wx.LEFT | wx.TOP, border=10)

        hbox7 = wx.BoxSizer(wx.HORIZONTAL)
        st = wx.StaticText(panel, label='4: ')
        st.SetFont(font)
        hbox7.Add(st)
        self.skill_cb4 = wx.ComboBox(panel, size=(100, 20), choices=self.items)
        self.skill_cb4.SetEditable(False)
        self.skill_cb4.SetSelection(self.get_item(self.config_player, 3))
        hbox7.Add(self.skill_cb4, flag=wx.LEFT, border=10)

        st = wx.StaticText(panel, label='12: ')
        st.SetFont(font)
        hbox7.Add(st, flag=wx.LEFT, border=20)
        self.skill_cb12 = wx.ComboBox(panel, size=(100, 20), choices=self.items)
        self.skill_cb12.SetEditable(False)
        self.skill_cb12.SetSelection(self.get_item(self.config_player, 11))
        hbox7.Add(self.skill_cb12, flag=wx.LEFT, border=2)


        #Inserstion of Row Box
        vbox.Add(hbox7, flag=wx.LEFT | wx.TOP, border=10)

        hbox8 = wx.BoxSizer(wx.HORIZONTAL)
        st = wx.StaticText(panel, label='5: ')
        st.SetFont(font)
        hbox8.Add(st)
        self.skill_cb5 = wx.ComboBox(panel, size=(100, 20), choices=self.items)
        self.skill_cb5.SetEditable(False)
        self.skill_cb5.SetSelection(self.get_item(self.config_player, 4))
        hbox8.Add(self.skill_cb5, flag=wx.LEFT, border=10)

        st = wx.StaticText(panel, label='13: ')
        st.SetFont(font)
        hbox8.Add(st, flag=wx.LEFT, border=20)
        self.skill_cb13 = wx.ComboBox(panel, size=(100, 20), choices=self.items)
        self.skill_cb13.SetEditable(False)
        self.skill_cb13.SetSelection(self.get_item(self.config_player, 12))
        hbox8.Add(self.skill_cb13, flag=wx.LEFT, border=2)

        #Inserstion of Row Box
        vbox.Add(hbox8, flag=wx.LEFT | wx.TOP, border=10)

        hbox11 = wx.BoxSizer(wx.HORIZONTAL)
        st = wx.StaticText(panel, label='6: ')
        st.SetFont(font)
        hbox11.Add(st)
        self.skill_cb6 = wx.ComboBox(panel, size=(100, 20), choices=self.items)
        self.skill_cb6.SetEditable(False)
        self.skill_cb6.SetSelection(self.get_item(self.config_player, 5))
        hbox11.Add(self.skill_cb6, flag=wx.LEFT, border=10)

        st = wx.StaticText(panel, label='14: ')
        st.SetFont(font)
        hbox11.Add(st, flag=wx.LEFT, border=20)
        self.skill_cb14 = wx.ComboBox(panel, size=(100, 20), choices=self.items)
        self.skill_cb14.SetEditable(False)
        self.skill_cb14.SetSelection(self.get_item(self.config_player, 13))
        hbox11.Add(self.skill_cb14, flag=wx.LEFT, border=2)

        #Inserstion of Row Box
        vbox.Add(hbox11, flag=wx.LEFT | wx.TOP, border=10)

        hbox12 = wx.BoxSizer(wx.HORIZONTAL)
        st = wx.StaticText(panel, label='7: ')
        st.SetFont(font)
        hbox12.Add(st)
        self.skill_cb7 = self.create_item_combobox(6)
        hbox12.Add(self.skill_cb7, flag=wx.LEFT, border=10)

        st = wx.StaticText(panel, label='15: ')
        st.SetFont(font)
        hbox12.Add(st, flag=wx.LEFT, border=20)
        self.skill_cb15 = wx.ComboBox(panel, size=(100, 20), choices=self.items)
        self.skill_cb15.SetEditable(False)
        self.skill_cb15.SetSelection(self.get_item(self.config_player, 14))
        hbox12.Add(self.skill_cb15, flag=wx.LEFT, border=2)

        #Inserstion of Row Box
        vbox.Add(hbox12, flag=wx.LEFT | wx.TOP, border=10)


        hbox13 = wx.BoxSizer(wx.HORIZONTAL)
        st = wx.StaticText(panel, label='8: ')
        st.SetFont(font)
        hbox13.Add(st)
        self.skill_cb8 = wx.ComboBox(panel, size=(100, 20), choices=self.items)
        self.skill_cb8.SetEditable(False)
        self.skill_cb8.SetSelection(self.get_item(self.config_player, 7))
        hbox13.Add(self.skill_cb8, flag=wx.LEFT, border=10)

        st = wx.StaticText(panel, label='16: ')
        st.SetFont(font)
        hbox13.Add(st, flag=wx.LEFT, border=20)
        self.skill_cb16 = wx.ComboBox(panel, size=(100, 20), choices=self.items)
        self.skill_cb16.SetEditable(False)
        self.skill_cb16.SetSelection(self.get_item(self.config_player, 15))
        hbox13.Add(self.skill_cb16, flag=wx.LEFT, border=2)
        #Inserstion of Row Box
        vbox.Add(hbox13, flag=wx.LEFT | wx.TOP, border=10)
        hbox9 = wx.BoxSizer(wx.HORIZONTAL)
        quick_btn1 = wx.Button(panel, label='Save', size=(132, 30))
        quick_btn1.Bind(wx.EVT_BUTTON, self.save)
        hbox9.Add(quick_btn1, flag=wx.LEFT, border=5)
        btn2 = wx.Button(panel, label='Cancel', size=(132, 30))
        btn2.Bind(wx.EVT_BUTTON, self.cancel)
        hbox9.Add(btn2, flag=wx.LEFT, border=10)
        vbox.Add(hbox9, flag=wx.LEFT | wx.TOP, border=10)
        panel.SetSizer(vbox)
        panel.Refresh()

    def create_item_combobox(self, item_num):
        """creates an item combobox and returns the combobox object
        :param item_num: number of item to be represented in the combobox
        :return: combobox object
        """
        combobox = wx.ComboBox(panel, size=(100, 20), choices=self.items)
        self.skill_cb7.SetEditable(False)
        self.skill_cb7.SetSelection(self.get_item(self.config_player, item_num))


    def get_item(self, player, pos):
        try:
            item = player.items[pos]
            if item < 9:
                return item
            else:
                return 3
        except:
            return 3

    #TODO: Save no longer works. Fix.
    def save(self, event):
        items = self.get_player_items()
        item_list = []
        for item in items:
            if item == "Health Potion":
                item_list.append(0)
            elif item == "Magic Potion":
                item_list.append(1)
            elif item == "Spirit Potion":
                item_list.append(2)
            else:
                item_list.append(9)
        self.config_player.items = item_list
        self.Destroy()

    def cancel(self, event):
        self.Destroy()

    def get_player_items(self):
        return [self.skill_cb1.GetValue().encode('utf-8'), self.skill_cb2.GetValue().encode('utf-8'),
                self.skill_cb3.GetValue().encode('utf-8'), self.skill_cb4.GetValue().encode('utf-8'),
                self.skill_cb5.GetValue().encode('utf-8'), self.skill_cb6.GetValue().encode('utf-8'),
                self.skill_cb7.GetValue().encode('utf-8'), self.skill_cb8.GetValue().encode('utf-8'),
                self.skill_cb9.GetValue().encode('utf-8'), self.skill_cb10.GetValue().encode('utf-8'),
                self.skill_cb11.GetValue().encode('utf-8'), self.skill_cb12.GetValue().encode('utf-8'),
                self.skill_cb13.GetValue().encode('utf-8'), self.skill_cb14.GetValue().encode('utf-8'),
                self.skill_cb15.GetValue().encode('utf-8'), self.skill_cb16.GetValue().encode('utf-8')]
