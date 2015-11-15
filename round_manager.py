import find_window
import pony_watcher
import player_monitor
import enemy_monitor
import item_manager
import Click_Press
import Status
import time
import logging
import image_initialize  # legacy
import Settings  # legacy
import Status  # legacy


class MasterControl(object):
    def __init__(self, mode=0):
        self.window_grabber = find_window.ScreenGrabber()
        self.p_watcher = pony_watcher.PonyWatcher()
        self.player_monitor = player_monitor.PlayerMonitor()
        self.enemy_monitor = enemy_monitor.EnemyMonitor()
        self.item_master = item_manager.ItemManager()
        self.mode = mode
        image_initialize.get_images()
        self.item_master.get_items()

    def start(self):
        logging.info("Master Control starting")
        if len(Settings.Player.skills[0]) <= 1:
            logging.critical("skills not set, shutting down")
            SystemExit
        self.window_grabber.refresh_image()
        if self.mode == 0:
            self._start_general_game()

    def _start_general_game(self):
        battle_end = False
        while not battle_end:
            self.enemy_monitor.get_enemies(self.window_grabber.image)
            if self.enemy_monitor.enemy_count == 0 or self.p_watcher.is_pony_time(self.window_grabber.image):
                Click_Press.press('spacebar')
                time.sleep(1.5)
                self.window_grabber.refresh_image()
                if self.enemy_monitor.enemy_count == 0 and not self.p_watcher.is_pony_time(self.window_grabber.image):
                    battle_end = True
                else:
                    self.p_watcher.activate_pony_time(self.window_grabber)
            else:
                if not self._start_round():
                    return False
                time.sleep(0.5)
                Click_Press.press('spacebar')
                self.window_grabber.refresh_image()
                if self.player_monitor.is_dead:
                    logging.info("Player is dead")
                    return False
                time.sleep(1)
                self.window_grabber.refresh_image()

    def _start_round(self):
        logging.info("Starting Round.")
        enemy_num = 0
        self.item_master.open_items()
        gem_color = Status.get_pixel_sum_color(self.item_master.item_cords.ibox_gem)
        self.item_master.get_gem(gem_color)
        style = Settings.Player.style
        Settings.pause = False
        while not self.enemy_monitor.enemy_count == 0 and not self.player_monitor.is_dead:
            if Settings.pause:
                return False
            #reduce_cooldown()
            self.window_grabber.refresh_image()
            if self.window_grabber.image.getpixel((42, 710)) != (227, 224, 209):
                continue
            self.enemy_monitor.get_enemies(self.window_grabber.image)
            current_enemies = self.enemy_monitor.current_enemies
            self.player_monitor.refresh_stats(self.window_grabber.image)
            self.item_master.cool_down_items()
            #logging.debug("Enemies: {} Health: {} Mana: {} Spirit: {}".format(len(current_enemies), get_health(im), get_mana(im), get_spirit(im)))
            log_message = "{},{},{},{},".format(len(current_enemies), self.player_monitor.health,
                                                self.player_monitor.mana, self.player_monitor.spirit)
            Status.get_status()
            restore_message = restore_stats(im)
            if len(restore_message) > 0:
                log_message = log_message + restore_message
                time.sleep(0.2)
            elif 0 < len(current_enemies) < enemy_num:
                self.item_master.open_items()
                gem_color = Status.get_pixel_sum_color(self.item_master.item_cords.ibox_gem)
                log_message = log_message + self.item_master.get_gem(gem_color)
            else:
                message = special_attack(im, current_enemies, style)
                log_message = log_message + message
            #this sleep function triggers the amount of time between clicks, thus the time between server communication
            #This function is very important as it randomizes the communication times, emulating the behavior of a player
            #sleep()
            logging.info(log_message)
            enemy_num = len(current_enemies)
        return True