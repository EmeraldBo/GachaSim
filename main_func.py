import random
import json
import os
import game_data as gd  # Import shared variables
import inventory as inv
import save_func
from char_list import mythic_char, leg_char, epic_char, common_char

"""PULL FUNCTION"""

def pull_id(pull):
	if  0 <= pull <= 0.019:
		return random.choice(mythic_char)
	elif 0.02 <= pull <= 0.1:
		return random.choice(leg_char)
	elif 0.2 <= pull <= 5:
		return random.choice(epic_char)
	else:
		return random.choice(common_char)

def clear_terminal():
	print("\n" * 100)

def reset_all():
	gd.pity = 0
	gd.pulls = 0
	gd.money = 500
	gd.max_pity = 0
	gd.luck_max = 100
	gd.luck_min = 1
	gd.pull_main = round(random.uniform(gd.luck_min, gd.luck_max), 1)
	gd.last_pull_time = 0  # Reset cooldown

	# Reset the inventories  
	inv.reset_inventory()  

	print("All progress has been reset.")

"""SYNCING VARIABLES WITH SAVE FILE"""

def save_game(slot):
	save_data = {
		"Inventory": {
			"Mythic Characters": inv.inventory["Mythic"],
			"Legendary Characters": inv.inventory["Legendary"],
			"Epic Characters": inv.inventory["Epic"],
			"Common Characters": inv.inventory["Common"],
			"Plushies": inv.inventory_items["Plushies"],
			"Tokens": inv.inventory_items["Tokens"]
		},
		"Progress": {
			"Money": gd.money,
			"Pity": gd.pity,
			"Pulls": gd.pulls,
			"Max Pity": gd.max_pity,
			"Luck Max": gd.luck_max,
			"Luck Min": gd.luck_min,
			"Pull Main": gd.pull_main
		}
	}
	file_path = save_func.get_save_file(slot)
	save_func.save_file( save_data, file_path)

def save_game_MOD():
	save_data = {
		"Inventory": {
			"Legendary Characters": inv.inventory["Legendary"],
			"Epic Characters": inv.inventory["Epic"],
			"Common Characters": inv.inventory["Common"],
			"Plushies": inv.inventory_items["Plushies"],
			"Tokens": inv.inventory_items["Tokens"]
		},
		"Progress": {
			"Money": gd.money,
			"Pity": gd.pity,
			"Pulls": gd.pulls,
			"Max Pity": gd.max_pity,
			"Luck Max": gd.luck_max,
			"Luck Min": gd.luck_min,
			"Pull Main": gd.pull_main
		}
	}
	save_func.save_file_mod(save_data)


def load_game():
	loaded_data = save_func.load_file(save_func.get_save_file())
	if loaded_data:
		# Load inventory data
		inv.inventory["Mythic"].update(loaded_data.get("Inventory", {}).get("Mythic Characters", {}))
		inv.inventory["Legendary"].update(loaded_data.get("Inventory", {}).get("Legendary Characters", {}))
		inv.inventory["Epic"].update(loaded_data.get("Inventory", {}).get("Epic Characters", {}))
		inv.inventory["Common"].update(loaded_data.get("Inventory", {}).get("Common Characters", {}))
		inv.inventory_items["Plushies"].update(loaded_data.get("Inventory", {}).get("Plushies", {}))
		inv.inventory_items["Tokens"].update(loaded_data.get("Inventory", {}).get("Tokens", {}))

		# Load progress data
		progress = loaded_data.get("Progress", {})
		gd.pity = progress.get("Pity", 0)
		gd.pulls = progress.get("Pulls", 0)
		gd.max_pity = progress.get("Max Pity", 0)
		gd.luck_max = progress.get("Luck Max", 100)
		gd.luck_min = progress.get("Luck Min", 1)
		gd.money = progress.get("Money", 500)
		gd.pull_main = progress.get("Pull Main", round(random.uniform(gd.luck_min, gd.luck_max), 1))

def load_game_mod():
	loaded_data = save_func.load_file_mod()
	if loaded_data:
		# Load inventory data
		inv.inventory["Legendary"].update(loaded_data.get("Inventory", {}).get("Legendary Characters", {}))
		inv.inventory["Epic"].update(loaded_data.get("Inventory", {}).get("Epic Characters", {}))
		inv.inventory["Common"].update(loaded_data.get("Inventory", {}).get("Common Characters", {}))
		inv.inventory_items["Plushies"].update(loaded_data.get("Inventory", {}).get("Plushies", {}))
		inv.inventory_items["Tokens"].update(loaded_data.get("Inventory", {}).get("Tokens", {}))

		# Load progress data
		progress = loaded_data.get("Progress", {})
		gd.pity = progress.get("Pity", 0)
		gd.pulls = progress.get("Pulls", 0)
		gd.max_pity = progress.get("Max Pity", 0)
		gd.luck_max = progress.get("Luck Max", 100)
		gd.luck_min = progress.get("Luck Min", 1)
		gd.money = progress.get("Money", 500)
		gd.pull_main = progress.get("Pull Main", round(random.uniform(gd.luck_min, gd.luck_max), 1))                