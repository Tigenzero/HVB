"""
For Screen Resolution 1920 X 1080
"""
import ImageGrab
import winsound
from numpy import *
from find_window import find_corner
import logging
import logging.config
import os
from Items import get_gem, use_health_pot, use_mana_pot, use_spirit_pot, get_items, use_gem, leftover_inventory
from Skills import activate_cure, activate_premium, activate_protection, activate_regen, special_attack, get_spirit, get_overcharge
from Click_Press import *
from Cooldown import *
from Coordinates import Cord
from Settings import Settings
from Status import get_status


def debug_levels(current_level, level):
    #Performs all of the needed functions during a round
    if current_level == 10:
        screenGrab_save(level + '_10', level)
    elif current_level == 20:
        screenGrab_save(level + '_20', level)
    elif current_level == 30:
        screenGrab_save(level + '_30', level)
    elif current_level == 40:
        screenGrab_save(level + '_40', level)
    elif current_level == 50:
        screenGrab_save(level + '_50', level)
    elif current_level == 60:
        screenGrab_save(level + '_60', level)
    elif current_level == 70:
        screenGrab_save(level + '_70', level)
    elif current_level == 80:
        screenGrab_save(level + '_80', level)
    elif current_level == 90:
        screenGrab_save(level + '_90', level)
    elif current_level == 100:
        screenGrab_save(level + '_100', level)

def enemies_exist(im):
    for enemy in Cord.enemies:
        if im.getpixel(enemy) == Cord.over_color or im.getpixel(enemy) == Cord.under_color:
            return True
    return False


def get_boundaries():
        corner = find_corner()
        Settings.box = (corner[0], corner[1], corner[0] + 1235, corner[1] + 701)
        Cord.window_padding_y = corner[1]
        Cord.window_padding_x = corner[0]


def get_cords():
    x, y = win32api.GetCursorPos()
    print x, y


#Pulls the current alive Enemies and places them in the current_enemy list
def get_enemies(im):
    current_enemies = []
    #enemy_num = 0
    for enemy in Cord.enemies:
        #enemy_num = enemy_num + 1
        if im.getpixel(enemy) == Cord.over_color or im.getpixel(enemy) == Cord.under_color:
            #return enemy
            current_enemies.append(enemy)
            #print "enemy %d is alive " % enemy_num
    return current_enemies


def get_health(im):
    p_health = 0
    for level in Cord.p_health_levels:
        if im.getpixel(level) != Cord.under_color:
            p_health += 10
        else:
            return p_health
    return 100


def get_mana(im):
    p_mana = 0
    for level in Cord.p_mana_levels:
        if im.getpixel(level) != Cord.under_color:
            p_mana += 10
        else:
            return p_mana
    return 100


def go_to_arena(level, point):
    mousePos(Cord.battle_cat_loc)
    time.sleep(0.5)
    mousePos(Cord.arena_cat_loc)
    leftClick()
    time.sleep(1)
    if point == 1:
        mousePos(Cord.a_next_loc)
        leftClick()
        time.sleep(1)
    mousePos(level)
    leftClick()
    time.sleep(1)
    #mousePos(Cord.a_window_ok_loc)
    #time.sleep(0.5)
    #leftClick()
    press("enter")
    time.sleep(1)


def go_to_grindfest():
    mousePos(Cord.battle_cat_loc)
    time.sleep(0.5)
    mousePos(Cord.Grindfest_cat_loc)
    leftClick()
    time.sleep(0.5)
    mousePos(Cord.grindfest_button)
    leftClick()


def is_channeling_active():
    for status in Cord.Current_Status:
        if status == "channeling":
            return True
    return False


def is_player_dead(im):
    if get_health(im) == 0:
        return True
    else:
        return False


def pony_time(im):
    if im.getpixel(Cord.Pony_check_loc[0]) != Cord.Pony_check_color and len(get_enemies(im)) == 0:
        time.sleep(0.5)
        get_boundaries()
        im = screenGrab()
        for pony in Cord.Pony_check_loc:
            if im.getpixel(pony) != Cord.Pony_check_color and len(get_enemies(im)) == 0:
                continue
            else:
                return False
        while im.getpixel(Cord.Pony_check_loc[0]) != Cord.Pony_check_color and len(get_enemies(im)) == 0:
            logging.info("Pony Time!")
            freq = 2500 # Set Frequency To 2500 Hertz
            dur = 1000 # Set Duration To 1000 ms == 1 second
            winsound.Beep(freq, dur)
            time.sleep(4)
            im = screenGrab()
        return True
    return False


def recover():
    if Settings.recover >= 0:
        mousePos(Cord.restoratives_button)
        leftClick()
        if Settings.recover == 0:
            mousePos(Cord.restore_all_button)
        elif Settings.recover == 1:
            mousePos(Cord.restore_health_button)
        elif Settings.recover == 2:
            mousePos(Cord.restore_mana_button)
        elif Settings.recover == 3:
            mousePos(Cord.restore_spirit_button)
        leftClick()
        sleep()
        return True
    return False


#Determines if round has been won or not
def round_won():
    im = screenGrab()
    #if im.getpixels(Cord.round_won) == Cord.round_won_color:
     #   return True
    if enemies_exist(im) == False:
        return True
    else:
        return False


def restore_stats(im):
        current_health = get_health(im)
        current_spirit = get_spirit(im)
        current_mana = get_mana(im)
        if current_health == 0 and not enemies_exist(im):
            time.sleep(1)
            if current_health == 0 and not enemies_exist(screenGrab()):
                Cord.p_dead = True
                logging.info("Player has died")
            else:
                return False
        elif use_gem(0, current_health):
            logging.info("Health Gem Used")
        elif activate_cure(current_health, current_mana):
            logging.info("Cure Casted")
        elif use_health_pot(current_health):
            logging.info("Health Potion used")
        elif use_gem(1, current_mana):
            logging.info("Mana Gem Used")
        elif use_mana_pot(current_mana):
            logging.info("Mana Potion used")
        elif use_gem(1, current_spirit):
            logging.info("Spirit Gem Used")
        elif use_spirit_pot(current_spirit):
            logging.info("Spirit Potion used")
        elif activate_regen(current_health):
            logging.info("Regen Casted")
        elif activate_protection():
            logging.info("Protection Casted")
        elif is_channeling_active() and activate_premium():
            logging.info("premium activated")
        else:
            return False
        return True


#Grabs the current Screen to be used
def screenGrab():
    im = ImageGrab.grab(Settings.box)
    #im = ImageGrab.grab()
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im


def screenGrab_save(file_name='', level=''):
    im = ImageGrab.grab(Settings.box)
    #im = ImageGrab.grab()
    if len(file_name) > 0:
        if len(level) > 0:
            if level == "health":
                im.save(os.getcwd() + '\\images\\debug\\health\\' + file_name + "_" + str(int(time.time())) + '.png', 'PNG')
            elif level == "mana":
                im.save(os.getcwd() + '\\images\\debug\\mana\\' + file_name + "_" + str(int(time.time())) + '.png', 'PNG')
            elif level == "spirit":
                im.save(os.getcwd() + '\\images\\debug\\spirit\\' + file_name + "_" + str(int(time.time())) + '.png', 'PNG')
            else:
                logging.warning("screenGrab_save level unknown, saving at root")
                im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
        else:
            im.save(os.getcwd() + '\\' + file_name + "_" + str(int(time.time())) + '.png', 'PNG')
    else:
        im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im


def screenGrab_all():
    im = ImageGrab.grab()
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im


def set_player(player):
    Cord.Cure = player.Cure
    Cord.Regen = player.Regen
    #Cord.Items = list(player.Items)
    get_items()
    Cord.Protection = player.Protection
    Cord.premium = player.premium
    Settings.style = player.style
    Cord.special_attack = player.special_attack


def sleep():
    time.sleep(random.uniform(0.5, Settings.sleep))


def start_arena(start=1, end=22):#UNFINISHED
    Count = 0
    Round = start - 1
    get_boundaries()
    for i in range(0, 2):
        for arena in Cord.arenas:
            Count += 1
            if Cord.arenas[Round] != arena:
                logging.debug("skipping arena %d" % Count)
                continue
            else:
                Round += 1
            if Count >= end:
                logging.info("Arenas Complete")
                return
            im = screenGrab()
            if not recover():
                while get_health(im) != 100 or get_mana(im) != 100 or get_spirit(im) != 100:
                    logging.debug("Player still recovering")
                    time.sleep(60)
                    mousePos(Cord.battle_cat_loc)
                    leftClick()
                    time.sleep(1)
                    get_boundaries()
                    im = screenGrab()
                    logging.debug("%d, %d, %d" % (get_health(im), get_mana(im), get_spirit(im)))
            logging.info("Starting Arena %d" % Count)
            go_to_arena(arena, i)
            startGame()
            press("spacebar")
            sleep()
            logging.info("Heading to next Arena.")
        Round -= 11



#Main Function
def startGame(): #UNFINISHED
    logging.basicConfig(filename=Settings.log_loc, level=Settings.log_level, format='%(asctime)s %(levelname)s: %(message)s')
    logging.info("Starting Game")
    reset_cooldown()
    get_boundaries()
    im = screenGrab()
    set_player(Settings.Player)
    #print "%d enemies" %len(getEnemies(im))
    battle_end = False
    while not battle_end:
        if len(get_enemies(im)) == 0 or pony_time(im):
            time.sleep(1.5)
            im = screenGrab()
            if len(get_enemies(im)) == 0 and not pony_time(im):
                logging.info("Battle ended: getEnemies was %d and Pony Time was %r" % (len(get_enemies(im)), pony_time(im)))
                battle_end = True
        else:
            startRound()
            time.sleep(0.5)
            press('spacebar')
            im = screenGrab()
            if is_player_dead(im):
                logging.info("Player is dead")
                leftover_inventory()
                return
            time.sleep(1)
            im = screenGrab()


def start_grindfest():
    while 1 == 1:
        get_boundaries()
        im = screenGrab()
        if not recover():
            while get_health(im) != 100 or get_mana(im) != 100 or get_spirit(im) != 100:
                logging.debug( "Player still recovering")
                time.sleep(60)
                mousePos(Cord.battle_cat_loc)
                leftClick()
                time.sleep(1)
                get_boundaries()
                im = screenGrab()
        logging.info("Starting Grindfest")
        go_to_grindfest()
        startGame()
        sleep()
        mousePos(Cord.battle_cat_loc)
        leftClick()
        logging.info("Player Dead, waiting until revival.")
        sleep()



def startRound(): #UNFINISHED
    #logging.config.fileConfig(os.path.join('settings', "logging.conf"))
    logging.info("Starting Round.")
    enemy_num = 0
    get_gem()
    style = Settings.style
    while not round_won() and not Cord.p_dead:
        #time.sleep(1)
        reduce_cooldown()
        im = screenGrab()
        current_enemies = get_enemies(im)
        #print str(current_enemies) + " enemies"
        #debug_levels(get_health(im), "health")
        #debug_levels(get_mana(im), "mana")
        #debug_levels(get_spirit(im), "spirit")
        get_status()
        if restore_stats(im):
            """restoration occurred"""
        elif 0 < len(current_enemies) < enemy_num:
            get_gem()
        else:
            special_attack(im, current_enemies, style)
        #this sleep function triggers the amount of time between clicks, thus the time between server communication
        #This function is very important as it randomizes the communication times, emulating the behavior of a player
        sleep()
        enemy_num = len(current_enemies)

if __name__ == '__main__':
    startGame()