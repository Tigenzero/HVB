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


def find_window():
    width = get_width()
    height = get_height()
    x_scanner = width/12
    y_scanner = height/12
    im = window_screenGrab()
    for j in range(0, 12):
        for i in range(0, 12):
            temp_x = x_scanner*j
            temp_y = y_scanner*i
            if im.getpixel((temp_x, temp_y)) == (237, 235, 223) or im.getpixel((temp_x, temp_y)) == (227, 224, 209) or im.getpixel((temp_x, temp_y)) == (177, 185, 194):
                #print "window found at %d, %d" % (temp_x, temp_y)
                return temp_x, temp_y
    print "Never Found Window"
    quit()


def find_left(window):
    x = window[0]
    y = window[1]
    im = window_screenGrab()
    count = 0
    last_x = 0
    #while point != orig_point:
    for i in range(1, x):
        if count >= 150:
            return last_x
        temp_point = x - i
        if im.getpixel((temp_point, y)) == (237, 235, 223) or im.getpixel((temp_point, y)) == (227, 224, 209) or im.getpixel((temp_point, y)) == (220, 217, 203):
            last_x = temp_point
            count = 0
        else:
            count += 1

    return last_x


def find_top(x, y):
    im = window_screenGrab()
    count = 0
    last_y = 0
    #while temp_point != orig_point:
    for i in range(1, y):
        if count >= 150:
            return last_y
        temp_point = y - i
        if im.getpixel((x, temp_point)) == (237, 235, 223) or im.getpixel((x, temp_point)) == (227, 224, 209) or im.getpixel((x, temp_point)) == (220, 217, 203):
            #print im.getpixel((x, temp_point)), "match!"
            last_y = temp_point
            count = 0
        else:
            #print im.getpixel((x, temp_point)), "Not a match....  the coordinates are: %d, %d!" % (x, temp_point)
            count += 1

    return last_y


def window_screenGrab():
    #box = ()
    im = ImageGrab.grab()
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im


#for window
def find_corner():
    window = find_window()
    left = find_left(window)
    #print "Left point found at %d!" % left
    top = find_top(left, window[1])
    #print "The Top Left Corner is %d, %d!" % (left, top)
    return left, top

if __name__ == '__main__':
    find_corner()