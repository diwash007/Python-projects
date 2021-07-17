#The code by Angela Yu has looping problem. This program solves that problem.
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear() and not right_is_clear:
        move()
    elif right_is_clear():
        turn_right()
        move()
    else:
        turn_left()
