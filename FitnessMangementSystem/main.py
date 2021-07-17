from datetime import datetime
import os
import shutil


def readn(n):
    c = 0
    if n == 1:
        try:
            c = int(input("\nEnter 1 for diet and 2 for exercise \n"))
        except:
            print("\n***\nEnter an integer!!\n***\n")
        print("\n********************************\n")
        if c == 1:
            try:
                f = open("stat/user1diet.txt")
                d = f.read()
                print(d)
                f.close()
            except FileNotFoundError:
                print("\n***\nEmpty!!\n***\n")

        elif c == 2:
            try:
                f = open("stat/user1ex.txt")
                d = f.read()
                print(d)
                f.close()
            except FileNotFoundError:
                print("\n***\nEmpty!!\n***\n")
        else:
            print("\n***\nInvalid Input!!\n***\n")

    elif n == 2:
        try:
            c = int(input("\nEnter 1 for diet and 2 for exercise \n"))
        except:
            print("\n***\nEnter an integer!!\n***\n")
        print("\n********************************\n")
        if c == 1:
            try:
                f = open("stat/user2diet.txt")
                d = f.read()
                print(d)
                f.close()
            except FileNotFoundError:
                print("\n***\nEmpty!!\n***\n")

        elif c == 2:
            try:
                f = open("stat/user2ex.txt")
                d = f.read()
                print(d)
                f.close()
            except FileNotFoundError:
                print("\n***\nEmpty!!\n***\n")
        else:
            print("\n***\nInvalid Input!!\n***\n")

    elif n == 3:
        try:
            c = int(input("\nEnter 1 for diet and 2 for exercise \n"))
        except:
            print("\n***\nEnter an integer!!\n***\n")
        print("\n********************************\n")
        if c == 1:
            try:
                f = open("stat/user3diet.txt")
                d = f.read()
                print(d)
                f.close()
            except FileNotFoundError:
                print("\n***\nEmpty!!\n***\n")

        elif c == 2:
            try:
                f = open("stat/user3ex.txt")
                d = f.read()
                print(d)
                f.close()
            except FileNotFoundError:
                print("\n***\nEmpty!!\n***\n")
        else:
            print("\n***\nInvalid Input!!\n***\n")


def writen(n):
    dt = datetime.now()
    c = 0
    if n == 1:
        try:
            c = int(input("\nEnter 1 for diet and 2 for exercise \n"))
        except:
            print("\n***\nEnter an integer!!\n***\n")
        if c == 1:
            f = open("stat/user1diet.txt", "a")
            d = input("Enter Diet:")
            f.write(d + "\t")
            f.write(str(dt) + "\n")
            print("\n***\nSuccessfully Inserted!!\n***\n")
            f.close()
        elif c == 2:
            f = open("stat/user1ex.txt", "a")
            d = input("Enter Excercise:")
            f.write(d + "\t")
            f.write(str(dt) + "\n")
            print("\n***\nSuccessfully Inserted!!\n***\n")
            f.close()
        else:
            print("\n***\nInvalid Input!!\n***\n")

    elif n == 2:
        try:
            c = int(input("\nEnter 1 for diet and 2 for exercise \n"))
        except:
            print("\n***\nEnter an integer!!\n***\n")
        if c == 1:
            f = open("stat/user2diet.txt", "a")
            d = input("Enter Diet:")
            f.write(d + "\t")
            f.write(str(dt) + "\n")
            print("\n***\nSuccessfully Inserted!!\n***\n")
            f.close()
        elif c == 2:
            f = open("stat/user2ex.txt", "a")
            d = input("Enter Excercise:")
            f.write(d + "\t")
            f.write(str(dt) + "\n")
            print("\n***\nSuccessfully Inserted!!\n***\n")
            f.close()
        else:
            print("\n***\nInvalid Input!!\n***\n")

    elif n == 3:
        try:
            c = int(input("\nEnter 1 for diet and 2 for exercise \n"))
        except:
            print("\n***\nEnter an integer!!\n***\n")
        if c == 1:
            f = open("stat/user3diet.txt", "a")
            d = input("Enter Diet:")
            f.write(d + "\t")
            f.write(str(dt) + "\n")
            print("\n***\nSuccessfully Inserted!!\n***\n")
            f.close()
        elif c == 2:
            f = open("stat/user3ex.txt", "a")
            d = input("Enter Excercise:")
            f.write(d + "\t")
            f.write(str(dt) + "\n")
            print("\n***\nSuccessfully Inserted!!\n***\n")
            f.close()
        else:
            print("\n***\nInvalid Input!!\n***\n")


while True:
    if not os.path.exists("stat"):
        os.mkdir("stat")

    print("\n********************************\n"
          "FITNESS MANAGEMENT SYSTEM"
          "\n********************************\n"
          "\nEnter:\n\t 1 for User-1\n\t 2 for User-2\n\t 3 for User-3\n\t 4 to reset all statistics\n"
          "\t Any other number for exit"
          "\n********************************\n")
    try:
        a = int(input())
    except:
        print("\n***\nEnter an integer!!\n***\n")
        continue
    if a == 4:
        r = input("\nAre you sure to reset statistics? [y/n]\n")
        if r == "y":
            shutil.rmtree("stat")
            print("\n All Statistics have been reset!! \n")
        continue
    if a != 1 and a != 2 and a != 3 and a != 4:
        exit()
    try:
        b = int(input("\nEnter 1 for reading and 2 for writing!"))
    except:
        print("\n***\nEnter an integer!!\n***\n")
        continue
    if b == 1:
        readn(a)
    elif b == 2:
        writen(a)
    else:
        print("\n***\nInvalid value!!\n***\n")
