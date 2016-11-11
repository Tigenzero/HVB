import wx

def factory(aClass, *args):
    return aClass(*args)

def display_message(value):
    dial = wx.MessageDialog(None, value, "Info", wx.OK)
    dial.ShowModal()


def get_help_file(file_loc):
    with open(file_loc, 'r') as f:
        list = f.readlines()
        content = ""
        for line in list:
            content = content + line
        return content