import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # If turtle collides with car, game ends
    for car in car_manager.car_list:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.finish_indication()

    # if player crosses the finishing line, it returns to initial position
    if player.crossed_finish_line():
        player.initial_position()
        car_manager.increase_speed()
        scoreboard.add_point()

screen.exitonclick()