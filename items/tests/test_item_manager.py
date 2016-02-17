from items import item_manager
import logging

PLAYER_ITEMS = [0, 0, 0, 1, 1, 2, 2, 9, 9, 9, 9, 9, 9, 9, 9, 9]


def test_item_manager_init():
    item_manager.ItemManager(PLAYER_ITEMS)


def test_item_manager_get_items():
    item_master = item_manager.ItemManager(PLAYER_ITEMS)
    item_master.get_items()
    count = 0
    for item in item_master.items:
        logging.debug("{} is equal to {}?".format(item.type, PLAYER_ITEMS[count]))
        assert(item.type == PLAYER_ITEMS[count])
        count += 1


def test_item_manager_item_cooldown():
    item_master = item_manager.ItemManager(PLAYER_ITEMS)
    item_master.get_items()
    item_master.cool_down_items()