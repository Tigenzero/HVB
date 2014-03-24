__author__ = 'Matt'
import ImageGrab
import os
import time
import win32api, win32con

class Cord:
    e_x = 890
    p_x50 = 75
    p_x10 = 31
    p_x0 = 22
    under_color = (0, 0, 0) #Black
    over_color = (251, 221, 65) #Green
    empty_color = (237, 235, 223) #Background Color
    dead_color = (166, 165, 156) #Dead Enemy Color
    spark_of_life_color = (192, 192, 192) #Color when Spark of Life is Active
    e1_health = (e_x, 127)
    e2_health = (e_x, 183)
    e3_health = (e_x, 240)
    e4_health = (e_x, 298)
    e5_health = (e_x, 357)
    e6_health = (e_x, 414)
    e7_health = (e_x, 472)
    e8_health = (e_x, 531)
    e9_health = ()
    e10_health = ()


    enemies = (e1_health, e2_health, e3_health, e4_health, e5_health, e6_health, e7_health, e8_health, e9_health, e10_health)
    s_y = 290
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



def screenGrab():
    box = ()
    im = ImageGrab.grab()
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')


def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    print "Click."          #completely optional. But nice for debugging purposes.


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

def get_cords():
    x,y = win32api.GetCursorPos()
    print x,y

def startGame():
    print "Starting Game"


def main():
    screenGrab()
if __name__ == '__main__':
    main()

