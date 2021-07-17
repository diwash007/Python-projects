import random

def guess_game(attempts):

	num = random.randint(1,100)

	while attempts > 0:

		print(f"You have {attempts} guess remaining.")
		guess = int(input("Guess a number: "))

		if guess == num:
			print(f"You guessed it!! The number is {num}")
			attempts = 0
		elif guess > num:
			print("Too high")
		elif guess < num:
			print("Too low")
		if attempts == 1:
			print(f"You ran out of guesses, You lose!! The number is {num}")
		attempts -= 1

def difficulty():
	level = input("Choose level: 'easy' or 'hard': ")
	if level == "hard":
		return 5
	else:
		return 10


print("Welcome to the guessing game!!")
print("I am thinking of a number between 1 and 100.")

attempts = difficulty()
guess_game(attempts)
