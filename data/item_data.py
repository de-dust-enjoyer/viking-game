from enum import Enum

# all items need a:
# name
# image (gets loaded in main)
# value
# category
# description
# rarity


# rarity:
#   common
#   uncommon
#   rare
#   epic
#   legendary
#   one-of-a-kind


class ItemType(Enum):
    WEAPON = "weapon"
    ARMOR = "armor"
    FOOD = "food"
    HOUSEHOLD = "household_items"
    RELIC = "relics"
    MISC = "misc"

    def __str__(self):
        return self.value


class Rarity(Enum):
    COMMON = "common"
    UNCOMMON = "uncommon"
    RARE = "rare"
    EPIC = "epic"
    LEGENDARY = "legendary"
    ONEOFAKIND = "one-of-a-kind"


rarity_color: dict = {
    Rarity.COMMON: (228, 231, 236),
    Rarity.UNCOMMON: (95, 187, 231),
    Rarity.RARE: (97, 55, 122),
    Rarity.EPIC: (89, 65, 146),
    Rarity.LEGENDARY: (223, 135, 0),
    Rarity.ONEOFAKIND: (221, 52, 57),
}

item_data = {
    # household items
    "wooden_spoon": {
        "name": "Wooden Spoon",
        "image": None,
        "image_outline": None,
        "image_alpha": None,
        "size": (2, 1),
        "value": 1,
        "category": ItemType.HOUSEHOLD,
        "description": "wooden spoon used for cooking.",
        "rarity": Rarity.COMMON,
        "stackable": True,
        "max_stack": 4,
    },
    "clay_jar": {
        "name": "Clay Jar",
        "image": None,
        "image_outline": None,
        "image_alpha": None,
        "size": (1, 1),
        "value": 3,
        "category": ItemType.HOUSEHOLD,
        "description": "clay jar for storing food",
        "rarity": Rarity.COMMON,
        "stackable": False,
        "max_stack": 1,
    },
    "wooden_plate": {
        "name": "Wooden Plate",
        "image": None,
        "image_outline": None,
        "image_alpha": None,
        "size": (2, 2),
        "value": 1,
        "category": ItemType.HOUSEHOLD,
        "description": "wooden plate to eat of",
        "rarity": Rarity.COMMON,
        "stackable": True,
        "max_stack": 4,
    },
    "wooden_cup": {
        "name": "Wooden Cup",
        "image": None,
        "image_outline": None,
        "image_alpha": None,
        "size": (1, 1),
        "value": 1,
        "category": ItemType.HOUSEHOLD,
        "description": "wooden cup to drink from",
        "rarity": Rarity.COMMON,
        "stackable": False,
        "max_stack": 1,
    },
    "clay_candlestick_holder": {
        "name": "Clay Candlestick Holder",
        "image": None,
        "image_outline": None,
        "image_alpha": None,
        "size": (1, 1),
        "value": 2,
        "category": ItemType.HOUSEHOLD,
        "description": "practical candlestick holder for ilumination.",
        "rarity": Rarity.COMMON,
        "stackable": False,
        "max_stack": 1,
    },
    "dirty_towels": {
        "name": "Dirty Towels",
        "image": None,
        "image_outline": None,
        "image_alpha": None,
        "size": (1, 1),
        "value": 1,
        "category": ItemType.HOUSEHOLD,
        "description": "basic towels made from linen.",
        "rarity": Rarity.COMMON,
        "stackable": True,
        "max_stack": 2,
    },
    "iron_chain_links": {
        "name": "Iron Chain Links",
        "image": None,
        "image_outline": None,
        "image_alpha": None,
        "size": (1, 1),
        "value": 3,
        "category": ItemType.HOUSEHOLD,
        "description": "iron chain links use for a lot of stuff.",
        "rarity": Rarity.COMMON,
        "stackable": True,
        "max_stack": 8,
    },
    "iron_pot": {
        "name": "Iron Pot",
        "image": None,
        "image_outline": None,
        "image_alpha": None,
        "size": (2, 2),
        "value": 6,
        "category": ItemType.HOUSEHOLD,
        "description": "cooking pot made from iron.",
        "rarity": Rarity.COMMON,
        "stackable": False,
        "max_stack": 1,
    },
    "iron_kitchen_knife": {
        "name": "Iron Kitchen Knife",
        "image": None,
        "image_outline": None,
        "image_alpha": None,
        "size": (2, 1),
        "value": 9,
        "category": ItemType.HOUSEHOLD,
        "description": "sharp knife to cut food, or foes . . .",
        "rarity": Rarity.UNCOMMON,
        "stackable": False,
        "max_stack": 1,
    },
    "salt": {
        "name": "Salt",
        "image": None,
        "image_outline": None,
        "image_alpha": None,
        "size": (1, 1),
        "value": 9,
        "category": ItemType.HOUSEHOLD,
        "description": "salty . . .",
        "rarity": Rarity.UNCOMMON,
        "stackable": True,
        "max_stack": 8,
    },
    "iron_lantern": {
        "name": "Iron Lantern",
        "image": None,
        "image_outline": None,
        "image_alpha": None,
        "size": (1, 2),
        "value": 8,
        "category": ItemType.HOUSEHOLD,
        "description": "for making the dark go away.",
        "rarity": Rarity.UNCOMMON,
        "stackable": False,
        "max_stack": 1,
    },
    "silver_candlestick_holder": {
        "name": "Silver Candlestick Holder",
        "image": None,
        "image_outline": None,
        "image_alpha": None,
        "size": (1, 1),
        "value": 23,
        "category": ItemType.HOUSEHOLD,
        "description": "decorative candlestick holder for ilumination.",
        "rarity": Rarity.RARE,
        "stackable": False,
        "max_stack": 1,
    },
    "gold_candlestick_holder": {
        "name": "Gold Candlestick Holder",
        "image": None,
        "image_outline": None,
        "image_alpha": None,
        "size": (1, 1),
        "value": 2,
        "category": ItemType.HOUSEHOLD,
        "description": "luxury candlestick holder for ilumination.",
        "rarity": Rarity.LEGENDARY,
        "stackable": False,
        "max_stack": 1,
    },
}
