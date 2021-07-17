import random
from hangman_words import word_list
from hangman_art import stages, logo
from replit import clear

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:

    guess = input("Guess a letter: ").lower()
    clear()

    if guess in display:
        print(f"You have already guessed {guess}.")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"'{guess}' is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("""

 _  _  _____  __  __    __    _____  ___  ____ 
( \/ )(  _  )(  )(  )  (  )  (  _  )/ __)( ___)
 \  /  )(_)(  )(__)(    )(__  )(_)( \__ \ )__) 
 (__) (_____)(______)  (____)(_____)(___/(____)

""")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print(""" _  _  _____  __  __    _    _  ____  _  _ 
( \/ )(  _  )(  )(  )  ( \/\/ )(_  _)( \( )
 \  /  )(_)(  )(__)(    )    (  _)(_  )  ( 
 (__) (_____)(______)  (__/\__)(____)(_)\_)

""")
    if not end_of_game:
        print(stages[lives])
