"""
For Screen Resolution 1920 X 1080
"""
import ImageGrab
import os
import winsound
import time
import ImageOps
import win32api, win32con
from numpy import *
from find_window import find_corner, find_browser

#Styles: Dual-wield:0, 1-handed:1, 2-handed:2, mage:3, niken:4
class Player_0:
    style = 0
    # 0 = Health, 1 = Mana, 2 = Spirit, 9 = used
    Items = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1] #main character
    Cure = 0
    Iris_Strike = 8
    Backstab = 9
    Frenzied_Blows = 10
    Regen = 4
    Protection = -1
    #unused
    shield_bash = -1
    shockblast = -1
    premium = [12, 13]


class Player_1:
    style = 1
    Cure = 0
    shield_bash = 1
    #unused
    Iris_Strike = -1
    Regen = -1
    Protection = -1 #3 (costs to much mana)
    shockblast = -1
     # 0 = Health, 1 = Mana, 2 = Spirit, 9 = used
    # Health has 30 round cooldown, Mana and Spirit have 15 round cooldown
    Items = [0,0,0,0,0,0,9,9,9] #Current Items in your Battle Inventory
    premium = [3, -1]

class Settings:
    full_screen = 0
    Player = Player_1
    box = []
    behavior = 0
    style = 0
    #Recover: -1: none, 0:all, 1:health, 2: magic, 3: spirit
    recover = -1


class Cord:
    chrome_popup_padding_y = 52
    firefox_padding_y = 85
    chrome_padding_y = 61

    #window_padding_y = chrome_popup_padding_y
    window_padding_y = 0
    window_padding_x = 0
    #Cure = (188,  96)
    Cure = -1
    Iris_Strike = -1
    Regen = -1
    Items = -1
    Protection = -1
    shield_bash = -1
    shockblast = -1
    premium = []
     # 0 = Health, 1 = Mana, 2 = Spirit, 9 = used
    # Health has 30 round cooldown, Mana and Spirit have 15 round cooldown

#Mapped Menu Buttons
    grindfest_button = (670,  327)
    restoratives_button = (78,  249)
    restore_health_button = (78,  283)
    restore_mana_button = (78,  303)
    restore_spirit_button = (78,  321)
    restore_all_button = (78,  340)
#Player Stat Locations
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
    p_health = 144
    p_mana = 186
    p_spirit = 227
    p_overcharge = 267
    p_health_levels = ((p_x0, p_health), (p_x10, p_health), (p_x20, p_health), (p_x30, p_health),
                      (p_x40, p_health), (p_x50, p_health), (p_x60, p_health), (p_x70, p_health),
                      (p_x80, p_health), (p_x90, p_health), (p_x100, p_health))

    p_mana_levels = ((p_x0, p_mana), (p_x10, p_mana), (p_x20, p_mana), (p_x30, p_mana),
                      (p_x40, p_mana), (p_x50, p_mana), (p_x60, p_mana), (p_x70, p_mana),
                      (p_x80, p_mana), (p_x90, p_mana), (p_x100, p_mana))
    
    p_spirit_levels = ((p_x0, p_spirit), (p_x10, p_spirit), (p_x20, p_spirit), (p_x30, p_spirit),
                      (p_x40, p_spirit), (p_x50, p_spirit), (p_x60, p_spirit), (p_x70, p_spirit),
                      (p_x80, p_spirit), (p_x90, p_spirit), (p_x100, p_spirit))
    
    p_overcharge_levels = ((p_x0, p_overcharge), (p_x10, p_overcharge), (p_x20, p_overcharge), (p_x30, p_overcharge),
                      (p_x40, p_overcharge), (p_x50, p_overcharge), (p_x60, p_overcharge), (p_x70, p_overcharge),
                      (p_x80, p_overcharge), (p_x90, p_overcharge), (p_x100, p_overcharge))

    spirit_cat_loc = (494,  60) #changed, confirm with Chrome. X used to be 508
    spirit_active_color = (250, 59, 56) #(170, 36, 36)
    #round_won = (550, 191)
    round_won = (550,  139) #UNTESTED
    #round_won_color = (251, 221, 65) #UNTESTED
    round_won_color = (165, 111, 44)
    under_color = (0, 0, 0) #Black
    over_color = (0, 166, 23) #Green
    spirit_over_color = (120, 70, 0)
    empty_color = (237, 235, 223) #Background Color UNTESTED
    dead_color = (166, 165, 156) #Dead Enemy Color UNTESTED
    spark_of_life_color = (192, 192, 192) #Color when Spark of Life is Active UNTESTED
    Pony_check_loc = (706,170)  #(518,  185) TEST
    Pony_check_color = (237, 235, 223)
#Enemies
    e_x = 890
    e1_health = (e_x,  73)
    e2_health = (e_x,  131)
    e3_health = (e_x,  188)
    e4_health = (e_x,  246)
    e5_health = (e_x,  305)
    e6_health = (e_x,  362)
    e7_health = (e_x,  420)
    e8_health = (e_x,  479)
    e9_health = (e_x,  537) #untested
    e10_health = (e_x,  595) #untested

    enemies = (e1_health, e2_health, e3_health, e4_health, e5_health, e6_health, e7_health, e8_health, e9_health, e10_health)
#Skills
    s_y = 96
    #s_y = 290
    s1 = ( 188, s_y)
    s2 = ( 225, s_y)
    s3 = ( 262, s_y)
    s4 = ( 299, s_y)
    s5 = ( 338,  s_y)
    s6 = ( 375, s_y)
    s7 = ( 412, s_y)
    s8 = ( 447, s_y)
    s9 = ( 485, s_y)
    s10 = ( 523, s_y)
    s11 = ( 559, s_y)
    s12 = ( 598, s_y)
    s13 = ( 630, s_y)
    s14 = ( 671, s_y)
    s15 = ( 707, s_y)
    s16 = ( 743, s_y)
    skills = (s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16)
#Items
    item_xloc = 261
    Item_cat_loc = (418,  65)
    gem_loc = (item_xloc,  210)
    i1 = (item_xloc,  230)
    i2 = (item_xloc,  254)
    i3 = (item_xloc,  278)
    i4 = (item_xloc,  300)
    i5 = (item_xloc,  324)
    i6 = (item_xloc,  345)
    i7 = (item_xloc,  368)
    i8 = (item_xloc,  391)
    i9 = (item_xloc,  414)
    i10 = (item_xloc,  438)
    i11 = (item_xloc,  460)
    i12 = (item_xloc,  482)
    i13 = (item_xloc,  507)
    i14 = (item_xloc,  530)
    scroll_xloc = 550
    scroll1_loc = (scroll_xloc,  234)
    infusion1_loc = [scroll_xloc,  253]
    item_locs = [i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, scroll1_loc, infusion1_loc]
    # 0 = Health, 1 = Mana, 2 = Spirit, 9 = used
    # Health has 30 round cooldown, Mana and Spirit have 15 round cooldown
    #Items = [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2] #main character
    p_dead = False
    battle_cat_loc = [640,  12]
    Grindfest_cat_loc = [640,  81]
#Statuses
    st_y1 = 13
    st_y2 = 45
    st1 = (167, st_y1, 196, st_y2)
    st2 = (200, st_y1, 229, st_y2)
    st3 = (233, st_y1, 262, st_y2)
    st4 = (266, st_y1, 295, st_y2)
    st5 = (299, st_y1, 328, st_y2)
    st6 = (332, st_y1, 361, st_y2)
    st7 = (365, st_y1, 394, st_y2)
    st8 = (398, st_y1, 427, st_y2)
    st9 = (431, st_y1, 460, st_y2)
    Status = (st1, st2, st3, st4, st5, st6, st7, st8, st9)
    Current_Status = []

#Arena Locations
    arena_cat_loc = (626, 40)
    a_x = 1140
    a_next_loc = (771, 60)
    a1 = 128
    a2 = 165
    a3 = 200
    a4 = 236
    a5 = 271
    a6 = 307
    a7 = 342
    a8 = 381
    a9 = 418
    a10 = 452
    a11 = 486
    arenas = [a1, a2, a3, a4, a5, a6, a7, a8 , a9, a10, a11]



class Cooldown:
    cure = 0
    overcharge = 0
    h_potion = 0
    m_potion = 0
    s_potion = 0
    regen = 0
    protection = 0
    shield_bash = 0
    shockblast = 0
    collection = [cure, overcharge, h_potion, m_potion, s_potion, regen, protection]
    premium = [0, 0]

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

def activate_cure(current_health, current_mana):
    if current_health <= 50 and Cooldown.cure <= 0 and current_mana >= 10 and Cord.Cure >= 0:
        use_skill(Cord.Cure)
        Cooldown.cure = 5
        return True
    else:
        return False


def activate_regen(current_health):
    if current_health <= 60 and Cooldown.regen <= 0 and Cord.Regen >=0:
        print "using Regen"
        use_skill(Cord.Regen)
        Cooldown.regen = 45
        return True
    else:
        return False


def activate_iris_strike(current_spirit, current_overcharge):
    if current_overcharge >= 30 and current_spirit < 100 and Cord.Iris_Strike >= 0:
        use_skill(Cord.Iris_Strike)
        return True
    else:
        return False


def activate_premium():
    for i in range(0, len(Cord.premium)):
        if Cooldown.premium[i] <= 0 and Cord.premium[i] >=0:
            use_skill(Cord.premium[i])
            Cooldown.premium[i] = 45
            return True
        else:
            print "%d greater than 0 and %d less than 0?" % (Cooldown.premium[i], Cord.premium[i])
    return False


def activate_shield_bash(current_spirit, current_overcharge):
    if current_overcharge >= 50 and current_spirit < 80 and Cord.shield_bash >= 0 and Cooldown.shield_bash <= 0:
        use_skill(Cord.shield_bash)
        Cooldown.shield_bash = 11
        return True
    else:
        return False


def activate_protection():
    if Cord.Protection >= 0 and Cooldown.protection <= 0:
        use_skill(Cord.Protection)
        Cooldown.protection = 19
        return True
    else:
        return False


def attack(enemy):
    try:
        mousePos(enemy)
        leftClick()
    except ValueError:
        print "no more enemies"


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


def getOvercharge(im):
    p_overcharge = 0
    for level in Cord.p_overcharge_levels:
        if im.getpixel(level) != Cord.under_color:
            p_overcharge += 10
        else:
            return p_overcharge
    return 100


def get_pixel_sum(box):
    im = ImageOps.grayscale(ImageGrab.grab((Settings.box[0] + box[0], Settings.box[1] + box[1], Settings.box[0] + box[2], Settings.box[1] + box[3])))
    a = array(im.getcolors())
    a = a.sum()
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return a


def getSpirit(im):
    p_spirit = 0
    for level in Cord.p_spirit_levels:
        if im.getpixel(level) != Cord.under_color:
            p_spirit += 10
        else:
            return p_spirit
    return 100


def get_status():
    Cord.Current_Status = []
    for status in Cord.Status:
        pixel_sum = get_pixel_sum(status)
        if pixel_sum == Status.nothing:
            return
        lookup = lookup_status(pixel_sum)
        if len(lookup) > 1:
            Cord.Current_Status.append(lookup)


def go_to_arena(level):
    mousePos(Cord.battle_cat_loc)
    time.sleep(0.5)
    mousePos(Cord.arena_cat_loc)
    leftClick()
    time.sleep(0.5)
    mousePos(Cord.arenas[level])
    leftClick()

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


def is_spirit_active(im):
    if im.getpixel(Cord.spirit_cat_loc) == Cord.spirit_active_color:
        return True
    else:
        return False


def lookup_status(pixel_sum):
    for known_status in Status.collection:
        if pixel_sum == known_status:
            #print "status found: %s" % Status.collection.get(known_status)
            return Status.collection.get(known_status)
    return " "


def haveItem(item_type):
    for i in range(0, len(Cord.Items)):
    #for item in Cord.Items:
        if Cord.Items[i] == item_type:
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
    try:
        #print Cord.window_padding_x + cord[0], ", ", Cord.window_padding_y + cord[1]
        win32api.SetCursorPos((Cord.window_padding_x + cord[0], Cord.window_padding_y + cord[1]))
    except ValueError:
        print "Mouse Positioning Failed"


def multiple_enemy_attack(enemies):
    if len(enemies) >= 5:
        return 2
    elif len(enemies) >= 3:
        return 1
    else:
        return 0

def pony_time(im):
    if im.getpixel(Cord.Pony_check_loc) != Cord.Pony_check_color and len(getEnemies(im)) == 0:
        time.sleep(0.5)
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


def reduceCooldown():
    #for i in range(0, len(Cooldown.collection)):
    #Cooldown.collection[i] = Cooldown.collection[i] -1 Does not update Values
    Cooldown.cure -= 1
    Cooldown.overcharge -= 1
    Cooldown.h_potion -= 1
    Cooldown.m_potion -= 1
    Cooldown.s_potion -= 1
    Cooldown.protection -= 1
    Cooldown.regen -= 1
    Cooldown.shield_bash -= 1
    Cooldown.shockblast -= 1
    #if Cooldown.shield_bash == 0:
        #print "shield bash now active"
    for i in range(0,len(Cooldown.premium)):
        Cooldown.premium[i] -= 1


def reset_cooldown():
    #for i in range(0, len(Cooldown.collection)):
     #   Cooldown.collection[i] = 0
    Cooldown.cure = 0
    Cooldown.overcharge = 0
    Cooldown.h_potion = 0
    Cooldown.m_potion = 0
    Cooldown.s_potion = 0
    Cooldown.protection = 0
    Cooldown.regen = 0
    Cooldown.shield_bash = 0
    Cooldown.shockblast = 0
    for i in range(0, len(Cooldown.premium)):
        Cooldown.premium[i] = 0


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


def special_attack(im, current_enemies):
    current_spirit = getSpirit(im)
    current_overcharge = getOvercharge(im)
    #print "Is Spirit Active? %r" %is_spirit_active(im)
    if not is_spirit_active(im):
            if use_spirit(current_spirit, current_overcharge, im):
                print "Spirit Activated"
            elif activate_iris_strike(current_spirit, current_overcharge):
                if len(current_enemies) > 0:
                    attack(current_enemies[0])
                    print "Iris Strike Used"
            elif activate_shield_bash(current_spirit, current_overcharge):
                if len(current_enemies) > 0:
                    attack(current_enemies[0])
                    print "Shield Bash Used"
            else:
                use_gem()
                if len(current_enemies) > 0:
                    attack(current_enemies[0])
    else:
        return False
    return True


def sleep():
    time.sleep(random.uniform(0.5, 2))


def start_arena():#UNFINISHED
    Count = 0
    get_boundaries()
    for i in range(0, 1):
        for arena in Cord.arenas:
            Count += 1
            im = screenGrab()
            if not recover():
                while getHealth(im) != 100 and getMana(im) != 100 and getSpirit(im) != 100:
                    print "Player still recovering"
                    time.sleep(60)
                    mousePos(Cord.battle_cat_loc)
                    leftClick()
                    time.sleep(1)
                    get_boundaries()
                    im = screenGrab()
                    print "%d, %d, %d" % (getHealth(im), getMana(im), getSpirit(im))
            print "Starting Arena %d" % Count
            go_to_arena(arena)
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
    print "%d enemies" %len(getEnemies(im))
    while len(getEnemies(im)) > 0 or pony_time(im):
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
            while getHealth(im) != 100 and getMana(im) != 100 and getSpirit(im) != 100:
                print "Player still recovering"
                time.sleep(60)
                mousePos(Cord.battle_cat_loc)
                leftClick()
                time.sleep(1)
                get_boundaries()
                im = screenGrab()
                print "%d, %d, %d" % (getHealth(im), getMana(im), getSpirit(im))
        print "Starting Grindfest"
        go_to_grindfest()
        startGame()
        sleep()
        mousePos(Cord.battle_cat_loc)
        leftClick()
        print "Player Dead, waiting until revival."


#Performs all of the needed functions during a round
def startRound(): #UNFINISHED
    print "Starting Round."

    while not roundWon() and not Cord.p_dead:
        #time.sleep(1)
        reduceCooldown()
        im = screenGrab()
        current_enemies = getEnemies(im)
        get_status()
        if restore_stats(im):
            """restoration occurred"""
        elif special_attack(im, current_enemies):
            """special attack occurred"""
        else:
            use_gem()
            if len(current_enemies) > 0:
                attack(current_enemies[0])
        #this sleep function triggers the amount of time between clicks, thus the time between server communication
        #This function is very important as it randomizes the communication times, emulating the behavior of a player
        sleep()


def use_health_pot(current_health):
    if current_health <= 40 and Cooldown.h_potion <= 0:
        if haveItem(0):
            print "Using Health Potion"
            use_item(0)
            Cooldown.h_potion = 20
            return True
        else:
            print "No Health Potions Left"
            Cooldown.h_potion = 999
            return False
    else:
        return False


def use_mana_pot(current_mana):
    if current_mana <= 10 and Cooldown.m_potion <= 0:
        if haveItem(1):
            use_item(1)
            Cooldown.m_potion = 20
            return True
        else:
            print "No Mana Potions Left"
            Cooldown.m_potion = 999
            return False
    else:
        return False


def use_spirit_pot(current_spirit):
    if current_spirit <= 10 and Cooldown.s_potion <= 0:
        if haveItem(2):
            use_item(2)
            Cooldown.s_potion = 20
            return True
        else:
            print "No Spirit Potions Left"
            Cooldown.s_potion = 999
            return False
    else:
        return False


def use_gem():
    mousePos(Cord.Item_cat_loc)
    leftClick()
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


def use_skill(skill):
    #mousePos(Cord.Cure)
    if skill >= 0:
        mousePos(Cord.skills[skill])
        leftClick()


def use_spirit(current_spirit, current_overcharge, im):
    if current_overcharge >= 80 and Cooldown.overcharge <= 0 and current_spirit >= 30 and not is_spirit_active(im):
        mousePos(Cord.spirit_cat_loc)
        leftClick()
        Cooldown.overcharge = 10
        return True
    else:
        return False

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