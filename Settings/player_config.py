__author__ = 'Matt'
import os
import logging
SETTINGS_FILE = os.path.join("data", "Player.txt")


class Player(object):
    def __init__(self):
        self.name = ""
        self.style = None
        self.items = None
        self.skills = []
        self.premium = []
        self.special = []
        self.spirit = None
        self.min_sleep = 0.0
        self.max_sleep = 0.0


class PlayerConfig(object):
    def __init__(self):
        self.player_list = []
        self.player = None

    def get_player_config(self):
        self.player_list = []
        if not os.path.isfile(SETTINGS_FILE):
            raise IOError("Settings File Not Found: {}".format(os.path.join(os.getcwd(), SETTINGS_FILE)))
        self.player = Player()
        player_config = open(SETTINGS_FILE)
        for line in player_config:
            line_split = line.split(":")
            line_split[1] = self._clean(line_split[1])
            if line_split[0] == "name":
                if len(self.player.name) > 0:
                    self._add_player()
                self.player.name = line_split[1]
            elif line_split[0] == "style":
                self.player.style = self._get_style(line_split[1])
            elif line_split[0] == "items":
                self.player.items = self._get_items(line_split[1])
            elif line_split[0] == "special":
                self.player.special = self._get_special(line_split[1])
            elif line_split[0] == "premium":
                self.player.premium = self._get_premium(line_split[1])
            elif line_split[0] == "skills":
                self.player.skills = self._get_skills(line_split[1])
            elif line_split[0] == "spirit":
                self.player.spirit = self._get_spirit(line_split[1])
            elif line_split[0] == "min_sleep":
                self.player.min_sleep = float(line_split[1])
            elif line_split[0] == "max_sleep":
                self.player.max_sleep = float(line_split[1])
        if len(self.player.name) > 0:
            self.player_list.append(self.player)
        delattr(self, "player")

    def _get_skills(self, line):
        return line.split(",")

    def _get_premium(self, line):
        return line.split(',')

    def _get_spirit(self, line):
        if line.lower() == "true":
            return True
        else:
            return False

    def _get_style(self, line):
        return int(line)

    def _get_items(self, line):
        return tuple(map(int, line.split(",")))

    def _get_special(self, line):
        return map(int, line.split(","))

    def _add_player(self):
        logging.info("adding player")
        self.player_list.append(self.player)
        self.player = Player()

    def _clean(self, line):
        #line = line.rstrip("\n")
        line = line.strip()
        line = line.replace(" ", "")
        line = line.replace("'", "")
        line = line.strip("[")
        line = line.strip(']')
        return line

    @classmethod
    def get_player_0(cls):
        player_config = PlayerConfig()
        player_config.get_player_config()
        return player_config.player_list[0]

    @classmethod
    def get_player_1(cls):
        player_config = PlayerConfig()
        player_config.get_player_config()
        return player_config.player_list[1]