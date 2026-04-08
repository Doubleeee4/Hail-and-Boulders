from turtle import Screen
from player import Player
import hail_n_boulders
import level_and_level_pb_and_scoreboard
import math
import time

screen = Screen()
player = Player()
obstacles = hail_n_boulders.HailNBoulders()
scoreboard = level_and_level_pb_and_scoreboard.Text()

screen.setup(1000,800)
screen.tracer(0)
game_over=False
pause_boolean = False
def pause():
    if pause_boolean:
        time.sleep(0.01)
        screen.ontimer(pause, 0)
def pause_variable_true():
    global pause_boolean
    if not pause_boolean:
        pause_boolean = True
        scoreboard.goto(0,0)
        scoreboard.write(arg="Paused", align="center", move=False, font=("Arial", 20, "normal"))
    else:
        pause_boolean = False
        scoreboard.clear()
        scoreboard.goto(0, 350)
        scoreboard.write(f"Level:{scoreboard.level} Personal best:{scoreboard.level_pb}", False, "center", scoreboard.font)
        scoreboard.pu()
        scoreboard.goto(-500, -190)
        scoreboard.pd()
        scoreboard.goto(500, -190)
        scoreboard.pu()



def collision():
    boulder_coords = []
    hail_coords = []
    player_coords = (player.xcor(), player.ycor())
    for boulder in obstacles.boulders_active:
        if boulder.isvisible():
            x = (boulder.xcor(),boulder.ycor())
            boulder_coords.append(x)
    for hail in obstacles.hail_active:
        x = (hail.xcor(),hail.ycor())
        hail_coords.append(x)
    for coords in boulder_coords:
        if  math.dist(player_coords, coords) < (45 + 10):
            return True
    for coords in hail_coords:
        if math.dist(player_coords, coords) < (15 + 10):
            return True
    return False


keys = {
    "w": False,
    "a": False,
    "s": False,
    "d": False
}

def press_w(): keys["w"] = True
def release_w(): keys["w"] = False
def press_a(): keys["a"] = True
def release_a(): keys["a"] = False
def press_s(): keys["s"] = True
def release_s(): keys["s"] = False
def press_d(): keys["d"] = True
def release_d(): keys["d"] = False

screen.listen()

screen.onkeypress(press_w, "w")
screen.onkeyrelease(release_w, "w")
screen.onkeypress(press_a, "a")
screen.onkeyrelease(release_a, "a")
screen.onkeypress(press_s, "s")
screen.onkeyrelease(release_s, "s")
screen.onkeypress(press_d, "d")
screen.onkeyrelease(release_d, "d")
screen.onkeypress(pause_variable_true, "p")

def game_loop():
    global game_over
    game_over = collision()

    if keys["w"]:
        player.move_up()
    if keys["s"]:
        player.move_down()
    if keys["a"]:
        player.move_left()
    if keys["d"]:
        player.move_right()
    obstacles.roll_hail_spawn_chance()
    obstacles.move_all_hail()
    obstacles.roll_boulder_spawn_chance()
    obstacles.move_all_boulders()
    obstacles.special_event_roll()
    obstacles.check_level_up_all()
    obstacles.check_for_inactive_boulders()
    obstacles.check_for_inactive_hail()
    obstacles.delay -= 1

    scoreboard.level_clock()
    scoreboard.rewrite_plus_level_update()
    if scoreboard.clock_ == 0.001:
        scoreboard.goto(370, 350)
        scoreboard.write(arg="Press p to pause", align="center", move=False, font= ("Arial",20,"normal"))
    pause()

    screen.update()
    if not game_over:
        screen.ontimer(game_loop,16)
    else:
        scoreboard.save_level_pb()
        scoreboard.game_over_text()



game_loop()
screen.mainloop()
screen.exitonclick()