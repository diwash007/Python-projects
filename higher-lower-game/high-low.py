import random
from game_data import data
from replit import clear


def data_gen():
    return random.choice(data)

def data_display(a,n):
    print(f"Compare {n}: {a['name']}, {a['description']}, from {a['country']}")
    
def check_data(choice,a,b):
    global score, not_end
    if (choice == "A" and a["follower_count"] > b["follower_count"]) or (choice == "B" and b["follower_count"] > a["follower_count"]):
        score += 1
        clear()
        print(logo)
        print(f"Correct answer!! Current score: {score}\n")
    else:
        clear()
        print(f"Sorry, that's wrong!! Final score: {score}")
        not_end = False

def display_all(a):
    data_display(a,"A")

    print("\nVS\n")

    b = data_gen()
    data_display(b,"B")

    choice = input("\nwho has more followers? 'A' or 'B'?").upper()

    check_data(choice,a,b)
    return b


logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
\n"""
print(logo)
score = 0
not_end = True
a = data_gen()
b = display_all(a)

while not_end:
    c = display_all(b)
    b = c
