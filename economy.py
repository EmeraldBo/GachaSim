import inventory as inv
import bonds as b
from inventory import inventory

money = 5000

shop = {
	"Plushies": {
		"Chimer Plushie": [2500, 25],
		"Ketsueki Plushie": [2250, 20],
		"Keith Plushie": [1000, 10],
		"Sah Plushie": [1000, 10],
		"Carlo Plushie": ["N/A", "N/A"]
	},
	"Tokens": {
		"Bronze Token": [250, 1],
		"Silver Token": [750, 2],
		"Gold Token": [1250, 2],
		"Diamond Token": [2500, 3]
	}
}    

def buy_shop(money, shop, category, item, inv):
	# Validate category and item exist
	if category not in shop or item not in shop[category]:
		print("Invalid category or item.")
		return money

	price = shop[category][item][0]

	# Check if item is purchasable
	if price == "N/A":
		print(f"{item} is not available for purchase.")
		return money

	# Check if player has enough money
	if money >= price:
		if inv[category][item] == False:
			money -= price
			print(f"Bought: {item} from category {category} for ${price}")
			inv[category][item] = True
		else:
			print()
	else:
		print("Not enough money.")

	return money

def show_shop(shop):
	print("~~~~~Luck Plushies~~~~~")    
	for item, value in shop["Plushies"].items():
		print(f"- {item} / ${value[0]} +{value[1]} Luck")
	print("~~~~~Cooldown Tokens~~~~~")
	for item, value in shop["Tokens"].items():
		print(f"- {item} / ${value[0]} -{value[1]} Cooldown")

def shop_select(shop_x, shop):
	shop_x = shop_x.lower()  # Convert input to lowercase
	shop_lower = {key.lower(): key for key in shop}  # Dictionary with lowercase keys
	
	if shop_x in shop_lower:
		selected_shop = shop_lower[shop_x]  # Get the original key
		print(f"Selected Shop: {selected_shop}")
		return selected_shop
	elif shop_x == "back":
		return None    
	else:
		print("That shop doesn't exist!")
		return None

def sell(option, money):
	"""Sell all Common and Epic characters without affecting other categories."""
	total_com = 0
	total_epic = 0

	if option == "all":
		# Count Common and Epic characters
		common_count = sum(value[1] for value in inv.inventory["Common"].values() if value[0] is True)
		epic_count = sum(1 for value in inv.inventory["Epic"].values() if value is True)

		# Only proceed if there are characters to sell
		if common_count > 0 or epic_count > 0:
			bond_bonus_com = sum(values[1] for values in b.bonds_stats.values())
			bond_bonus_epic = sum(values[2] for values in b.bonds_stats.values())

			total_com = (10 * common_count + bond_bonus_com)
			total_epic = (100 * epic_count + bond_bonus_epic)

			# Remove only common and epic characters
			for char in list(inv.inventory["Common"].keys()):
				inv.inventory["Common"][char] = (False, 0)  # Set ownership to False

			for char in list(inv.inventory["Epic"].keys()):
				inv.inventory["Epic"][char] = False  # Set ownership to False

	elif option in inv.inventory["Common"] and inv.inventory["Common"][option][0] is True:
		total_com = 10  # Value for selling one Common character
		inv.inventory["Common"][option] = (False, 0)

	elif option in inv.inventory["Epic"] and inv.inventory["Epic"][option] is True:
		total_epic = 100  # Value for selling one Epic character
		inv.inventory["Epic"][option] = False

	# Add money only if characters were actually sold
	if total_com > 0 or total_epic > 0:
		money += total_com + total_epic

	return money