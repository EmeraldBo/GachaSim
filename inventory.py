from char_list import common_char

inventory = {
    "Mythic": {
        "Hyfriz Prime": False,
        "Chrono Warden": False,
        "Temporal Chimer": False,
        "Flame Knight Ketsueki": False,
        "White Fury Keith": False,
        "Black Rage Sah": False,
        "John Dick": False
    },
    
    "Legendary": {
        "Chimer": False,
        "Ketsueki": False,
        "Keith": False,
        "Sah": False,
        "Lyra": False,
        "The Carlo": False,
        "Nell": False,
        "Pixel": True
    },
    
    "Epic": {
        "CheeseConsumer": False,
        "Kito": False,
        "Genshi": False,
        "Carlo": False,
        "Setsuna": False,
        "Midori": False,
        "Novi": False,
        "Moshomi": False,
        "Mushy": False,
        "Martis": False,
        "Reyna": False,
        "Chambler": True,
        "Watermelon": True
    },
    
    "Common": {char: [False, 0] for char in common_char}
}

inventory_items = {
    "Plushies": {
        "Chimer Plushie": True,
        "Ketsueki Plushie": False,
        "Keith Plushie": False,
        "Sah Plushie": False,
        "Carlo Plushie": False
    },
    "Tokens": {
        "Bronze Token": False,
        "Silver Token": False,
        "Gold Token": False,
        "Diamond Token": False
    }
}

def total_luck(inventory_items, shop):
    total = sum(shop["Plushies"][item][1] for item, owned in inventory_items["Plushies"].items() if owned)
    return total

def total_cd(inventory_items, shop):
    total = sum(shop["Tokens"][item][1] for item, owned in inventory_items["Tokens"].items() if owned)
    return total

def mythic_counter():
    return sum(1 for obtained in inventory["Mythic"].values() if obtained)

def leg_counter():
    return sum(1 for obtained in inventory["Legendary"].values() if obtained)

def epic_counter():
    return sum(1 for obtained in inventory["Epic"].values() if obtained)

def obtain_char(char):
    if char in inventory["Mythic"]:
        inventory["Mythic"][char] = True
    elif char in inventory["Legendary"]:
        inventory["Legendary"][char] = True
    elif char in inventory["Epic"]:
        inventory["Epic"][char] = True
    elif char in inventory["Common"]:
        is_owned, count = inventory["Common"][char]
        inventory["Common"][char] = (True, count + 1)  # Replace with a new tuple
def show_inventory():
    print("/////Characters/////")
    for rarity in ["Mythic", "Legendary", "Epic"]:
        print(f"~~~~~{rarity}~~~~~")
        obtained_chars = [char for char, obtained in inventory[rarity].items() if obtained]
        if obtained_chars:
            for char in obtained_chars:
                print(f"- {char}")
        else:
            print("Empty")
    
    print("~~~~~Common~~~~~")
    obtained_common = [f"- {char} ({data[1]})" for char, data in inventory["Common"].items() if data[0]]
    print("\n".join(obtained_common) if obtained_common else "Empty")
    
    print("\n/////Items/////")
    for category in ["Plushies", "Tokens"]:
        print(f"~~~~~{category}~~~~~")
        obtained_items = [f"- {item}" for item, obtained in inventory_items[category].items() if obtained]
        print("\n".join(obtained_items) if obtained_items else "Empty")

def reset_inventory():
    for rarity in inventory:
        if rarity == "Common":
            for char in inventory[rarity]:
                inventory[rarity][char] = [False, 0]  # Reset count for Common characters
        else:
            for char in inventory[rarity]:
                inventory[rarity][char] = False  # Reset for Epic and Legendary

    for category in inventory_items:
        for item in inventory_items[category]:
            inventory_items[category][item] = False

def reset_com_epic():
    for item in inventory["Epic"]:
        inventory["Epic"][item] = False
    for item in inventory["Common"]:
        inventory["Common"][item] = [False, 0]