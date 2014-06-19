import Settings
import logging
import os.path
import UI
import wx
import Players

def get_player_config():
    if os.path.isfile("Player.txt"):
        #player_stats = ["", "", "", "", "", ""]
        player_stats = factory(Players.Player)
        player_config = open(os.getcwd() + "\\" + "Player.txt")
        for line in player_config:
            line_split = line.split(":")
            if line_split[0] == "name":
                if len(player_stats.name) > 0:
                    Settings.Player_List.append(player_stats)
                    player_stats = Players.Player
                    player_stats.name = line_split[1].rstrip("\n")
                else:
                    player_stats.name = line_split[1].rstrip("\n")
            elif line_split[0] == "style":
                player_stats.style = int(line_split[1].rstrip("\n"))
            elif line_split[0] == "items":
                player_stats.items = tuple(map(int, line_split[1].rstrip("\n").split(",")))
            elif line_split[0] == "special":
                player_stats.special_attack = map(int, line_split[1].rstrip("\n").split(","))
            elif line_split[0] == "premium":
                player_stats.premium = line_split[1].rstrip("\n").split(",")
            elif line_split[0] == "skills":
                player_stats.skills = line_split[1].rstrip("\n").split(",")
        if len(player_stats.name) > 0:
            Settings.Player_List.append(player_stats)


def factory(aClass, *args):
    return aClass(*args)


def get_arena_values():
    if os.path.isfile("Arenas.txt"):
        Arena_File = open(os.getcwd() + "\\" + "Arenas.txt")
        for line in Arena_File:
            Settings.Arenas.append(line.rstrip("\n"))
    else:
        logging.critical("Arena File Could not be Found")
        dial = wx.MessageDialog(None, "Critical Error: Arena File could not be found. Please Contact Support.", "Info", wx.OK)
        dial.ShowModal()

if __name__ == '__main__':
    logging.basicConfig(filename=Settings.log_loc, level=Settings.log_level, format='%(asctime)s %(levelname)s: %(message)s')
    logging.debug("Starting main")
    get_player_config()
    get_arena_values()
    app = wx.App()
    UI.UI(None, title='Grind Buster')
    app.MainLoop()