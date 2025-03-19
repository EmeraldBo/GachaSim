from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import os
import random
import game_data as gd
import inventory as inv
import main_func as mf
import save_func as sf
import bonds as b
import economy as ec
import mining as m
from kivy.clock import Clock
from kivy.core.window import Window
 
Window.size = (800, 800)


# Define Screens
class MainMenu(Screen):
	pass

class OtherScreen(Screen):
	pass

class SavesScreen(Screen):
	pass

class UpdateLog(Screen):
	def on_pre_enter(self):
		with open('updatelog.txt','r') as file:
			content = file.read()
		self.ids.update_log_label.text = f"{content}"
	pass

class MineScreen(Screen):
	m_cooldown_active = False  
	m_cooldown_time = 30

	def on_pre_enter(self):
		self.update_money_display()

	def update_money_display(self):
		app = App.get_running_app()
		self.ids.money_label.text = f"Money: ${app.money}"
	
	def mine(self):
		if self.m_cooldown_active:
			return
		
		self.m_cooldown_active = True
		self.ids.mine_button.disabled = True
		self.ids.m_cooldown_label.text = f"Cooldown: {self.m_cooldown_time}"
		
		mine_luck = random.randint(1, 1000)
		mineral = m.mine_id(mine_luck)
		self.ids.mine_rewards.text = f"You got: {mineral[0]} (${mineral[1]})"

		app = App.get_running_app()
		app.money += mineral[1]

		app.update_money_display()

		self.remaining_time = self.m_cooldown_time
		Clock.schedule_interval(self.update_cooldown, 1)  
		Clock.schedule_once(self.reset_cooldown, self.m_cooldown_time)

		self.update_money_display()


	def update_cooldown(self, dt):
		self.remaining_time -= 1
		if self.remaining_time > 0:
			self.ids.m_cooldown_label.text = f"Cooldown: {self.remaining_time}s"
		else:
			self.ids.m_cooldown_label.text = ""

	def reset_cooldown(self, dt):
		self.m_cooldown_active = False
		self.ids.mine_button.disabled = False
		self.ids.m_cooldown_label.text = ""  
		Clock.unschedule(self.update_cooldown)

class SaveMenu(Screen):
	overwrite_prompt = False  # Now an instance variable

	def save_game_slot1(self):
		file_path = sf.get_save_file(1)

		# Check if the save slot already contains data
		if os.path.exists(file_path):
			if not self.overwrite_prompt:
				self.ids.save_label.text = "THIS SLOT ALREADY HAS A SAVE, CLICK AGAIN TO CONFIRM OVERWRITE."
				self.overwrite_prompt = True
				return

		# Proceed with saving the game
		mf.save_game(1)
		print("Save Success (Debug)")
		self.ids.save_label.text = "Game saved successfully!"
		self.overwrite_prompt = False  # Reset confirmation
	
	def save_game_slot2(self):
		file_path = sf.get_save_file(2)

		# Check if the save slot already contains data
		if os.path.exists(file_path):
			if not self.overwrite_prompt:
				self.ids.save_label.text = "THIS SLOT ALREADY HAS A SAVE, CLICK AGAIN TO CONFIRM OVERWRITE."
				self.overwrite_prompt = True
				return

		# Proceed with saving the game
		mf.save_game(2)
		print("Save Success (Debug)")
		self.ids.save_label.text = "Game saved successfully!"
		self.overwrite_prompt = False  # Reset confirmation
	
	def save_game_slot3(self):
		file_path = sf.get_save_file(3)

		# Check if the save slot already contains data
		if os.path.exists(file_path):
			if not self.overwrite_prompt:
				self.ids.save_label.text = "THIS SLOT ALREADY HAS A SAVE, CLICK AGAIN TO CONFIRM OVERWRITE."
				self.overwrite_prompt = True
				return

		# Proceed with saving the game
		mf.save_game(3)
		print("Save Success (Debug)")
		self.ids.save_label.text = "Game saved successfully!"
		self.overwrite_prompt = False  # Reset confirmation

class LoadMenu(Screen):
	def load_game(save_slot, self):
		loaded_data = sf.load_file(sf.get_save_file(save_slot))
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
		if not os.path.exists(sf.get_save_file(save_slot)):
			self.ids.load_label.text = "Game Loaded Unsuccessfully! No file was found!"
		else:
			self.ids.load_label.text = "Game Loaded Successfully!"
	def load_game_slot1(self):
		LoadMenu.load_game(1, self)

	def load_game_slot2(self):
		LoadMenu.load_game(2, self)

	def load_game_slot3(self):
		LoadMenu.load_game(3, self)

class GachaScreen(Screen):
	cooldown_active = False  
	cooldown_time = 10 - gd.get_total_cooldown_reduction()

	def pull_character(self):
		if self.cooldown_active:
			return  

		self.cooldown_active = True  
		self.ids.pull_button.disabled = True
		self.ids.cooldown_label.text = f"Cooldown: {self.cooldown_time}s"  

		pull_chance = round(random.uniform(gd.luck_min, gd.luck_max), 1)
		pulled_char = mf.pull_id(pull_chance)

		rarity = "Mythic" if pulled_char in inv.inventory["Mythic"] else \
				 "Legendary" if pulled_char in inv.inventory["Legendary"] else \
				 "Epic" if pulled_char in inv.inventory["Epic"] else "Common"

		inv.obtain_char(pulled_char)
		inventory_screen = App.get_running_app().root.get_screen("inventory")
		inventory_screen.update_inventory_display()
		self.ids.pull_result.text = f"You pulled: {pulled_char} ({rarity})"

		self.remaining_time = self.cooldown_time
		Clock.schedule_interval(self.update_cooldown, 1)  
		Clock.schedule_once(self.reset_cooldown, self.cooldown_time)

	def update_cooldown(self, dt):
		self.remaining_time -= 1
		if self.remaining_time > 0:
			self.ids.cooldown_label.text = f"Cooldown: {self.remaining_time}s"
		else:
			self.ids.cooldown_label.text = ""

	def reset_cooldown(self, dt):
		self.cooldown_active = False
		self.ids.pull_button.disabled = False
		self.ids.cooldown_label.text = ""  
		Clock.unschedule(self.update_cooldown)  

class InventoryScreen(Screen):
	def on_pre_enter(self):
		self.update_inventory_display()

	def update_inventory_display(self):
		inventory_text = "/////Characters/////\n"
		items_text = "/////Items/////\n"
		has_characters = False
		has_items = False  

		try:
			for rarity in ["Mythic", "Legendary", "Epic", "Common"]:
				owned_chars = []

				if rarity != "Common":
					for char, obtained in inv.inventory[rarity].items():
						if obtained:
							has_characters = True
							owned_chars.append(f"<<<{char}>>>" if rarity == "Mythic" else f"- {char}")
				else:
					for char, (is_owned, count) in inv.inventory["Common"].items():
						if is_owned:
							has_characters = True
							owned_chars.append(f"- {char} ({count})")

				inventory_text += f"\n~~~~~{rarity}~~~~~\n" + ("\n".join(owned_chars) if owned_chars else "Empty") + "\n"
				
			for category in ["Plushies", "Tokens"]:
				owned_items = []

				for item, obtained in inv.inventory_items[category].items():
					if obtained:
						has_items = True
						owned_items.append(f"- {item}")
				items_text += f"\n~~~~~{category}~~~~~\n" + ("\n".join(owned_items) if owned_items else "Empty") + "\n"
				

			self.ids.inventory_list.text = inventory_text if has_characters else "No characters owned."
			self.ids.items_list.text = items_text if has_items else "No items owned."
		except Exception as e:
			print(f"Error updating inventory display: {e}")

	def sell_character(self):
		app = App.get_running_app()  
		app.money = ec.sell("all", app.money)  
		self.update_inventory_display()  
		app.update_money_display()  

class ShopScreen(Screen):
	def on_pre_enter(self):
		self.update_money_display()

	def buy_item(self, category, item):
		app = App.get_running_app()
		app.money = ec.buy_shop(app.money, ec.shop, category, item, inv.inventory_items)
		self.update_money_display()

	def update_money_display(self):
		app = App.get_running_app()
		self.ids.money_label.text = f"Money: ${app.money}"

class GachaApp(App):
	money = 500  

	def update_money_display(self):
		if self.root:
			try:
				inventory_screen = self.root.get_screen("inventory")
				if "money_label" in inventory_screen.ids:
					inventory_screen.ids.money_label.text = f"Money: ${self.money}"
				else:
					print("money_label not found in InventoryScreen.ids")
			except Exception as e:
				print(f"Error updating money display: {e}")
	def build(self):
		return Builder.load_file("main.kv")

if __name__ == "__main__":
	GachaApp().run()