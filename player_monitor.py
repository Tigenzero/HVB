from Coordinates import PlayerCords


class PlayerMonitor(object):
    def __init__(self):
        self.health = 100
        self.mana = 100
        self.spirit = 100
        self.player_coordinates = PlayerCords()
        self.is_dead = False

    def _get_health(self, image):
        p_health = 0
        for level in self.player_coordinates.p_health_levels:
            if image.getpixel(level) != self.player_coordinates.under_color:
                p_health += 10
            else:
                return p_health
        return 100

    def _get_mana(self, image):
        p_mana = 0
        for level in self.player_coordinates.p_mana_levels:
            if image.getpixel(level) != self.player_coordinates.under_color:
                p_mana += 10
            else:
                return p_mana
        return 100

    def _get_overcharge(self, image):
        p_overcharge = 0
        for level in self.player_coordinates.p_overcharge_levels:
            if image.getpixel(level) != self.player_coordinates.under_color:
                p_overcharge += 10
            else:
                return p_overcharge
        return 100

    def _get_spirit(self, image):
        p_spirit = 0
        for level in self.player_coordinates.p_spirit_levels:
            if image.getpixel(level) != self.player_coordinates.under_color:
                p_spirit += 10
            else:
                return p_spirit
        return 100

    def _is_player_dead(self):
        if self.health == 0:
            self.is_dead = True
        else:
            self.is_dead = False

    def refresh_stats(self, image):
        self._get_health(image)
        self._get_mana(image)
        self._get_spirit(image)
        self._is_player_dead()

