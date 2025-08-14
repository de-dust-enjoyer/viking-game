import random

viking_attributes = {
    "positive": # -----------------------------------
{    
    "Warrior Father": 
        {"damage": 2},
    "Well Trained": 
        {"damage": 2, "defense": 2},
    "Battle Hardened": 
        {"damage": 3, "defence": 5},
    "Professional Soldier": 
        {"damage": 6, "defense": 8},
    "Thick Skin": 
        {"defense": 6}
},

    "negative": # -----------------------------------
{
    "Deathwish":
        {"defense": -10},
    "Fearfull": 
        {"damage": -5, "defense": 3},
    "Weakling":
        {"damage": -2, "defense": -3},

},

    "mixed": # --------------------------------------
{
    "Aggressive": {"damage": 5, "defense": -4},
    "Berserker": {"damage": 9, "defense": -8},
    "Defensive": {"damage": -2, "defense": 5}
},

}

viking_attribute_info = {
    "Warrior Father": "my Father was a great Warrior. He trained me well ... when he was home that is.",
    "Well Trained": "i enjoyed good training in my home village.",
    "Battle Hardened": "i have proven myself on the battlefield coutless times.",
    "Professional Soldier": "i was trained by the best instructors in the kings army.",
    "Thick Skin": "My skin has stopped various Blades",
    "Deathwish": "I cannot wait to feast with the Gods in Vallhalla.",
    "Fearfull": "Ahh, dont scare me like that!",
    "Weakling": "I am not the strongest but i can make up for it with my technique.",
    "Aggressive": "Why are you looking at me?. Do you have a Problem?!",
    "Berserker": "MURDEEER, KILL AAAARRRRRRRRGGGGG",
    "Defensive": "I like my shield more than my Axe",
}

english_attributes = {
    "positive": # -----------------------------------
{    
    "Soldier Father": 
        {"damage": 2},
    "Well Trained": 
        {"damage": 2, "defense": 2},
    "Battle Hardened": 
        {"damage": 3, "defence": 5},
    "Professional Soldier": 
        {"damage": 6, "defense": 8},
    "Thick Skin": 
        {"defense": 6}
},

    "negative": # -----------------------------------
{
    "Deathwish":
        {"defense": -10},
    "Fearfull": 
        {"damage": -5, "defense": 3},
    "Weakling":
        {"damage": -2, "defense": -3},

},

    "mixed": # --------------------------------------
{
    "Tempered": {"damage": 5, "defense": -4},
    "Aggressive": {"damage": 9, "defense": -8},
    "Defensive": {"damage": -2, "defense": 5}
}
}
english_attribute_info = {
    "Soldier Father": "my Father was a great Fighter. He trained me well ... when he was home that is.",
    "Well Trained": "i enjoyed good training in my home twon.",
    "Battle Hardened": "i have proven myself on the battlefield coutless times.",
    "Professional Soldier": "i was trained by the best instructors in the kings army.",
    "Thick Skin": "My skin has stopped various Blades",
    "Deathwish": "i will die for my Homeland.",
    "Fearfull": "Ahh, dont scare me like that!",
    "Weakling": "I am not the strongest but i can make up for it with my technique.",
    "Aggressive": "AAAGGGGEERERERERERER",
    "Tempered": "Why are you looking at me?. Do you have a Problem?!",
    "Defensive": "I like my shield more than my Sword",
}



def get_random_attributes(attr_list:dict, type:str="viking") -> dict:
    # get the number of attributes for each category -> weighted
    attr_weights =   [2, 7, 1]
    num_pos_attr = random.choices([0, 1, 2], attr_weights, k=1)[0]
    attr_weights = [7, 3]
    num_neg_attr = random.choices([0, 1], attr_weights, k=1)[0]
    attr_weights = [9, 1]
    num_mix_attr = random.choices([0, 1], attr_weights, k=1)[0]
    # dict with the number of attributes of each category
    num_attr = {"positive": num_pos_attr, "negative": num_neg_attr, "mixed": num_mix_attr}
    possible_attr_dict = attr_list.copy()
    attr_dict = {}
    for category in possible_attr_dict:
        attr_dict[category] = {}
        for i in range(num_attr[category]):

            random_attr = random.choice(list(attr_list[category].keys()))

            attr_dict[category][random_attr] = possible_attr_dict[category][random_attr]
            # possible_attributes[category].pop(random_attr) # this makes it impossible to have duplicate atributes

    return attr_dict


