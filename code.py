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
    p_overcharge = current_browser + 267 #UNTESTED UNCHECKED
    p_health_levels = ((p_x0, p_health), (p_x10, p_health), (p_x20, p_health), (p_x30, p_health),
                      (p_x40, p_health), (p_x50, p_health), (p_x60, p_health), (p_x70, p_health),
                      (p_x80, p_health), (p_x90, p_health), (p_x100, p_health))
    
    p_spirit_levels = ((p_x0, p_spirit), (p_x10, p_spirit), (p_x20, p_spirit), (p_x30, p_spirit),
                      (p_x40, p_spirit), (p_x50, p_spirit), (p_x60, p_spirit), (p_x70, p_spirit),
                      (p_x80, p_spirit), (p_x90, p_spirit), (p_x100, p_spirit))

    p_Overcharge_Max = (p_x100, p_overcharge)

    #round_won = (550, 191)
    round_won = (550, current_browser + 139) #UNTESTED
    round_won_color = (251, 221, 65) #UNTESTED
    under_color = (0, 0, 0) #Black UNTESTED
    over_color = (0, 166, 23) #Green
    spirit_over_color = (255, 0, 0) #a red color UNTESTED UNCHECKED
    empty_color = (237, 235, 223) #Background Color UNTESTED
    dead_color = (166, 165, 156) #Dead Enemy Color UNTESTED
    spark_of_life_color = (192, 192, 192) #Color when Spark of Life is Active UNTESTED
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


def attack(enemy):
    mousePos(enemy)
    leftClick()


def castCure():
    mousePos(Cord.Cure)
    leftClick()


def get_cords():
    x,y = win32api.GetCursorPos()
    print x,y


#Pulls the current alive Enemies and places them in the current_enemy list
def getEnemies(im):
    current_enemies = ()
    for enemy in Cord.enemies:
        if im.getpixel(enemy) == Cord.over_color or im.getpixel(enemy) == Cord.under_color:
            current_enemies.append(enemy)
    return current_enemies


def getHealth(im):
    p_health = 0
    for level in Cord.p_health_levels:
        if im.getpixel(level) == Cord.over_color:
            p_health += 10
        else:
            return p_health


def getOvercharge(im):
    if im.getpixel(Cord.p_Overcharge_Max) == Cord.over_color:
        return 100
    else:
        return 0


def getSpirit(im):#UNFINISHED
    p_spirit = 0
    for level in Cord.p_spirit_levels:
        if im.getpixel(level) == Cord.spirit_over_color:
            p_spirit += 10
        else:
            return p_spirit
    
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
    win32api.SetCursorPos(cord[0], cord[1])


#Determines if round has been won or not
def roundWon():
    im = screenGrab()
    if im.getpixels(Cord.round_won) == Cord.round_won_color:
        return True
    else:
        return False


#Grabs the current Screen to be used
def screenGrab():
    box = ()
    im = ImageGrab.grab()
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im


#Main Function
def startGame(): #UNFINISHED
    print "Starting Game"


#Performs all of the needed functions during a round
def startRound(): #UNFINISHED
    print "Starting Round"
    cure_cooldown = 0
    overcharge_cooldown = 0
    h_potion_cooldown = 0
    while roundWon() != True:
        time.sleep(1.5)
        cure_cooldown = cure_cooldown - 1
        overcharge_cooldown = overcharge_cooldown - 1
        h_potion_cooldown = h_potion_cooldown - 1
        im = screenGrab()
        current_enemies = getEnemies(im)
        current_health = getHealth(im)
        current_spirit = getSpirit(im)
        current_overcharge = getOvercharge(im)
        if current_health < 30 and cure_cooldown <= 0:
            castCure()
            cure_cooldown = 2
        elif current_health < 30 and h_potion_cooldown <= 0:
            useHealthPot()
            h_potion_cooldown = 30
        elif current_overcharge == 100 and overcharge_cooldown <= 0:
            useSpirit()
            overcharge_cooldown = 3
        else:
            attack(current_enemies(1))


def useHealthPot(): #UNFINISHED
    print "using health potion"


def useSpirit(): #UNFINISHED
    print "activating Spirit"


if __name__ == '__main__':
    startGame()

