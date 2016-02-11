import time
import logging

import pony_watcher
import player_monitor
import enemy_monitor
import item_manager
import click_press
from skill import skill_manager
from Settings.player_config import PlayerConfig
import etc_manager
from status import status_monitor
from window_finder import find_window


class MasterControl(object):
    def __init__(self, mode=0):
        self.window_grabber = find_window.ScreenGrabber.get_window()
        self.p_watcher = pony_watcher.PonyWatcher()
        self.player_monitor = player_monitor.PlayerMonitor()
        self.enemy_monitor = enemy_monitor.EnemyMonitor()
        self.item_master = item_manager.ItemManager()
        self.player = PlayerConfig.get_player_0()
        skill_list = skill_manager.SkillGenerator.generate_skills(self.player.skills,
                                                                  self.player.premium,
                                                                  self.player.special_attack)
        self.skill_master = skill_manager.SkillMaster(skill_list)
        self.status_monitor = status_monitor.StatusMonitor()
        self.mode = mode
        #image_initialize.get_images()
        self.item_master.get_items()
        self.pause = False

    def start(self):
        logging.info("Master Control starting")
        if len(self.player.skills[0]) <= 1:
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
            if self.pause:
                return False
            self._round_refresh_and_cooldown()
            if self.window_grabber.image.getpixel((42, 710)) not in find_window.WINDOW_COLORS:
                continue
            current_enemies = self.enemy_monitor.current_enemies
            log_message = "{},{},{},{},".format(self.enemy_monitor.enemy_count, self.player_monitor.health,
                                                self.player_monitor.mana, self.player_monitor.spirit)
            restore_message = self.restore_player()
            if restore_message is not None:
                log_message += restore_message
                time.sleep(0.2)
            elif 0 < self.enemy_monitor.enemy_count < prev_enemy_num:
                gem_message = self.check_gem_color()
                log_message = log_message + gem_message
            else:
                message = special_attack(im, current_enemies, self.player.style)
                log_message = log_message + message
            #this sleep function triggers the amount of time between clicks, thus the time between server communication
            #This function is very important, it randomizes the communication times, emulating the behavior of a player
            #sleep()
            logging.info(log_message)
            prev_enemy_num = len(current_enemies)
        return True

    def _round_init(self):
        self.check_gem_color()
        self.pause = False

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
        elif restore_id <= 101 and self.skill_master.get_skill("Cure").active:
            self.skill_master.use_skill("Cure")
            return "Cure Used"
        elif restore_id <= 102 and self.skill_master.get_skill("Regen").active and not self.skill_master.get_skill("Regen").premium\
                and "Regen" not in self.status_monitor.current_status:
            self.skill_master.use_skill("Regen")
            return "Regen Used"
        else:
            return None

    def start_mana_recovery(self, restore_id):
        if restore_id == 200 and self.item_master.m_available:
            self.item_master.use_item(self.item_master.next_m)
            self.item_master.next_m = None
            self.item_master.check_inventory()
            return "Mana Pot Used"
        else:
            return None

    def start_spirit_recovery(self, restore_id):
        if restore_id == 200 and self.item_master.s_available:
            self.item_master.use_item(self.item_master.next_s)
            self.item_master.next_s = None
            self.item_master.check_inventory()
            return "Spirit Pot Used"
        else:
            return None

    def activate_premium(self):
        for premium in self.player.premium:
            if not self.status_monitor.is_status_active(premium):
                self.skill_master.use_skill(premium)
                return "Premium Skill Activated: {}".format(premium)
        return None

    def restore_player(self):
        need_restore = etc_manager.recover_stats(self.player_monitor.health,
                                                 self.player_monitor.mana,
                                                 self.player_monitor.spirit)
        restore_message = None
        if 99 < need_restore < 200:
            restore_message = self.start_health_recovery(need_restore)
        elif 200 <= need_restore < 300:
            restore_message = self.start_mana_recovery(need_restore)
        elif 300 <= need_restore < 400:
            restore_message = self.start_spirit_recovery(need_restore)
        elif self.status_monitor.is_status_active("Channeling"):
            restore_message = self.activate_premium()
        elif self.item_master.current_gem == 3:
            self.item_master.activate_gem()
            restore_message = "Channeling Gem Activated"
        return restore_message

    def check_gem_color(self):
        self.item_master.open_item_tab()
        self.window_grabber.refresh_image()
        gem_color = etc_manager.get_pixel_sum_color(self.window_grabber.image, self.item_master.item_cords.ibox_gem)
        self.item_master.close_item_tab()
        return self.item_master.get_gem(gem_color)