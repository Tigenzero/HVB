"""
For Screen Resolution 1920 X 1080
"""
import ImageGrab
import winsound
import time
import ImageOps
from numpy import *
from find_window import find_corner, find_browser
import logging
import logging.config
import win32api
import win32con
from Coordinates import Cord
from Players import *
import os
from Items import use_gem, use_health_pot, use_mana_pot, use_spirit_pot
from Skills import activate_cure, activate_premium, activate_protection, activate_regen, special_attack, getSpirit
from Click_Press import *
from Cooldown import *

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
def getEnemies(im):
    current_enemies = []
    #enemy_num = 0
    for enemy in Cord.enemies:
        #enemy_num = enemy_num + 1
        if im.getpixel(enemy) == Cord.over_color or im.getpixel(enemy) == Cord.under_color:
            #return enemy
            current_enemies.append(enemy)
            #print "enemy %d is alive " % enemy_num
    return current_enemies


def getHealth(im):
    p_health = 0
    for level in Cord.p_health_levels:
        if im.getpixel(level) != Cord.under_color:
            p_health += 10
        else:
            return p_health
    return 100


def getMana(im):
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
    if getHealth(im) == 0:
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
    if im.getpixel(Cord.Pony_check_loc) != Cord.Pony_check_color and len(getEnemies(im)) == 0:
        time.sleep(0.5)
        get_boundaries()
        im = screenGrab()
        while im.getpixel(Cord.Pony_check_loc) != Cord.Pony_check_color and len(getEnemies(im)) == 0:
            print "Pony Time!"
            Freq = 2500 # Set Frequency To 2500 Hertz
            Dur = 1000 # Set Duration To 1000 ms == 1 second
            winsound.Beep(Freq, Dur)
            time.sleep(4)
            im = screenGrab()
        return True
    return False

def press(*args):
    '''
    one press, one release.
    accepts as many arguments as you want. e.g. press('left_arrow', 'a','b').
    '''
    for i in args:
        win32api.keybd_event(VK_CODE[i], 0, 0, 0)
        time.sleep(.05)
        win32api.keybd_event(VK_CODE[i], 0, win32con.KEYEVENTF_KEYUP, 0)


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
def roundWon():
    im = screenGrab()
    #if im.getpixels(Cord.round_won) == Cord.round_won_color:
     #   return True
    if enemies_exist(im) == False:
        return True
    else:
        return False


def restore_stats(im):
        current_health = getHealth(im)
        current_spirit = getSpirit(im)
        current_mana = getMana(im)
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
    for i in range(0, 1):
        for arena in Cord.arenas:
            Count += 1
            im = screenGrab()
            if not recover():
                while getHealth(im) != 100 or getMana(im) != 100 or getSpirit(im) != 100:
                    print "Player still recovering"
                    time.sleep(60)
                    mousePos(Cord.battle_cat_loc)
                    leftClick()
                    time.sleep(1)
                    get_boundaries()
                    im = screenGrab()
                    print "%d, %d, %d" % (getHealth(im), getMana(im), getSpirit(im))
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
        if len(getEnemies(im)) == 0 or pony_time(im):
            time.sleep(1.5)
            im = screenGrab()
            if len(getEnemies(im)) == 0 and not pony_time(im):
                print "Battle ended: getEnemies was %d and Pony Time was %r" % (len(getEnemies(im)), pony_time(im))
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
            while getHealth(im) != 100 or getMana(im) != 100 or getSpirit(im) != 100:
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
    while not roundWon() and not Cord.p_dead:
        #time.sleep(1)
        reduceCooldown()
        im = screenGrab()
        current_enemies = getEnemies(im)
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

VK_CODE = {'backspace':0x08,
           'tab':0x09,
           'clear':0x0C,
           'enter':0x0D,
           'shift':0x10,
           'ctrl':0x11,
           'alt':0x12,
           'pause':0x13,
           'caps_lock':0x14,
           'esc':0x1B,
           'spacebar':0x20,
           'page_up':0x21,
           'page_down':0x22,
           'end':0x23,
           'home':0x24,
           'left_arrow':0x25,
           'up_arrow':0x26,
           'right_arrow':0x27,
           'down_arrow':0x28,
           'select':0x29,
           'print':0x2A,
           'execute':0x2B,
           'print_screen':0x2C,
           'ins':0x2D,
           'del':0x2E,
           'help':0x2F,
           '0':0x30,
           '1':0x31,
           '2':0x32,
           '3':0x33,
           '4':0x34,
           '5':0x35,
           '6':0x36,
           '7':0x37,
           '8':0x38,
           '9':0x39,
           'a':0x41,
           'b':0x42,
           'c':0x43,
           'd':0x44,
           'e':0x45,
           'f':0x46,
           'g':0x47,
           'h':0x48,
           'i':0x49,
           'j':0x4A,
           'k':0x4B,
           'l':0x4C,
           'm':0x4D,
           'n':0x4E,
           'o':0x4F,
           'p':0x50,
           'q':0x51,
           'r':0x52,
           's':0x53,
           't':0x54,
           'u':0x55,
           'v':0x56,
           'w':0x57,
           'x':0x58,
           'y':0x59,
           'z':0x5A,
           'numpad_0':0x60,
           'numpad_1':0x61,
           'numpad_2':0x62,
           'numpad_3':0x63,
           'numpad_4':0x64,
           'numpad_5':0x65,
           'numpad_6':0x66,
           'numpad_7':0x67,
           'numpad_8':0x68,
           'numpad_9':0x69,
           'multiply_key':0x6A,
           'add_key':0x6B,
           'separator_key':0x6C,
           'subtract_key':0x6D,
           'decimal_key':0x6E,
           'divide_key':0x6F,
           'F1':0x70,
           'F2':0x71,
           'F3':0x72,
           'F4':0x73,
           'F5':0x74,
           'F6':0x75,
           'F7':0x76,
           'F8':0x77,
           'F9':0x78,
           'F10':0x79,
           'F11':0x7A,
           'F12':0x7B,
           'F13':0x7C,
           'F14':0x7D,
           'F15':0x7E,
           'F16':0x7F,
           'F17':0x80,
           'F18':0x81,
           'F19':0x82,
           'F20':0x83,
           'F21':0x84,
           'F22':0x85,
           'F23':0x86,
           'F24':0x87,
           'num_lock':0x90,
           'scroll_lock':0x91,
           'left_shift':0xA0,
           'right_shift ':0xA1,
           'left_control':0xA2,
           'right_control':0xA3,
           'left_menu':0xA4,
           'right_menu':0xA5,
           'browser_back':0xA6,
           'browser_forward':0xA7,
           'browser_refresh':0xA8,
           'browser_stop':0xA9,
           'browser_search':0xAA,
           'browser_favorites':0xAB,
           'browser_start_and_home':0xAC,
           'volume_mute':0xAD,
           'volume_Down':0xAE,
           'volume_up':0xAF,
           'next_track':0xB0,
           'previous_track':0xB1,
           'stop_media':0xB2,
           'play/pause_media':0xB3,
           'start_mail':0xB4,
           'select_media':0xB5,
           'start_application_1':0xB6,
           'start_application_2':0xB7,
           'attn_key':0xF6,
           'crsel_key':0xF7,
           'exsel_key':0xF8,
           'play_key':0xFA,
           'zoom_key':0xFB,
           'clear_key':0xFE,
           '+':0xBB,
           ',':0xBC,
           '-':0xBD,
           '.':0xBE,
           '/':0xBF,
           '`':0xC0,
           ';':0xBA,
           '[':0xDB,
           '\\':0xDC,
           ']':0xDD,
           "'":0xDE,
           '`':0xC0}