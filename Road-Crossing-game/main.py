import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("grey")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
game_level = Scoreboard()
manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
car_tracker = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # creating car every 6th frame
    if car_tracker % 6 == 0  or car_tracker == 0:
    	manager.create_car()

    # updating level
    if player.has_crossed_finish_line():
        game_level.update_score()
        manager.update_speed()    
        player.goto_start()

    #checking collision
    for car in manager.cars:
    	if player.distance(car) < 20:
    		game_is_on = False

    manager.move()		

    car_tracker += 1

screen.exitonclick()