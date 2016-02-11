from window_finder.find_window import *
def screenGrab():
    corner = find_corner()
    #for 1920 X 1080
    box = (corner[0], corner[1], corner[0] + 1235, corner[1] + 701)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

def main():
    screenGrab()
if __name__ == '__main__':
    main()