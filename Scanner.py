from PIL import ImageGrab, Image
import PIL
import logging


class Scanner(object):
    """
    Scans an image for a certain pixel color. Once found, it returns the x and y.
    """
    def __init__(self, x_scan, y_scan, scan_size, image, scan_targets):
        self.x_scan = x_scan
        self.y_scan = y_scan
        self.scan_size = scan_size
        self.image = image
        self.scan_targets = scan_targets
        self.found_x_coord = None
        self.found_y_coord = None

    def _scan(self):
        x_scanner = self.x_scan/self.scan_size
        y_scanner = self.y_scan/self.scan_size
        for x_scan_num in range(0, self.scan_size):
            x_scan = x_scanner*x_scan_num
            for y_scan_num in range(0, self.scan_size):
                y_scan = y_scanner*y_scan_num
                if self._check_coordinates_for_targets(x_scan, y_scan):
                    return True
        raise SystemError("Scanner class was unable to find evidence of window. "
                          "Please reposition window or place window in another screen if using dual monitors")

    def _check_coordinates_for_targets(self, x_coord, y_coord):
        for target in self.scan_targets:
            color = self.image.getpixel((x_coord, y_coord))
            if len(color) > 3:
                color = (color[0], color[1], color[2])
            #logging.info(color)
            if color == target:
                self.found_x_coord = x_coord
                self.found_y_coord = y_coord
                return True
        return False

    @classmethod
    def run(cls, x_scan, y_scan, scan_size, image, scan_targets):
        scanner = cls(x_scan, y_scan, scan_size, image, scan_targets)
        scanner._scan()
        return scanner.found_x_coord, scanner.found_y_coord
