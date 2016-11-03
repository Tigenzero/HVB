from PIL import ImageGrab, Image
import PIL
from logging import getLogger


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
        self.logger = getLogger('HVB.scanner')

    def _scan(self):
        """ Scans through image pixels, one by one, to find a color that may match a list of colors.
        :return: True/SystemError
        """
        x_scanner = self.x_scan/self.scan_size
        y_scanner = self.y_scan/self.scan_size
        for x_scan_num in xrange(0, self.scan_size):
            x_scan = x_scanner*x_scan_num
            for y_scan_num in xrange(0, self.scan_size):
                y_scan = y_scanner*y_scan_num
                if self._check_coordinates_for_targets(x_scan, y_scan):
                    return True
        raise SystemError("Scanner class was unable to find evidence of window. "
                          "Please reposition window or place window in another screen if using dual monitors")

    def _check_coordinates_for_targets(self, x_coord, y_coord):
        """Checks x,y coordinate for specific color within a list of target colors.
        :param x_coord: int x coordinate
        :param y_coord: int y coordinate
        :return: True/False if matches list of target colors
        """
        for target in self.scan_targets:
            try:
                color = self.image.getpixel((x_coord, y_coord))
                if len(color) > 3:
                    color = (color[0], color[1], color[2])
                #logging.info(color)
                if color == target:
                    self.found_x_coord = x_coord
                    self.found_y_coord = y_coord
                    return True
            except IndexError as e:
                self.logger.error("{},{} coordinates exceeded the scan index".format(x_coord, y_coord))
                raise IndexError(e)
        return False

    @classmethod
    def run(cls, x_scan, y_scan, scan_size, image, scan_targets):
        scanner = cls(x_scan, y_scan, scan_size, image, scan_targets)
        scanner.logger.info("Starting Scanner")
        scanner.logger.debug('x_scan: {}'.format(x_scan))
        scanner.logger.debug('y_scan: {}'.format(y_scan))
        scanner.logger.debug('scan_size: {}'.format(scan_size))
        scanner.logger.debug('scan_targets: {}'.format(scan_targets))
        scanner._scan()
        return scanner.found_x_coord, scanner.found_y_coord
