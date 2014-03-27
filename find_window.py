import win32api
import ImageGrab
"""
 The initial test will involve 1920X1080
 The width of the box will be at least 1293px
"""

def get_width():
    return win32api.GetSystemMetrics(0)


def get_height():
    return win32api.GetSystemMetrics(1)

#The plan is to take the resolution of the screen, split it into 4 scanner X coordinates and 10 Y coordinates in hopes that the window can be quickly found
#Afterwards, the scanner will find the top right corner of the window and determine that the whole window (or at least enough of the window needed to function) is viewable.
def find_window():
    width = get_width()
    height = get_height()
    x_scanner = width/10
    y_scanner = height/4
    im = screenGrab()
    for j in range(1, 4):
        for i in range(1, 10):
            if im.getpixel(x_scanner*i, y_scanner*j) == (237, 235, 223):
                print "window found at %d, %d" % (x_scanner*i, y_scanner*j)
                return (x_scanner*i, y_scanner*j)
    print "Never Found Window"
    return (0, 0)


def find_left(window):
    x = window[0]
    y = window[1]
    x_delimiter = x/4
    im = screenGrab()
    while x != 0:
        for i in range(1,4):
            if im.getpixel(x-(x_delimiter*i), y) != (237, 235, 223):
                x = crawl_right(x-(x_delimiter*i), x, y)
                return x
    return x


def crawl_right(point, orig_point, y):
    im = screenGrab()
    while point != orig_point:
        for i in range(1, orig_point - point):
            if im.getpixel(point + i, y) != (237, 235, 223):
                return (point + i)
    print "no point was found, must have been orig_point"
    return orig_point

def screenGrab():
    box = ()
    im = ImageGrab.grab()
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im


def main():
    window = find_window()
    left = find_left(window)