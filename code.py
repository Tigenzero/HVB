"""
For Screen Resolution 1920 X 1080
"""
import ImageGrab
import winsound
import ImageOps
from numpy import *
from find_window import find_corner
import logging
import logging.config
from Players import *
import os
from Items import use_gem, use_health_pot, use_mana_pot, use_spirit_pot
from Skills import activate_cure, activate_premium, activate_protection, activate_regen, special_attack, get_spirit
from Click_Press import *
from Cooldown import *
from Coordinates import Cord


class Settings:
    full_screen = 0
    Player = Player_1
    box = []
    behavior, style = 0, 0
    #Recover: -1: none, 0:all, 1:health, 2: magic, 3: spirit
    recover = -1
    sleep = 2


class Status:
    channeling = 10527
    protection = 9619
    shadow_veil = 7476
    hastened = 10229
    nothing = 1162
    spirit_shield = 7827
    heartseeker = 6340
    collection = {channeling: 'channeling',
                  protection: 'protection',
                  shadow_veil: 'shadow_veil',
                  hastened: 'hastened',
                  spirit_shield: 'spirit_shield',
                  heartseeker: 'heartseeker'}


def enemies_exist(im):
    for enemy in Cord.enemies:
        if im.getpixel(enemy) == Cord.over_color or im.getpixel(enemy) == Cord.under_color:
            return True
    return False


def get_boundaries():
    #if Settings.full_screen == 0:
        corner = find_corner()
        #for 1920 X 1080
        Settings.box = (corner[0], corner[1], corner[0] + 1235, corner[1] + 701)
        Cord.window_padding_y = corner[1]
        Cord.window_padding_x = corner[0]
    #else:
     #   y = find_browser()
      #  corner = (0, y)
       # Settings.box = (corner[0], corner[1], corner[0] + 1235, corner[1] + 701)


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


def get_pixel_sum(box):
    im = ImageOps.grayscale(ImageGrab.grab((Settings.box[0] + box[0], Settings.box[1] + box[1], Settings.box[0] + box[2], Settings.box[1] + box[3])))
    a = array(im.getcolors())
    a = a.sum()
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return a


def get_status():
    Cord.Current_Status = []
    for status in Cord.Status:
        pixel_sum = get_pixel_sum(status)
        if pixel_sum == Status.nothing:
            return
        lookup = lookup_status(pixel_sum)
        if len(lookup) > 1:
            Cord.Current_Status.append(lookup)


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


def lookup_status(pixel_sum):
    for known_status in Status.collection:
        if pixel_sum == known_status:
            #print "status found: %s" % Status.collection.get(known_status)
            return Status.collection.get(known_status)
    return " "


def pony_time(im):
    if im.getpixel(Cord.Pony_check_loc) != Cord.Pony_check_color and len(get_enemies(im)) == 0:
        time.sleep(0.5)
        get_boundaries()
        im = screenGrab()
        while im.getpixel(Cord.Pony_check_loc) != Cord.Pony_check_color and len(get_enemies(im)) == 0:
            print "Pony Time!"
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
            Cord.p_dead = True
            print "Player has died"
        elif activate_cure(current_health, current_mana):
            print "Cure Casted"
        elif use_health_pot(current_health):
            print "Health Potion used"
        elif use_mana_pot(current_mana):
            print "Using Mana Potion"
        elif use_spirit_pot(current_spirit):
            print "Using Spirit Potion"
        elif activate_regen(current_health):
            print "Regen Casted"
        elif activate_protection():
            print "Protection Casted"
        elif is_channeling_active() and activate_premium():
            print "premium activated"
        else:
            return False
        return True


#Grabs the current Screen to be used
def screenGrab():
    im = ImageGrab.grab(Settings.box)
    #im = ImageGrab.grab()
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im

def screenGrab_save():
    im = ImageGrab.grab(Settings.box)
    #im = ImageGrab.grab()
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im

def screenGrab_all():
    im = ImageGrab.grab()
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im


def set_player(player):
    Cord.Cure = player.Cure
    Cord.Iris_Strike = player.Iris_Strike
    Cord.Regen = player.Regen
    Cord.Items = player.Items
    Cord.Protection = player.Protection
    Cord.shield_bash = player.shield_bash
    Cord.shockblast = player.shockblast
    Cord.premium = player.premium
    Settings.style = player.style
    Cord.special_attack = player.special_attack


def sleep():
    time.sleep(random.uniform(0.5, Settings.sleep))


def start_arena():#UNFINISHED
    Count = 0
    get_boundaries()
    for i in range(0, 2):
        for arena in Cord.arenas:
            Count += 1
            im = screenGrab()
            if not recover():
                while get_health(im) != 100 or get_mana(im) != 100 or get_spirit(im) != 100:
                    print "Player still recovering"
                    time.sleep(60)
                    mousePos(Cord.battle_cat_loc)
                    leftClick()
                    time.sleep(1)
                    get_boundaries()
                    im = screenGrab()
                    print "%d, %d, %d" % (get_health(im), get_mana(im), get_spirit(im))
            print "Starting Arena %d" % Count
            go_to_arena(arena, i)
            startGame()
            press("spacebar")
            sleep()
            print "Heading to next Arena."


#Main Function
def startGame(): #UNFINISHED
    set_player(Settings.Player)
    print "Starting Game"
    reset_cooldown()
    get_boundaries()
    im = screenGrab()
    #print "%d enemies" %len(getEnemies(im))
    battle_end = False
    while not battle_end:
        if len(get_enemies(im)) == 0 or pony_time(im):
            time.sleep(1.5)
            im = screenGrab()
            if len(get_enemies(im)) == 0 and not pony_time(im):
                print "Battle ended: getEnemies was %d and Pony Time was %r" % (len(get_enemies(im)), pony_time(im))
                battle_end = True
        else:
            startRound()
            time.sleep(0.5)
            press('spacebar')
            im = screenGrab()
            if is_player_dead(im):
                print "Player is dead"
                return
            time.sleep(1)
            im = screenGrab()


def start_grindfest():
    while 1 == 1:
        get_boundaries()
        im = screenGrab()
        if not recover():
            while get_health(im) != 100 or get_mana(im) != 100 or get_spirit(im) != 100:
                print "Player still recovering"
                time.sleep(60)
                mousePos(Cord.battle_cat_loc)
                leftClick()
                time.sleep(1)
                get_boundaries()
                im = screenGrab()
        print "Starting Grindfest"
        go_to_grindfest()
        startGame()
        sleep()
        mousePos(Cord.battle_cat_loc)
        leftClick()
        print "Player Dead, waiting until revival."
        sleep()


#Performs all of the needed functions during a round
def startRound(): #UNFINISHED
    #logging.config.fileConfig(os.path.join('settings', "logging.conf"))
    print "Starting Round."
    enemy_num = 0
    use_gem()
    style = Settings.style
    while not round_won() and not Cord.p_dead:
        #time.sleep(1)
        reduce_cooldown()
        im = screenGrab()
        current_enemies = get_enemies(im)
        get_status()
        if restore_stats(im):
            """restoration occurred"""
        else:
            special_attack(im, current_enemies, style)
        #this sleep function triggers the amount of time between clicks, thus the time between server communication
        #This function is very important as it randomizes the communication times, emulating the behavior of a player
        sleep()
        if len(current_enemies) < enemy_num:
            use_gem()
        enemy_num = len(current_enemies)

if __name__ == '__main__':
    startGame()