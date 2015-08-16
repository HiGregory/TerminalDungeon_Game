import random

CELLS = [(0,0), (0,1), (0,2), 
		 (1,0), (1,1), (1,2),
		 (2,0), (2,1), (2,2)]

def get_location():
	# monster = random
	# door = random
	#start = random
	monster = random.choice(CELLS)
	door = random.choice(CELLS)
	start = random.choice(CELLS)

	# if monster, door, or start are the same, do it again

	# return monster, door, start 

	if monster == door or monster == start or door == start:
		return get_location()

	return monster, door, start

def move_player(player, move):
	# player = (x, y)
	x, y = player

	# I need to get the player's current location
	# If move is L, y - 1. If move is R, y + 1
	# If move is U, x - 1. If move is D, x + 1
	if move == 'L':
		y-= 1
	elif move == 'R':
		y+= 1
	elif move == 'U':
		x-= 1
	elif move == 'D':
		x+= 1

	return x, y

def get_moves(player):
	moves = ['L', 'R', 'U', 'D']
	# player = (x, y)

	# If player's y is 0, remove LEFT. If player's x is 0, remove UP
	# If player's y is 2, remove RIGHT. If player's x is 2, remove Down

	if player[1] == 0:
		moves.remove('L')
	if player[1] == 2:
		moves.remove('R')
	if player[0] == 0:
		moves.remove('U')
	if player[0] == 2:
		moves.remove('D')
	return moves

# This code will the Map 
def draw_map():
	print(' _ _ _')
	tile = '|{}'

	for idx, cell in enumerate(CELLS):
	  if idx in [0, 1, 3, 4, 6, 7]:
			if cell == player:
				print(tile.format('X'), end="")
			else:
				print(tile.format('_'), end="")
				if cell == player:
					print(tile.format('X|'), end="")
				else:
					print(tile.format('_|'), end="")


monster, door, player = get_location()
print("Welcome to Gregory's dungeon")

while True:
	moves = get_moves(player)
	# next I will call the function I created draw map

	# this will show in the terminal where the player is
	print("You current room is {}".format(player)) 
	# this will show in the terminal where the player can move
	print("You can move {}".format(moves))
	# This allows person playing the game to quit the game 
	print("Enter QUIT to quit")

	move = input("> ")
	move = move.upper()


	if move == "QUIT":
	   break
	# If it's a good move, change player position
	if move in moves:
		player = move_player(player, move)
	# If bad move, do nothing
	else:
		print(" ** You just walked into a wall. BE CAREFUL! **")
		continue
	# If the new player position is at the door, they win!
	if player == door:
		print("You made it out!")
		break
	# If the new player position is at the monster, they lose!
	elif player == monster:
		print("The monster just ate you for dinner")
		break

