from user_interface.coordinates import EnemyCords


class EnemyMonitor(object):
    def __init__(self):
        self.coordinates = EnemyCords()
        self.current_enemies = []
        self.enemy_count = 0

    def get_enemies(self, image):
        current_enemies = []
        for enemy in self.coordinates.enemies:
            pixel = image.getpixel(enemy)
            if len(pixel) > 3:
                pixel = (pixel[0], pixel[1], pixel[2])
            if pixel == self.coordinates.over_color \
                    or pixel == self.coordinates.under_color:
                current_enemies.append(self.coordinates.enemy_press(enemy))
        self.current_enemies = current_enemies
        self.enemy_count = len(current_enemies)
