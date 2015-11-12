class PonyWatcher(object):
    def __init__(self):
        # (518,  185) TEST
        self.Pony_check_loc = ((706, 170), (760, 122))
        self.Pony_check_color = (237, 235, 223)

    def is_pony_time(self, image):
        if image.getpixel(self.Pony_check_loc[0]) != self.Pony_check_color:
            return True
        else:
            return False

    def pony_time(self, im):
        if im.getpixel(Cord.Pony_check_loc[0]) != Cord.Pony_check_color and len(get_enemies(im)) == 0:
            time.sleep(0.5)
            get_boundaries()
            im = screenGrab()
            for pony in Cord.Pony_check_loc:
                if im.getpixel(pony) != Cord.Pony_check_color and len(get_enemies(im)) == 0:
                    continue
                else:
                    return False
            while im.getpixel(Cord.Pony_check_loc[0]) != Cord.Pony_check_color and len(get_enemies(im)) == 0:
                logging.info("Pony Time!")
                freq = 2500 # Set Frequency To 2500 Hertz
                dur = 1000 # Set Duration To 1000 ms == 1 second
                winsound.Beep(freq, dur)
                time.sleep(4)
                Settings.pony_timer += 1
                im = screenGrab()
                if Settings.pony_timer >= 6:
                    press('backspace')
                    time.sleep(0.2)
                    option = random.randint(0, 2)
                    if option == 0:
                        press('a')
                    if option == 1:
                        press('b')
                    if option == 2:
                        press('c')
                    press('enter')
            return True
        return False