import random
from char_list import minerals

"""GAMBLING (but with minerals)"""

def mine_id(mine):
	if mine == 1:
		return ["Uranium", 5000]
	else:
		return random.choice(minerals)