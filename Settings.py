from Players import *
import logging

class Settings:
    full_screen = 0
    Player = Player_1
    box = []
    behavior, style = 0, 0
    #Recover: -1: none, 0:all, 1:health, 2: magic, 3: spirit
    recover = 0
    sleep = 2.5
    log_loc = "Battle.log"
    log_level = logging.DEBUG
    shutdown = False
    skill_buffer = 20
