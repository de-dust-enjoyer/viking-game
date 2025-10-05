import random, os
from typing import Optional


def list_from_dir(folder_path: str, includes: Optional[str] = None):
    folder_list = os.listdir(folder_path)
    if includes is None:
        return folder_list
    filtered_list = []
    for element in folder_list:
        if includes in element:
            filtered_list.append(element)

    return filtered_list


def list_from_dir_args(folder_path: str, *args):
    """*args: strings that the desired items must include (or operation)
    this function does not keep the order of the folders"""
    filtered_list = []
    for arg in args:
        filtered_list.extend(list_from_dir(folder_path, arg))
    return list(set(filtered_list))


possible_appearances = {
    "viking": {
        "base": list_from_dir("assets/sprites/units/base/"),
        "accessories": list_from_dir("assets/sprites/units/accessories/", "none"),
        "chest": list_from_dir("assets/sprites/units/chest/", "og_shirt"),
        "feet": list_from_dir("assets/sprites/units/feet/"),
        "hands": list_from_dir("assets/sprites/units/hands/"),
        "head": list_from_dir_args("assets/sprites/units/head/", "ginger", "blonde", "no_hair"),
        "legs": list_from_dir("assets/sprites/units/legs/", "og_pants"),
    },
    "soldier": {
        "base": list_from_dir("assets/sprites/units/base/"),
        "accessories": list_from_dir("assets/sprites/units/accessories/", "none"),
        "chest": list_from_dir("assets/sprites/units/chest/", "royal_shirt"),
        "feet": list_from_dir("assets/sprites/units/feet/"),
        "hands": list_from_dir("assets/sprites/units/hands/"),
        "head": list_from_dir_args("assets/sprites/units/head/", "black", "blonde", "grey", "brown", "no_hair"),
        "legs": list_from_dir("assets/sprites/units/legs/", "royal_pants"),
    },
    "civilian": {
        "base": list_from_dir("assets/sprites/units/base/"),
        "accessories": list_from_dir_args("assets/sprites/units/accessories/", "farmer_hat", "none"),
        "chest": list_from_dir_args("assets/sprites/units/chest/", "farmer_shirt", "lumberjack_shirt"),
        "feet": list_from_dir("assets/sprites/units/feet/"),
        "hands": list_from_dir("assets/sprites/units/hands/"),
        "head": list_from_dir_args("assets/sprites/units/head/", "black", "blonde", "grey", "brown", "no_hair"),
        "legs": list_from_dir("assets/sprites/units/legs/", "farmer_pants"),
    },
}


def get_random_appearance(type: str) -> dict:
    appearance = {
        "base": random.choice(possible_appearances[type]["base"]),
        "accessories": random.choice(possible_appearances[type]["accessories"]),
        "chest": random.choice(possible_appearances[type]["chest"]),
        "feet": random.choice(possible_appearances[type]["feet"]),
        "hands": random.choice(possible_appearances[type]["hands"]),
        "head": random.choice(possible_appearances[type]["head"]),
        "legs": random.choice(possible_appearances[type]["legs"]),
    }
    return appearance


print(get_random_appearance("civilian"))
