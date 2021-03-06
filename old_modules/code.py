"""
For Screen Resolution 1920 X 1080
"""
import winsound

from numpy import *

from items import get_gem, use_health_pot, use_mana_pot, use_spirit_pot, get_items, use_gem, leftover_inventory, cool_down
from old_modules.Skills import activate_cure, activate_premium, activate_protection, activate_regen, special_attack, get_spirit, \
    activate_auto_cast, activate_spark_life
from user_interface.click_press import *
from user_interface.coordinates import Cord
import Settings
from Status import get_status
from status.image_initialize import get_images
from window_finder import find_window, scanner


def enemies_exist(im):
    for enemy in Cord.enemies:
        if im.getpixel(enemy) == Cord.over_color or im.getpixel(enemy) == Cord.under_color:
            return True
    return False


"""def get_boundaries():
        corner = find_corner()
        Settings.box = (corner[0], corner[1], corner[0] + 1235, corner[1] + 720)
        Cord.window_padding_y = corner[1]
        Cord.window_padding_x = corner[0]"""


def get_cords():
    x, y = win32api.GetCursorPos()
    print x, y


#Pulls the current alive Enemies and places them in the current_enemy list
def get_enemies(im):
    current_enemies = []
    #enemy_num = 0
    for enemy in Cord.enemies:
        #enemy_num = enemy_num + 1
        if im.getpixel(enemy) == Cord.over_color or im.getpixel(enemy) == Cord.under_color:
            #return enemy
            current_enemies.append(enemy)
            #print "enemy %d is alive " % enemy_num
    return current_enemies


def find_window_dimensions(window_grabber=find_window.ScreenGrabber()):
    window_grabber.refresh_image()
    window = scanner.Scanner.run(window_grabber.screen_width,
                                 window_grabber.screen_height,
                                 window_grabber.scan_size,
                                 window_grabber.image,
                                 find_window.WINDOW_COLORS)
    left = window_grabber.find_left(window)
    top = window_grabber.find_top(left, window[1])
    window_grabber.window_dimensions = (left, top, left + 1235, top + 720)


def find_window(self):
    self.refresh_image()
    return scanner.Scanner.run(self.screen_width,
                               self.screen_height,
                               self.scan_size,
                               self.image,
                               find_window.WINDOW_COLORS)


def go_to_arena(level, point):
    mouse_position(Cord.battle_cat_loc)
    time.sleep(0.5)
    mouse_position(Cord.arena_cat_loc)
    left_click()
    time.sleep(1)
    if point == 1:
        mouse_position(Cord.a_next_loc)
        left_click()
        time.sleep(1)
    mouse_position(level)
    left_click()
    time.sleep(1)
    #mouse_position(Cord.a_window_ok_loc)
    #time.sleep(0.5)
    #left_click()
    press("enter")
    time.sleep(1)


def go_to_grindfest():
    mouse_position(Cord.battle_cat_loc)
    time.sleep(0.5)
    mouse_position(Cord.Grindfest_cat_loc)
    left_click()
    time.sleep(0.5)
    mouse_position(Cord.grindfest_button)
    left_click()


def is_channeling_active():
    for status in Cord.Current_Status:
        if status == "Channeling":
            return True
    return False


def pony_time(im):
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


def recover():
    if Settings.recover:
        mouse_position(Cord.restoratives_button)
        left_click()
        mouse_position(Cord.restore_all_button)
    #if Settings.recover >= 0:
    #    mouse_position(Cord.restoratives_button)
    #    left_click()
    #    if Settings.recover == 0:
    #        mouse_position(Cord.restore_all_button)
    #    elif Settings.recover == 1:
    #        mouse_position(Cord.restore_health_button)
    #    elif Settings.recover == 2:
    #        mouse_position(Cord.restore_mana_button)
    #    elif Settings.recover == 3:
    #        mouse_position(Cord.restore_spirit_button)
        left_click()
        sleep()
        return True
    return False


#Determines if round has been won or not
def round_won():
    im = screenGrab()
    #if im.getpixels(Cord.round_won) == Cord.round_won_color:
     #   return True
    if enemies_exist(im) == False:
        return True
    else:
        return False


def restore_stats(im):
        current_health = get_health(im)
        current_spirit = get_spirit(im)
        current_mana = get_mana(im)
        message = ""
        if current_health == 0 and not enemies_exist(im):
            time.sleep(1)
            if current_health == 0 and not enemies_exist(screenGrab()):
                Cord.p_dead = True
                message = "Player has died"
            else:
                return False
        elif use_gem(0, current_health):
            message = "Health Gem Used"
        elif activate_cure(current_health):
            message = "Cure Casted"
        elif activate_spark_life(current_health):
            message = "Spark Life Casted"
        elif use_health_pot(current_health):
            message = "Health Potion used"
        elif use_gem(1, current_mana):
            message = "Mana Gem Used"
        elif use_mana_pot(current_mana):
            message = "Mana Potion used"
        elif use_gem(2, current_spirit):
            message = "Spirit Gem Used"
        elif use_spirit_pot(current_spirit):
            message = "Spirit Potion used"
        elif activate_regen(current_health):
            message = "Regen Casted"
        elif activate_protection():
            message = "Protection Casted"
        elif is_channeling_active() and activate_premium():
            message = "premium activated"
        #elif activate_absorb():
        #    message = "absorb activated")
        elif activate_auto_cast():
            message = "auto skill activated"
        return message


def sleep():
    time.sleep(random.uniform(Settings.min_sleep, Settings.max_sleep))


def start_arena(start=1, end=21):#UNFINISHED
    Count = 0
    Starting_Point = 0
    Round = start - 1
    if Round > 10:
        Round -= 11
        Starting_Point = 1
    get_boundaries()
    stop_arena = False
    for i in range(Starting_Point, 2):
        if stop_arena:
            return
        for arena in Cord.arenas:
            if stop_arena:
                return
            Count += 1
            if Cord.arenas[Round] != arena:
                logging.debug("skipping arena %d" % Count)
                continue
            else:
                Round += 1
            if Count >= end:
                logging.info("Arenas Complete")
                return
            im = screenGrab()
            if not recover():
                while get_health(im) != 100 or get_mana(im) != 100 or get_spirit(im) != 100:
                    logging.debug("Player still recovering")
                    time.sleep(60)
                    mouse_position(Cord.battle_cat_loc)
                    left_click()
                    time.sleep(1)
                    get_boundaries()
                    im = screenGrab()
                    logging.debug("%d, %d, %d" % (get_health(im), get_mana(im), get_spirit(im)))
            logging.info("Starting Arena %d" % Count)
            go_to_arena(arena, i)
            if not startGame():
                stop_arena = True
                return
            press("spacebar")
            sleep()
            logging.info("Heading to next Arena.")
        Round -= 11



#Main Function
def startGame(): #UNFINISHED
    logging.basicConfig(filename=Settings.log_loc, level=Settings.log_level, format='%(asctime)s %(levelname)s: %(message)s')
    logging.info("Starting Game")
    #reset_cooldown()
    get_boundaries()
    im = screenGrab()
    get_images()
    get_items()
    if len(Settings.Player.skills[0]) <= 1:
        logging.critical("skills not set, shutting down")
        SystemExit
    #print "%d enemies" %len(getEnemies(im))
    battle_end = False
    while not battle_end:
        if len(get_enemies(im)) == 0 or pony_time(im):
            press('spacebar')
            time.sleep(1.5)
            im = screenGrab()
            if len(get_enemies(im)) == 0 and not pony_time(im):
                logging.info("Battle ended: getEnemies was %d and Pony Time was %r" % (len(get_enemies(im)), pony_time(im)))
                #creenGrab_save()
                leftover_inventory()
                battle_end = True
        else:
            Settings.pony_timer = 0
            if not start_round():
                return False
            time.sleep(0.5)
            press('spacebar')
            im = screenGrab()
            if is_player_dead(im):
                logging.info("Player is dead")
                leftover_inventory()
                return False
            time.sleep(1)
            im = screenGrab()
    return True


def start_grindfest():
    while 1 == 1:
        get_boundaries()
        im = screenGrab()
        if not recover():
            while get_health(im) != 100 or get_mana(im) != 100 or get_spirit(im) != 100:
                logging.debug( "Player still recovering")
                time.sleep(60)
                mouse_position(Cord.battle_cat_loc)
                left_click()
                time.sleep(1)
                get_boundaries()
                im = screenGrab()
        logging.info("Starting Grindfest")
        go_to_grindfest()
        if not startGame():
            return
        sleep()
        mouse_position(Cord.battle_cat_loc)
        left_click()
        logging.info("Player Dead, waiting until revival.")
        sleep()



def start_round():
    logging.info("Starting Round.")
    enemy_num = 0
    get_gem()
    style = Settings.Player.style
    Settings.pause = False
    while not round_won() and not Cord.p_dead:
        if Settings.pause:
            return False
        #reduce_cooldown()
        im = screenGrab()
        if im.getpixel((42, 710)) != (227, 224, 209):
            continue
        current_enemies = get_enemies(im)
        cool_down()
        #logging.debug("Enemies: {} Health: {} Mana: {} Spirit: {}".format(len(current_enemies), get_health(im), get_mana(im), get_spirit(im)))
        log_message = "{},{},{},{},".format(len(current_enemies), get_health(im), get_mana(im), get_spirit(im))
        get_status()
        restore_message = restore_stats(im)
        if len(restore_message) > 0:
            log_message = log_message + restore_message
            time.sleep(0.2)
        elif 0 < len(current_enemies) < enemy_num:
            log_message = log_message + get_gem()
        else:
            message = special_attack(im, current_enemies, style)
            log_message = log_message + message
        #this sleep function triggers the amount of time between clicks, thus the time between server communication
        #This function is very important as it randomizes the communication times, emulating the behavior of a player
        #sleep()
        logging.info(log_message)
        enemy_num = len(current_enemies)
    return True

if __name__ == '__main__':
    startGame()