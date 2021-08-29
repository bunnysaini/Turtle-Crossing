import random
from turtle import Turtle

COLORS = ["navajowhite", "chartreuse2", "dark turquoise", "light slate blue", "yellow", "lawn green", "violetred", "cyan", "purple3", "SeaGreen2", "gold2", "IndianRed1", "maroon1", "magenta2", "orchid1"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_event = random.randint(1,6)
        if random_event == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(300, random.randint(-250, 250))
            self.car_list.append(new_car)

    def move_cars(self):
        for car in self.car_list:
            car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += STARTING_MOVE_DISTANCE