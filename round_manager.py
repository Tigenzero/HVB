import time
import logging

import find_window
import pony_watcher
import player_monitor
import enemy_monitor
import item_manager
import click_press
from skill import skill_manager
import status_monitor
import image_initialize  # legacy
import Settings  # legacy
import Status  # legacy
import etc_manager


class MasterControl(object):
    def __init__(self, mode=0):
        self.window_grabber = find_window.ScreenGrabber()
        self.p_watcher = pony_watcher.PonyWatcher()
        self.player_monitor = player_monitor.PlayerMonitor()
        self.enemy_monitor = enemy_monitor.EnemyMonitor()
        self.item_master = item_manager.ItemManager()
        self.skill_master = skill_manager.SkillMaster()
        self.status_monitor = status_monitor.StatusMonitor()
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
                click_press.press('spacebar')
                time.sleep(1.5)
                self.window_grabber.refresh_image()
                if self.enemy_monitor.enemy_count == 0 and not self.p_watcher.is_pony_time(self.window_grabber.image):
                    battle_end = True
                else:
                    self.window_grabber.save()
                    self.p_watcher.activate_pony_time(self.window_grabber)
            else:
                if not self._start_round():
                    return False
                time.sleep(0.5)
                click_press.press('spacebar')
                self.window_grabber.refresh_image()
                if self.player_monitor.is_dead:
                    logging.info("Player is dead")
                    return False
                time.sleep(1)
                self.window_grabber.refresh_image()

    def _start_round(self):
        logging.info("Starting Round.")
        prev_enemy_num = 0
        self._round_init()
        while not self.enemy_monitor.enemy_count == 0 and not self.player_monitor.is_dead:
            if Settings.pause:
                return False
            self._round_refresh_and_cooldown()
            if self.window_grabber.image.getpixel((42, 710)) not in find_window.WINDOW_COLORS:
                continue
            current_enemies = self.enemy_monitor.current_enemies
            log_message = "{},{},{},{},".format(self.enemy_monitor.enemy_count, self.player_monitor.health,
                                                self.player_monitor.mana, self.player_monitor.spirit)
            needed_restore = etc_manager.recover_stats(self.player_monitor.health,
                                                       self.player_monitor.mana,
                                                       self.player_monitor.spirit)
            if 99 < needed_restore < 200:
                restore_message = self.start_health_recovery(needed_restore)
            elif 200 <= needed_restore < 300:
                restore_message = self.start_mana_recovery(needed_restore)
            elif 300 <= needed_restore < 400:
                restore_message = self.start_spirit_recovery(needed_restore)
            # elif premium or channeling can be activated
            if len(restore_message) > 0:
                log_message += restore_message
                time.sleep(0.2)
            elif 0 < self.enemy_monitor.enemy_count < prev_enemy_num:
                self.item_master.open_item_tab()
                gem_color = Status.get_pixel_sum_color(self.item_master.item_cords.ibox_gem)
                log_message = log_message + self.item_master.get_gem(gem_color)
            else:
                message = special_attack(im, current_enemies, Settings.Player.style)
                log_message = log_message + message
            #this sleep function triggers the amount of time between clicks, thus the time between server communication
            #This function is very important, it randomizes the communication times, emulating the behavior of a player
            #sleep()
            logging.info(log_message)
            prev_enemy_num = len(current_enemies)
        return True

    def _round_init(self):
        self.item_master.open_item_tab()
        gem_color = Status.get_pixel_sum_color(self.item_master.item_cords.ibox_gem)
        self.item_master.get_gem(gem_color)
        Settings.pause = False

    def _round_refresh_and_cooldown(self):
        self.window_grabber.refresh_image()
        self.enemy_monitor.get_enemies(self.window_grabber.image)
        self.player_monitor.refresh_stats(self.window_grabber.image)
        self.item_master.cool_down_items()
        self.status_monitor.refresh_status(self.window_grabber.image)

    def start_health_recovery(self, restore_id):
        """
        if restore_id equals 100 and h potions are available, use potion
        if restore_id is less than or equal to 101 and cure is available, use cure
        if restore_id is less than or equal to 102 and regen is available, use regen
        else return empty string
        """
        if restore_id == 100 and self.item_master.h_available:
            self.item_master.use_item(self.item_master.next_h)
            self.item_master.next_h = None
            self.item_master.check_inventory()
            return "Health Pot Used"
        elif restore_id <= 101:  # and Cure is available (skill manager not implemented)
            # Use Cure (skill manager not implemented)
            return "Cure Used"
        elif restore_id <= 102:  # and Regen is available and not already used and isn't a premium skill (skill manager not implemented)
            # Use Regen (skill manager not implemented)
            return "Regen Used"
        else:
            return ""

    def start_mana_recovery(self, restore_id):
        if restore_id == 200 and self.item_master.m_available:
            self.item_master.use_item(self.item_master.next_m)
            self.item_master.next_m = None
            self.item_master.check_inventory()
            return "Mana Pot Used"
        else:
            return ""

    def start_spirit_recovery(self, restore_id):
        if restore_id == 200 and self.item_master.s_available:
            self.item_master.use_item(self.item_master.next_s)
            self.item_master.next_s = None
            self.item_master.check_inventory()
            return "Spirit Pot Used"
        else:
            return ""