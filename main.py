import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
player = Player()
screen = Screen()
car_manager = CarManager()
score_board = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(player.go_up, "Up ")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    
    car_manager.create_car()
    car_manager.movecar()
    
    for car in car_manager.all_cars:
        if car.distance(player)<20 :
            game_is_on = False
            score_board.game_over()
            
    
    if player.is_at_finnish_line():
        score_board.increse_level()
        car_manager.level_up()
        player.go_to_start()
            
screen.exitonclick()