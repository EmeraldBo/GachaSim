import inventory as inv

bonds_stats = { 
    "Burning Clock": [False, 10, 5],
    "Frozen Time": [False, 5, 7],
    "Guardians": [False, 8, 7],
    "Past's Servants": [False, 7, 7],
    "Interversal Cameo": [False, 3, 7],
    "Yin and Yang": [False, 3, 7],
    "Furries": [False, 5, 5]
}

# Bonds Function
def check_bonds(inv, bonds):
    """
    Checks if certain combinations of characters exist in the inventory.
    If true, updates the corresponding bond status and prints a message only once.
    """
    if inv.get("Legendary", {}).get("Chimer") and inv["Legendary"].get("Ketsueki"):
        if not bonds.setdefault("Burning Clock", [False])[0]:  # Check if bond is already False
            bonds["Burning Clock"][0] = True
            print("Burning Clock activated!")

    if inv.get("Legendary", {}).get("Chimer") and inv["Legendary"].get("Nell"):
        if not bonds.setdefault("Frozen Time", [False])[0]:
            bonds["Frozen Time"][0] = True
            print("Frozen Time activated!")

    if (inv.get("Legendary", {}).get("Chimer") and inv["Legendary"].get("Ketsueki") and
        inv["Legendary"].get("Keith") and inv["Legendary"].get("Sah") and inv["Legendary"].get("Lyra")):
        if not bonds.setdefault("Guardians", [False])[0]:
            bonds["Guardians"][0] = True
            print("Guardians activated!")

    if (inv.get("Legendary", {}).get("Hyfriz") and 
        inv.get("Epic", {}).get("Fegelein") and inv["Epic"].get("Umbra")):
        if not bonds.setdefault("Past's Servants", [False])[0]:
            bonds["Past's Servants"][0] = True
            print("Past's Servants activated!")

    if inv.get("Epic", {}).get("Baron Jager") and inv["Epic"].get("Setsuna"):
        if not bonds.setdefault("Interversal Cameo", [False])[0]:
            bonds["Interversal Cameo"][0] = True
            print("Interversal Cameo activated!")

    if inv.get("Legendary", {}).get("Keith") and inv["Legendary"].get("Sah"):
        if not bonds.setdefault("Yin and Yang", [False])[0]:
            bonds["Yin and Yang"][0] = True
            print("Yin and Yang activated!")
            
    if inv.get("Epic", {}).get("Mushy") and inv["Epic"].get("Martis") and inv["Epic"].get("Reyna"):
        if not bonds.setdefault("Furries", [False])[0]:
            bonds["Furries"][0] = True
            print("Furries activated!")


def bonds_inv():
    """
    Prints all activated bonds.
    """
    
    print("///// Bonds /////")
    has_bonds = False  # Track if any bond is active

    for bond, stats in bonds_stats.items():
        com_bonus = bonds_stats[bond][1]
        epic_bonus = bonds_stats[bond][2]
        if stats[0]:  # Check if the first value (boolean) is True
            print(f"""- {bond}
   (Sell Bonus: +${com_bonus} Common / +${epic_bonus} Epic)""")
            has_bonds = True
    
    if not has_bonds:
        print("Empty")