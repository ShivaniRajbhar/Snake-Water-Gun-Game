# Import random module
import random
print('python - java - javascript')


# Input no. of rounds
n = int(input('Enter number of rounds: '))


# List containing Snake(s), Water(w), Gun(g)
options = ['p', 'j', 'ja']

# Round numbers
rounds = 1

# Count of computer wins
comp_win = 0

# Count of player wins
user_win = 0



while rounds <= n:

	# Display round
	print(f"Round :{rounds}\npython - 'p'\njava - 'j'\njavasscript - 'ja'")

	# Exception handling
	try:
		player = input("Choose your option: ")
	except EOFError as e:
		print(e)

	# Control of bad inputs
	if player != 'p' and player != 'j' and player != 'ja':
		print("Invalid input, try again\n")
		continue

	# random.choice() will randomly choose
	# item from list- options
	computer = random.choice(options)

	# Conditions based on the game rule
	if computer == 'p':
		if player == 'j':
			comp_win += 1
		elif player == 'j':
			user_win += 1

	elif computer == 'g':
		if player == 'w':
			comp_win += 1
		elif player == 'w':
			user_win += 1

	elif computer == 'g':
		if player == 's':
			comp_win += 1
		elif player == 'w':
			user_win += 1

	# Announce winner of every round
	if user_win > comp_win:
		print(f"You Won round {rounds}\n")
	elif comp_win > user_win:
		print(f"Computer Won round {rounds}\n")
	else:
		print("Draw!!\n")

	rounds += 1


# Final winner based on the number of wons
if user_win > comp_win:
	print("Congratulations!! You Winning the round")
elif comp_win > user_win:
	print("You lose but dont worry you try again!!")
else:
	print("match draw!!")
