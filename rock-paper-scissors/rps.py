import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = ["rock", "paper", "scissors"]
rps_img = [rock, paper, scissors]
rand = random.randint(0,2)

val = int(input("Enter 0 for rock, 1 for paper, and 2 for scissors:"))

if val < 3:
  print(f"\nYou chose {rps[val]} \n{rps_img[val]}")
  print(f"\nComputer chose {rps[rand]} \n{rps_img[rand]}")

if val == rand:
  print("It's a draw!!")
elif (val == 0 and rand == 2) or (val == 1 and rand == 0) or (val == 2 and rand == 1):
  print("You won!!")
elif val < 3:
  print("Computer won!!")
else:
  print("Invalid Input!!")
