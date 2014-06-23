import logging
full_screen = 0
Player = None
box = []
behavior, style = 0, 0
#Recover: -1: none, 0:all, 1:health, 2: magic, 3: spirit
recover = True
min_sleep = 0.5
max_sleep = 2.5
log_loc = "Battle.log"
log_level = logging.DEBUG
shutdown = False
skill_buffer = 20
Player_List = []
Arenas = []
pause = False
pony_timer = 0
