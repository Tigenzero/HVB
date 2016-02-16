import os
import logging

from PIL import Image

from status import image_initialize
from status.status_monitor import StatusMonitor


TEST_IMAGE = Image.open(os.path.join("data", "test_HV_window.png")).convert("RGB")
SPARK_LIFE = 15707
STATUS_LIST = ["Spark_Life", "Spirit_Shield", "Haste", "Shadow_Veil", "Protection"]

def test_status_status_monitor_init():
    StatusMonitor()


def test_status_status_monitor_get_status_sum():
    status_monitor = StatusMonitor()
    status_sum = status_monitor._get_status_sum(TEST_IMAGE, status_monitor.status_coordinates.status_locs[0])
    logging.debug(status_sum)
    assert(status_sum == SPARK_LIFE)


def test_status_status_monitor_lookup_status_not_none():
    status_monitor = StatusMonitor()
    status_result = status_monitor._lookup_status(SPARK_LIFE)
    image_initialize.print_collection(status_monitor.status_collection)
    logging.debug(status_result)
    assert(status_result == "Spark_Life")


def test_status_status_monitor_lookup_status_none():
    status_monitor = StatusMonitor()
    status_result = status_monitor._lookup_status(0)
    assert(status_result is None)


def test_status_status_monitor_update_status():
    status_monitor = StatusMonitor()
    status_monitor.refresh_status(TEST_IMAGE)
    logging.debug(status_monitor.current_status)
    assert(status_monitor.current_status == STATUS_LIST)


def test_status_status_monitor_is_status_active():
    status_monitor = StatusMonitor()
    status_monitor.refresh_status(TEST_IMAGE)
    is_active = status_monitor.is_status_active("Haste")
    assert is_active