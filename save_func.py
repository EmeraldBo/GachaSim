import os
import json
from inventory import inventory

def get_save_file(save_slot):
    if 1 <= save_slot <= 5:
        return f"saves/save{save_slot}.json"
    else:
        print("Invalid Slot. Using default slot...")
        return "saves/save1.json"
def save_file(save_data, slot, ):
    try:
        file_path = slot

        # Check if file exists and if we need to overwrite
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                data = file.read().strip()
                if data and json.loads(data) not in ([], {}):
                    return True

        with open(file_path, "w") as file:
            json.dump(save_data, file, indent=4)
        print("Save successful.")

    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Error saving file: {e}")
        print("Creating a new save.")
        with open(file_path, "w") as file:
            json.dump(save_data, file, indent=4)
        print("Save successful.")

def save_file_mod(save_data):
    try:
        file_path = "saves/save_MOD.json"

        # Check if file exists and if we need to overwrite
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                data = file.read().strip()
                if data and json.loads(data) not in ([], {}):
                    opt = input("THIS SAVE FILE ALREADY HAS A SAVE, DO YOU WANT TO OVERWRITE? (y/n): ").strip().lower()
                    if opt != "y":
                        print("Save Cancelled.")
                        return

        with open(file_path, "w") as file:
            json.dump(save_data, file, indent=4)
        print("Save successful.")

    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Error saving file: {e}")
        print("Creating a new save.")
        with open(file_path, "w") as file:
            json.dump(save_data, file, indent=4)
        print("Save successful.")


def load_file(slot):
    try:
        file_path = slot
        with open(file_path, "r") as file:
            data = json.load(file)
            print("Loaded save data:")
            return data
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Error loading file: {e}")
        print("No save file found or file is invalid.")
        return None

def load_file_mod():
    try:
        file_path = "saves/save_MOD.json"
        with open(file_path, "r") as file:
            data = json.load(file)
            print("Loaded save data:")
            return data
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Error loading file: {e}")
        print("No save file found or file is invalid.")
        return None
