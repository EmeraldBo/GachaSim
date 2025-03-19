# game_data.py
import inventory as inv
import economy as ec

def get_total_cooldown_reduction():
    return inv.total_cd(inv.inventory_items, ec.shop)
    
def get_total_luck_reduction():
    return inv.total_luck(inv.inventory_items, ec.shop)
pity = 70
pulls = 0
money = 500
max_pity = 0
luck_max = 100 - get_total_luck_reduction()
luck_min = 0.01
pull_main = 50  # Default value
last_pull_time = 0
last_mine_time = 0