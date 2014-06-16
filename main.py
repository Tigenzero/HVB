import Settings
import logging
import os.path

def get_player_config():
    if os.path.isfile("Player.txt"):
        player_stats = ["", "", "", "", "", ""]
        player_config = open(os.getcwd() + "\\" + "Player.txt")
        for line in player_config:
            line_split = line.split(":")
            if line_split[0] == "name":
                if len(player_stats[0]) > 0:
                    Settings.Player_List.append(player_stats)
                    player_stats = ["", "", "", "", "", ""]
                    player_stats[0] = line_split[1].rstrip("\n")
                else:
                    player_stats[0] = line_split[1].rstrip("\n")
            elif line_split[0] == "style":
                player_stats[1] = line_split[1].rstrip("\n")
            elif line_split[0] == "items":
                player_stats[2] = line_split[1].rstrip("\n")
            elif line_split[0] == "special":
                player_stats[3] = line_split[1].rstrip("\n")
            elif line_split[0] == "premium":
                player_stats[4] = line_split[1].rstrip("\n")
            elif line_split[0] == "skills":
                player_stats[5] = line_split[1].rstrip("\n")
        if len(player_stats[0]) > 0:
            Settings.Player_List.append(player_stats)

if __name__ == '__main__':
    logging.debug("Starting main")
    get_player_config()