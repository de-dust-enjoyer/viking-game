from enum import Enum
import random

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
    HOUSEHOLD = "household"
    RESOURCE = "resource"
    VALUABLE = "valuable"
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
    Rarity.COMMON: (194, 177, 169),
    Rarity.UNCOMMON: (112, 148, 255),
    Rarity.RARE: (165, 91, 232),
    Rarity.EPIC: (204, 47, 65),
    Rarity.LEGENDARY: (233, 149, 7),
    Rarity.ONEOFAKIND: (249, 199, 255),
}


def generate_loot(category: ItemType, value: int, luck: int):
    if not item_data_sorted.keys():
        sort_item_data()
    if category not in item_data_sorted:
        return []

    rarity_weight = [50 - luck, 30 - luck // 2, 10, 4, 1, 0]
    data = item_data_sorted[category]
    budget = random.randrange((value - value // 4) + luck, (value + value // 4) + luck)
    items = []
    commons = 0
    uncommons = 0
    rares = 0
    epics = 0
    legendarys = 0
    worth = 0
    while budget > 0:
        item_selected = False
        while not item_selected:
            rarity = random.choices(list(Rarity._member_map_.values()), rarity_weight)[0]
            if not data[rarity]:  # if no items are from this rarity loop again
                continue

            if rarity == Rarity.COMMON:
                commons += 1
            elif rarity == Rarity.UNCOMMON:
                uncommons += 1
            elif rarity == Rarity.RARE:
                rares += 1
            elif rarity == Rarity.EPIC:
                epics += 1
            elif rarity == Rarity.LEGENDARY:
                legendarys += 1

            item = random.choice(list(data[rarity].keys()))
            items.append(item)
            item_selected = True

            budget -= item_data[item]["value"]
            worth += item_data[item]["value"]

    print(rarity_weight)
    print(f"commons {commons}")
    print(f"uncommons {uncommons}")
    print(f"rares {rares}")
    print(f"epics {epics}")
    print(f"legendarys {legendarys}")
    print(f"num items {len(items)}")
    print(f"total worth {worth}")

    return items


def sort_item_data():
    global item_data_sorted
    data = {}
    categorys = []
    raritys = []
    for item_id, item_attr in item_data.items():
        if item_attr["category"] not in categorys:
            categorys.append(item_attr["category"])
        if item_attr["rarity"] not in raritys:
            raritys.append(item_attr["rarity"])
    for category in categorys:
        data[category] = {}
        for rarity in raritys:
            data[category][rarity] = {}
    for item_id, item_attr in item_data.items():
        data[item_attr["category"]][item_attr["rarity"]][item_id] = item_attr
    item_data_sorted = data
    print("SORTED ITEM DATA CREATED!!!")


item_data_sorted = {}

item_data = {
    # horns (there will be a lot of them) # horns horns horns horns horns horns horns horns horns horns horns horns horns horns horns horns horns
    "drinking_horn_01": {
        "name": "Drinking Horn",
        "image": None,
        "image_outline": None,
        "image_alpha": None,
        "size": (1, 2),
        "value": 1,
        "weight": 0.5,
        "category": ItemType.HOUSEHOLD,
        "description": "horn to drink from. gulp.",
        "rarity": Rarity.LEGENDARY,
        "stackable": False,
        "max_stack": 1,
    },
    # household household household household household household household household household household household household household household
    "wooden_spoon": {
        "name": "Wooden Spoon",
        "image": None,
        "image_outline": None,
        "image_alpha": None,
        "size": (2, 1),
        "value": 1,
        "weight": 0.05,
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
        "weight": 0.3,
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
        "value": 2,
        "weight": 0.1,
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
        "value": 3,
        "weight": 0.05,
        "category": ItemType.HOUSEHOLD,
        "description": "wooden cup to drink from",
        "rarity": Rarity.COMMON,
        "stackable": False,
        "max_stack": 1,
    },
    "silver_cup": {
        "name": "Silver Cup",
        "image": None,
        "image_outline": None,
        "image_alpha": None,
        "size": (1, 1),
        "value": 23,
        "weight": 0.5,
        "category": ItemType.HOUSEHOLD,
        "description": "silver cup to drink from",
        "rarity": Rarity.RARE,
        "stackable": False,
        "max_stack": 1,
    },
    "gold_cup": {
        "name": "Gold Cup",
        "image": None,
        "image_outline": None,
        "image_alpha": None,
        "size": (1, 1),
        "value": 58,
        "weight": 1,
        "category": ItemType.HOUSEHOLD,
        "description": "wooden cup to drink from",
        "rarity": Rarity.EPIC,
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
        "weight": 0.5,
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
        "weight": 0.02,
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
        "weight": 0.5,
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
        "weight": 2,
        "category": ItemType.HOUSEHOLD,
        "description": "cooking pot made from iron.",
        "rarity": Rarity.COMMON,
        "stackable": False,
        "max_stack": 1,
    },
    "small_knife": {
        "name": "Small Knife",
        "image": None,
        "image_outline": None,
        "image_alpha": None,
        "size": (1, 1),
        "value": 4,
        "weight": 0.3,
        "category": ItemType.HOUSEHOLD,
        "description": "for cutting stuff lol.",
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
        "weight": 1.5,
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
        "weight": 0.5,
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
        "weight": 2,
        "category": ItemType.HOUSEHOLD,
        "description": "for making the dark go away.",
        "rarity": Rarity.UNCOMMON,
        "stackable": False,
        "max_stack": 1,
    },
    "glass_pouch_bottle": {
        "name": "Glass Pouch Bottle",
        "image": None,
        "image_outline": None,
        "image_alpha": None,
        "size": (1, 2),
        "value": 1,
        "weight": 0.5,
        "category": ItemType.HOUSEHOLD,
        "description": "primitive glass bottle to store liquids",
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
        "weight": 0.5,
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
        "value": 57,
        "weight": 1,
        "category": ItemType.HOUSEHOLD,
        "description": "luxury candlestick holder for ilumination.",
        "rarity": Rarity.LEGENDARY,
        "stackable": False,
        "max_stack": 1,
    },
    # valubles valubles valubles valubles valubles valubles valubles valubles valubles valubles valubles valubles valubles valubles valubles valubles
    "silver_ring": {
        "name": "Silver Ring",
        "image": None,
        "image_outline": None,
        "image_alpha": None,
        "size": (1, 1),
        "value": 42,
        "weight": 0.01,
        "category": ItemType.VALUABLE,
        "description": "small silver finger ring.",
        "rarity": Rarity.RARE,
        "stackable": False,
        "max_stack": 1,
    },
    "silver_ring_amethist": {
        "name": "Silver Ring with Amethist",
        "image": None,
        "image_outline": None,
        "image_alpha": None,
        "size": (1, 1),
        "value": 62,
        "weight": 0.01,
        "category": ItemType.VALUABLE,
        "description": "small silver finger ring with Amethist stone.",
        "rarity": Rarity.EPIC,
        "stackable": False,
        "max_stack": 1,
    },
    "silver_ring_saffire": {
        "name": "Silver Ring with Saffire",
        "image": None,
        "image_outline": None,
        "image_alpha": None,
        "size": (1, 1),
        "value": 71,
        "weight": 0.01,
        "category": ItemType.VALUABLE,
        "description": "small silver finger ring with Saffire stone.",
        "rarity": Rarity.EPIC,
        "stackable": False,
        "max_stack": 1,
    },
    "silver_ring_ruby": {
        "name": "Silver Ring with Ruby",
        "image": None,
        "image_outline": None,
        "image_alpha": None,
        "size": (1, 1),
        "value": 75,
        "weight": 0.01,
        "category": ItemType.VALUABLE,
        "description": "small silver finger ring with Ruby stone.",
        "rarity": Rarity.EPIC,
        "stackable": False,
        "max_stack": 1,
    },
    "gold_ring": {
        "name": "Gold Ring",
        "image": None,
        "image_outline": None,
        "image_alpha": None,
        "size": (1, 1),
        "value": 74,
        "weight": 0.01,
        "category": ItemType.VALUABLE,
        "description": "small gold finger ring.",
        "rarity": Rarity.EPIC,
        "stackable": False,
        "max_stack": 1,
    },
    "gold_ring_amethist": {
        "name": "Gold Ring with Amethist",
        "image": None,
        "image_outline": None,
        "image_alpha": None,
        "size": (1, 1),
        "value": 87,
        "weight": 0.01,
        "category": ItemType.VALUABLE,
        "description": "small gold finger ring with Amethist Stone.",
        "rarity": Rarity.EPIC,
        "stackable": False,
        "max_stack": 1,
    },
    "gold_ring_ruby": {
        "name": "Gold Ring with Ruby",
        "image": None,
        "image_outline": None,
        "image_alpha": None,
        "size": (1, 1),
        "value": 92,
        "weight": 0.01,
        "category": ItemType.VALUABLE,
        "description": "small gold finger ring with Ruby Stone.",
        "rarity": Rarity.EPIC,
        "stackable": False,
        "max_stack": 1,
    },
    "gold_ring_saffire": {
        "name": "Gold Ring with Saffire",
        "image": None,
        "image_outline": None,
        "image_alpha": None,
        "size": (1, 1),
        "value": 90,
        "weight": 0.01,
        "category": ItemType.VALUABLE,
        "description": "small gold finger ring with Saffire Stone.",
        "rarity": Rarity.EPIC,
        "stackable": False,
        "max_stack": 1,
    },
    "gold_ring_diamand": {
        "name": "Gold Ring with Diamand",
        "image": None,
        "image_outline": None,
        "image_alpha": None,
        "size": (1, 1),
        "value": 120,
        "weight": 0.01,
        "category": ItemType.VALUABLE,
        "description": "small gold finger ring with Diamand Stone.",
        "rarity": Rarity.LEGENDARY,
        "stackable": False,
        "max_stack": 1,
    },
    "silver_bracelet": {
        "name": "Silver Bracelet",
        "image": None,
        "image_outline": None,
        "image_alpha": None,
        "size": (1, 1),
        "value": 51,
        "weight": 0.05,
        "category": ItemType.VALUABLE,
        "description": "beautyfull silver bracelet.",
        "rarity": Rarity.RARE,
        "stackable": False,
        "max_stack": 1,
    },
    "gold_bracelet": {
        "name": "Gold Bracelet",
        "image": None,
        "image_outline": None,
        "image_alpha": None,
        "size": (1, 1),
        "value": 81,
        "weight": 0.05,
        "category": ItemType.VALUABLE,
        "description": "beautyfull gold bracelet.",
        "rarity": Rarity.EPIC,
        "stackable": False,
        "max_stack": 1,
    },
    "log": {
        "name": "Wood Log",
        "image": None,
        "image_outline": None,
        "image_alpha": None,
        "size": (4, 1),
        "value": 1,
        "weight": 4,
        "category": ItemType.RESOURCE,
        "description": "Wooden log. Good for building stuff.",
        "rarity": Rarity.COMMON,
        "stackable": True,
        "max_stack": 4,
    },
    "board": {
        "name": "Wood Board",
        "image": None,
        "image_outline": None,
        "image_alpha": None,
        "size": (4, 1),
        "value": 2,
        "weight": 1,
        "category": ItemType.RESOURCE,
        "description": "cut wooden log.",
        "rarity": Rarity.COMMON,
        "stackable": True,
        "max_stack": 12,
    },
}
