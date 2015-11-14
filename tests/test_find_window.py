import find_window
from PIL import Image
import scanner

def test_screengrabber_init():
    find_window.ScreenGrabber()
    pass


def test_find_window_corner():
    window_grabber = find_window.ScreenGrabber()
    window_grabber.image = Image.open("test_window.png")
    window_grabber.image.convert('RGB')
    x, y = scanner.Scanner.run(window_grabber.screen_width,
                               window_grabber.screen_height,
                               window_grabber.scan_size,
                               window_grabber.image,
                               find_window.WINDOW_COLORS)
    print("x:{} y:{}".format(x, y))


