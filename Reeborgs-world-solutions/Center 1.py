def hoop():
    def flip():
        turn_left()
        turn_left()
        
    x=0
    while front_is_clear():
        move()
        x += 1
    flip()
    move()
    flip()
    build_wall()
    flip()
    while x != 2:
        move()
        x -=1
    build_wall()
    flip()
    
while not wall_in_front():
    hoop()
put()
