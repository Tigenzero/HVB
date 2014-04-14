import win32api
from win32con import MOUSEEVENTF_LEFTUP, MOUSEEVENTF_LEFTDOWN
import time
from code import Cord
def leftClick():
    win32api.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0)
    #print "Click."          #completely optional. But nice for debugging purposes.


def leftDown():
    win32api.mouse_event(MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print 'left Down'


def leftUp():
    win32api.mouse_event(MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print 'left release'


def mousePos(cord):
    try:
        #print Cord.window_padding_x + cord[0], ", ", Cord.window_padding_y + cord[1]
        win32api.SetCursorPos((Cord.window_padding_x + cord[0], Cord.window_padding_y + cord[1]))
    except ValueError:
        print "Mouse Positioning Failed"