from Coordinates import EnemyCords


class EnemyMonitor(object):
    def __init__(self):
        self.coordinates = EnemyCords()
        self.current_enemies = []
        self.enemy_count = 0

    def get_enemies(self, image):
        current_enemies = []
        for enemy in self.coordinates.enemies:
            if image.getpixel(enemy) == self.coordinates.over_color \
                    or image.getpixel(enemy) == self.coordinates.under_color:
                current_enemies.append(enemy)
        self.current_enemies = current_enemies
        self.enemy_count = len(current_enemies)
