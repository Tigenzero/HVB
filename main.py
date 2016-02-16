import logging
import logging.config
import os.path
import wx
from Settings import Settings
from user_interface import UI
from player.player_config import PlayerConfig


def get_arena_values():
    if os.path.isfile("Arenas.txt"):
        arena_file = open("Arenas.txt")
        for line in arena_file:
            Settings.Arenas.append(line.rstrip("\n"))
    else:
        logging.critical("arena file Could not be Found")
        dial = wx.MessageDialog(None, "Critical Error: arena file could not be found. Please Contact Support.", "Info", wx.OK)
        dial.ShowModal()

if __name__ == '__main__':
    logfile = os.path.join('logs', 'logging_file.log')
    print logfile
    if not os.path.isdir('logs'):
        os.makedirs('logs')
    logging.config.fileConfig('logging.conf', defaults={'logfile': logfile})
    logging.debug("Starting main")
    player_config = PlayerConfig()
    player_config.get_player_config()
    Settings.Player_List = player_config.player_list

    get_arena_values()
    app = wx.App()
    UI.UI(None, title='Grind Buster')
    app.MainLoop()