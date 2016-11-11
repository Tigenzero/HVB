# import os
#
# from PIL import Image
#
# from pony_time import pony_watcher
# from window_finder import find_window
#
# TEST_WINDOW_IMAGE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../tests/test_full_window.png")
# TEST_PONY_IMAGE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_pony_image.png")
#
#
# def test_is_pony_time_init():
#     image = Image.open(TEST_WINDOW_IMAGE).convert('RGB')
#     watcher = pony_watcher.PonyWatcher()
#     pass
#
#
# def test_is_pony_time_false():
#     image = Image.open(TEST_WINDOW_IMAGE).convert('RGB')
#     watcher = pony_watcher.PonyWatcher()
#     assert(watcher.is_pony_time(image) is False)
#
#
# def test_activate_pony_time():
#     image = Image.open(TEST_PONY_IMAGE).convert('RGB')
#     window_grabber = find_window.ScreenGrabber()
#     window_grabber.image = image
#     watcher = pony_watcher.PonyWatcher()
#     # need to split out activate_pony_time to enable easier testing
#     pass
#
#
# def test_pony_time_safety_check():
#     image = Image.open(TEST_PONY_IMAGE).convert('RGB')
#     window_grabber = find_window.ScreenGrabber()
#     window_grabber.image = image
#     watcher = pony_watcher.PonyWatcher()
#     # need to split out pony_time_safety_check to enable easier testing
#     pass