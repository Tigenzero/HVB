import Settings
import logging
import logging.config
import os.path
import UI
import wx
import Players
import datetime


def get_player_config():
    Settings.Player_List = []
    if os.path.isfile("Player.txt"):
        #player_stats = ["", "", "", "", "", ""]
        Players.Player.name = ""
        player_stats = factory(Players.Player)
        player_stats.skills = []
        player_stats.premium = []
        player_config = open(os.getcwd() + "\\" + "Player.txt")
        for line in player_config:
            try:
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
                    player_stats.items = tuple(map(int, clean(line_split[1]).split(",")))
                elif line_split[0] == "special":
                    player_stats.special_attack = map(int, clean(line_split[1]).split(","))
                elif line_split[0] == "premium":
                    for skills in line_split[1].split(","):
                        skills = clean(skills)
                        player_stats.premium.append(skills)
                elif line_split[0] == "skills":
                    #player_stats.skills = line_split[1].rstrip("\n").split(",")
                    for skills in line_split[1].split(","):
                        skills = clean(skills)
                        player_stats.skills.append(skills)
                elif line_split[0] == "spirit":
                    if line_split[1].rstrip("\n") == "True":
                        player_stats.spirit = True
                    else:
                        player_stats.spirit = False
                elif line_split[0] == "min_sleep":
                    player_stats.min_sleep = float(line_split[1].rstrip("\n"))
                elif line_split[0] == "max_sleep":
                    player_stats.max_sleep = float(line_split[1].rstrip("\n"))
            except:
                continue
        if len(player_stats.name) > 0:
            Settings.Player_List.append(player_stats)


def factory(aClass, *args):
    return aClass(*args)


def clean(line):
    line = line.rstrip("\n")
    line = line.strip("[")
    line = line.strip("]")
    line = line.replace(" ", "")
    line = line.replace("'", "")
    return line

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
    logfile = os.path.join('logs', 'logging_file.log')
    print logfile
    if not os.path.isdir('logs'):
        os.makedirs('logs')
    logging.config.fileConfig('logging.conf', defaults={'logfile': logfile})
    #log_path = "{}{}".format( datetime.datetime.today().strftime("%Y%m%d"), Settings.log_loc)
    #logging.basicConfig(filename=log_path, level=Settings.log_level, format='%(asctime)s,%(levelname)s,%(message)s')
    logging.debug("Starting main")
    get_player_config()
    get_arena_values()
    app = wx.App()
    UI.UI(None, title='Grind Buster')
    app.MainLoop()