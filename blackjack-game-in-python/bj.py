import random
from replit import clear


deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]
player_cards = []
c_card = []
not_end = True

def serve():
    player_cards.append(random.choice(deck))
    player_cards.append(random.choice(deck))
    c_card.append(random.choice(deck))
    c_card.append(random.choice(deck))

    player_bj = False
    c_bj = False

    if sum(player_cards) == 21:
        player_bj = True
    elif sum(c_card) == 21:
        c_bj = True

    return [sum(player_cards), sum(c_card), player_bj, c_bj]

def check_ace(who, who_index):
    if sum(who) > 21:
        for i in range(len(who)):
            if who[i] == 11:
                who[i] = 1
        score[who_index] = sum(who)

def c_more_cards():
    while score[1] < 17:
        c_card.append(random.choice(deck))
        score[1] = sum(c_card)
        check_ace(c_card,1)

def display():

    print("\n\n ******* Result *******\n")
    print(f"Your cards: {player_cards}")
    print(f"Your score: {score[0]}")
    print(f"Computer's cards: {c_card}")
    print(f"Computer's score: {score[1]}")

    if score[3] == True or score[0] > 21:
        print("You Lose!!\n")
    elif score[0] == score[1]:
        print("It's a draw!!\n")
    elif score[2] or (score[0] > score[1] and not score[0] > 21) or score[1] > 21:
        print("You win!!\n")
    elif not score[1] > 21:
        print("You lose!\n")
    not_end = False

def rounds():

    choice = input("Type 'y' to hit or 'n' to pass: ")
    c_more_cards()

    if choice == "n":
        display() 
    elif choice == "y":      
        player_cards.append(random.choice(deck))
        score[0] = sum(player_cards)
        check_ace(player_cards,0)
        print(f"\nYour cards: {player_cards}")
        print(f"Your score: {score[0]}")
        print(f"Computer's first card: {c_card[0]}\n")
        rounds()
    else:
        rounds()

while not_end:

    choice = input("Do you want to play BlackJack? 'y' or 'n'")
    
    clear()

    if choice == "y":

        print("BLACKJACK GAME\n")
        score = serve()
        print(f"Your cards: {player_cards}")
        print(f"Your score: {score[0]}\n")
        print(f"Computer's first card: {c_card[0]}\n")

        rounds()

        player_cards = []
        c_card = []
