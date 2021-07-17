from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from plyer import notification
from pygame import mixer
from datetime import datetime
import time

# Header
dev = "diwash007"
print("\n******************************************\n")
print(
      "█░█ █▀▀ ▄▀█ █░░ ▀█▀ █░█ █▄█   █▄░█ █▀█ ▀█▀ █ █▀▀ █ █▀▀ █▀█\n"
      "█▀█ ██▄ █▀█ █▄▄ ░█░ █▀█ ░█░   █░▀█ █▄█ ░█░ █ █▀░ █ ██▄ █▀▄")
print(f"\n******************************************           -Developed by {dev}\n")
print("DO NOT CLOSE THIS WINDOW!!")
print("\n********************************\n")
print(f"Initialized at {datetime.now()}")


# Initialization
init_eyes = init_water = init_ex = time.time()
eye_flag = water_flag = 0
sleeping = 1200


def play_tone(tone):
    """ Function to play the tone"""
    mixer.init()
    mixer.music.load(tone)
    mixer.music.set_volume(0.9)
    mixer.music.play(-1)
    input("Enter anything to stop the alarm!")
    mixer.music.stop()


def eyes(time_gap):
    """ Function to notify to do eye exercise"""
    global init_eyes, eye_flag
    if time.time()-init_eyes > time_gap:
        notification.notify(title="Do EYE exercise!!",
                            message="Blink your eyes for 1 min!!",
                            app_name="EYE Exercise",
                            app_icon="assets\icon.ico", timeout=60)

        print("\n********************************\n"
              "Do EYE exercise!!     - " + str(datetime.now()) +
              "\n********************************\n")
        play_tone("assets\eyes.mp3")
        f = open("stat.txt", "a")
        f.write("Did eye exercise     \t")
        f.write(str(datetime.now()) + "\n")
        f.close()
        init_eyes = time.time()
        eye_flag += 1


def water(time_gap):
    """ Function to notify to drink water"""
    global init_water, water_flag
    if time.time()-init_water > time_gap:
        notification.notify(title="Drink a glass of water!!",
                            message="Drink a glass of water!!",
                            app_name="Drink Water",
                            app_icon="assets\icon.ico", timeout=60)
        print("\n********************************\n"
              "Drink a glass of water!!     - " + str(datetime.now()) +
              "\n********************************\n")
        play_tone("assets\water.mp3")
        f = open("stat.txt", "a")
        f.write("Drank water          \t")
        f.write(str(datetime.now()) + "\n")
        f.close()
        init_water = time.time()
        water_flag += 1


def exercise(time_gap):
    """ Function to notify to do physical exercise"""
    global init_ex
    if time.time()-init_ex > time_gap:
        notification.notify(title="Do Physical Exercise!!",
                            message="Do Physical Exercise!!",
                            app_name="Do Physical Exercise",
                            app_icon="assets\icon.ico", timeout=60)
        print("\n********************************\n"
              "Do Physical exercise!!     - " + str(datetime.now()) +
              "\n********************************\n")
        play_tone("assets\exercise.mp3")
        f = open("stat.txt", "a")
        f.write("Did physical exercise\t")
        f.write(str(datetime.now()) + "\n")
        f.close()
        init_ex = time.time()


while True:

    time.sleep(sleeping)  # to reduce CPU usage

    eyes(1199)  # calling eye exercise notifier

    if eye_flag == 3:   # checking if eye exercise collides with water
        sleeping = 600    # adding time gap
        eye_flag = 0    # resetting flag of collision
        continue        # Continuing operation in order to stop executing below code
    else:
        sleeping = 1200    # setting default sleeping value

    water(3600)  # calling drink water notifier

    if water_flag == 2:    # checking if water collides with physical exercise
        sleeping = 600       # adding time gap
        water_flag = 0     # resetting flag of collision
        time.sleep(sleeping)      # sleeping to avoid collision
    else:
        sleeping = 1200       # setting default sleeping value

    exercise(7200)  # calling physical exercise notifier
