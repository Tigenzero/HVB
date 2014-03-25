__author__ = 'Matt'
"""
For Screen Resolution 1920 X 1080
"""
import ImageGrab
import os
import time
import win32api, win32con
from numpy import *

class Cord:
    chrome_popup_padding_y = 52
    firefox_padding_y = 64
    chrome_padding_y = 61
    current_browser = chrome_popup_padding_y
    e_x = 890
    p_x0 = 22
    p_x10 = 33
    p_x20 = 44
    p_x30 = 55
    p_x40 = 66
    p_x50 = 77
    p_x60 = 88
    p_x70 = 99
    p_x80 = 101
    p_x90 = 123
    p_x100 = 134
    #p_health = 196
    p_health = current_browser + 144
    p_spirit = current_browser + 227
    p_overcharge = current_browser + 267
    p_health_levels = ((p_x0, p_health), (p_x10, p_health), (p_x20, p_health), (p_x30, p_health),
                      (p_x40, p_health), (p_x50, p_health), (p_x60, p_health), (p_x70, p_health),
                      (p_x80, p_health), (p_x90, p_health), (p_x100, p_health))
    
    p_spirit_levels = ((p_x0, p_spirit), (p_x10, p_spirit), (p_x20, p_spirit), (p_x30, p_spirit),
                      (p_x40, p_spirit), (p_x50, p_spirit), (p_x60, p_spirit), (p_x70, p_spirit),
                      (p_x80, p_spirit), (p_x90, p_spirit), (p_x100, p_spirit))

    p_Overcharge_Max = (p_x100, p_overcharge)
    spirit_cat_loc = (508, current_browser + 60)
    spirit_active_color = (170, 36, 36)
    #round_won = (550, 191)
    round_won = (550, current_browser + 139) #UNTESTED
    #round_won_color = (251, 221, 65) #UNTESTED
    round_won_color = (165,111,44)
    under_color = (0, 0, 0) #Black
    over_color = (0, 166, 23) #Green
    spirit_over_color = (120, 70, 0)
    empty_color = (237, 235, 223) #Background Color UNTESTED
    dead_color = (166, 165, 156) #Dead Enemy Color UNTESTED
    spark_of_life_color = (192, 192, 192) #Color when Spark of Life is Active UNTESTED
    Pony_check_loc = (705, current_browser + 385)
    Pony_check_color = (237, 235, 223)
    #e1_health = (e_x, 125)
    #e2_health = (e_x, 183)
    #e3_health = (e_x, 240)
    #e4_health = (e_x, 298)
    #e5_health = (e_x, 357)
    #e6_health = (e_x, 414)
    #e7_health = (e_x, 472)
    #e8_health = (e_x, 531)
    #e9_health = (e_x, 589) #untested
    #e10_health = (e_x, 642) #untested
    e1_health = (e_x, current_browser + 73)
    e2_health = (e_x, current_browser + 131)
    e3_health = (e_x, current_browser + 188)
    e4_health = (e_x, current_browser + 246)
    e5_health = (e_x, current_browser + 305)
    e6_health = (e_x, current_browser + 362)
    e7_health = (e_x, current_browser + 420)
    e8_health = (e_x, current_browser + 479)
    e9_health = (e_x, current_browser + 537) #untested
    e10_health = (e_x, current_browser + 590) #untested

    enemies = (e1_health, e2_health, e3_health, e4_health, e5_health, e6_health, e7_health, e8_health, e9_health, e10_health)
    s_y = current_browser + 238
    #s_y = 290
    s1 = (188, s_y)
    s2 = (225, s_y)
    s3 = (262, s_y)
    s4 = (299, s_y)
    s5 = (338, s_y)
    s6 = (375, s_y)
    s7 = (412, s_y)
    s8 = (447, s_y)
    s9 = (485, s_y)
    s10 = (523, s_y)
    s11 = (559, s_y)
    s12 = (598, s_y)
    s13 = (630, s_y)
    s14 = (671, s_y)
    s15 = (707, s_y)
    s16 = (743, s_y)
    skills = (s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16)
    Cure = s1
    item_xloc = 261
    Item_cat_loc = (418, current_browser + 65)
    gem_loc = (item_xloc, current_browser + 210)
    i1 = (item_xloc, current_browser + 230)
    i2 = (item_xloc, current_browser + 254)
    i3 = (item_xloc, current_browser + 278)
    i4 = (item_xloc, current_browser + 300)
    i5 = (item_xloc, current_browser + 324)
    i6 = (item_xloc, current_browser + 345)
    i7 = (item_xloc, current_browser + 368)
    i8 = (item_xloc, current_browser + 391)
    i9 = (item_xloc, current_browser + 414)
    i10 = (item_xloc, current_browser + 438)
    i11 = (item_xloc, current_browser + 460)
    i12 = (item_xloc, current_browser + 482)
    i13 = (item_xloc, current_browser + 507)
    i14 = (item_xloc, current_browser + 530)
    scroll_xloc = 550
    scroll1_loc = (scroll_xloc, current_browser + 234)
    infusion1_loc = (scroll_xloc, current_browser + 253)
    item_locs = (i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, scroll1_loc, infusion1_loc)
    # 0 = Health, 1 = Mana, 2 = Spirit, 9 = used
    # Health has 30 round cooldown, Mana and Spirit have 15 round cooldown
    Items = [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    p_dead = False


class Cooldown:
    cure = 0
    overcharge = 0
    h_potion = 0
    m_potion = 0
    s_potion = 0


def attack(enemy):
    mousePos(enemy)
    leftClick()


def castCure():
    mousePos(Cord.Cure)
    leftClick()


def enemies_exist(im):
    for enemy in Cord.enemies:
        if im.getpixel(enemy) == Cord.over_color or im.getpixel(enemy) == Cord.under_color:
            return True
    return False


def get_cords():
    x,y = win32api.GetCursorPos()
    print x,y


#Pulls the current alive Enemies and places them in the current_enemy list
#EDIT: Pulls first enemy, multiple enemies will be introduced later
def getEnemies(im):
    #current_enemies = ()
    #enemy_num = 0
    for enemy in Cord.enemies:
        #enemy_num = enemy_num + 1
        if im.getpixel(enemy) == Cord.over_color or im.getpixel(enemy) == Cord.under_color:
            return enemy
    #        current_enemies.__add__(enemy)
    #        print "enemy %d is alive at %s" % (enemy_num, current_enemies.__getitem__(enemy_num-1).__str__())
    #return current_enemies


def getHealth(im):
    p_health = 0
    for level in Cord.p_health_levels:
        if im.getpixel(level) != Cord.under_color:
            p_health += 10
        else:
            return p_health
    return 100


def getOvercharge(im):
    if im.getpixel(Cord.p_Overcharge_Max) != Cord.under_color:
        return 100
    else:
        return 0


def getSpirit(im):#UNFINISHED
    p_spirit = 0
    for level in Cord.p_spirit_levels:
        if im.getpixel(level) != Cord.under_color:
            p_spirit += 10
        else:
            return p_spirit
    return 100


def haveItem(item_type):
    for item in Cord.Items:
        if item == item_type:
            return True
    return False


def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    #print "Click."          #completely optional. But nice for debugging purposes.


def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print 'left Down'


def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print 'left release'


def mousePos(cord):
    win32api.SetCursorPos((cord[0], cord[1]))


def press(*args):
    '''
    one press, one release.
    accepts as many arguments as you want. e.g. press('left_arrow', 'a','b').
    '''
    for i in args:
        win32api.keybd_event(VK_CODE[i], 0,0,0)
        time.sleep(.05)
        win32api.keybd_event(VK_CODE[i],0 ,win32con.KEYEVENTF_KEYUP ,0)
#Determines if round has been won or not
def roundWon():
    im = screenGrab()
    #if im.getpixels(Cord.round_won) == Cord.round_won_color:
     #   return True
    if enemies_exist(im) == False:
        return True
    else:
        return False


def reduceCooldown():
    Cooldown.cure = Cooldown.cure - 1
    Cooldown.overcharge = Cooldown.overcharge - 1
    Cooldown.h_potion = Cooldown.h_potion - 1
    Cooldown.m_potion = Cooldown.m_potion - 1
    Cooldown.s_potion = Cooldown.s_potion - 1

#Grabs the current Screen to be used
def screenGrab():
    box = ()
    im = ImageGrab.grab()
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im


#Main Function
def startGame(): #UNFINISHED
    print "Starting Game"
    Cooldown.cure = 0
    Cooldown.overcharge = 0
    Cooldown.h_potion = 0
    im = screenGrab()
    while im.getpixel(Cord.Pony_check_loc) == Cord.Pony_check_color and Cord.p_dead == False:
        startRound()
        time.sleep(0.5)
        press('spacebar')
        time.sleep(0.5)
        im = screenGrab()


#Performs all of the needed functions during a round
def startRound(): #UNFINISHED
    print "Starting Round"

    while roundWon() == False and Cord.p_dead == False:
        time.sleep(1)
        reduceCooldown()
        im = screenGrab()
        current_enemies = getEnemies(im)
        current_health = getHealth(im)
        current_spirit = getSpirit(im)
        current_overcharge = getOvercharge(im)
        if current_health == 0:
            Cord.p_dead = True
        elif current_health < 30 and Cooldown.cure <= 0:
            castCure()
            Cooldown.cure = 2
        elif current_health < 30 and Cooldown.h_potion <= 0:
            useHealthPot()
        elif current_overcharge == 100 and Cooldown.overcharge <= 0 and current_spirit >= 30 and im.getpixel(Cord.spirit_cat_loc) != Cord.spirit_active_color:
            useSpirit()
        else:
            use_gem()
            attack(current_enemies)
        time.sleep(0.5)


def useHealthPot(): #UNFINISHED
    if haveItem(0):
        print "Using Health Potion"
        use_item(0)
        Cooldown.h_potion = 30
    else:
        print "No Health Potions Left"
        Cooldown.h_potion = 999


def use_gem():
    mousePos(Cord.gem_loc)
    leftClick()

def use_item(item_type):
    for i in range(0, len(Cord.Items)):
        if Cord.Items[i] == item_type:
            Cord.Items[i] = 9
            mousePos(Cord.Item_cat_loc)
            leftClick()
            mousePos(Cord.item_locs[i])
            leftClick()
            return
    print "Item Not Found..."


def useSpirit():
    print "activating Spirit"
    mousePos(Cord.spirit_cat_loc)
    leftClick()
    Cooldown.overcharge = 100

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