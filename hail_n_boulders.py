from turtle import Turtle
import random
from itertools import chain
stuff_spawned_count = 0
level_up_flag = False
class OneHail(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("triangle")
        self.shapesize(1,1.5)
        self.color("light blue")
        self.setheading(270)
        self.hideturtle()
        self.move_speed = 8
        self.goto(random.randint(-500, 500), 500)
        self.showturtle()
    def move_hail(self):
        self.sety(self.ycor() - self.move_speed)

class Boulder(Turtle):
    def __init__(self, custom_spawn):
        super().__init__()
        self.pu()
        self.shape("circle")
        self.shapesize(4.5,4.5)
        self.color("gray")
        self.hideturtle()
        self.move_speed = 7
        self.spawn_side = ""
        if not custom_spawn:
            double_coinflip=random.randint(1,4)
            if double_coinflip == 1:
                self.goto((600, -347))
                self.spawn_side = "r"
            elif double_coinflip == 2:
                self.goto((600, -235))
                self.spawn_side = "r"
            elif double_coinflip == 3:
                self.goto((-600, -347))
                self.spawn_side = "l"
            else:
                self.goto((-600,-235))
                self.spawn_side = "l"
        elif custom_spawn:
            pass
        else:
            print("Variable custom spawn is not a boolean. Invalid custom spawn entry")

        self.showturtle()

    def move_boulder(self):
        if self.spawn_side == "r":
            self.setx(self.xcor() - self.move_speed)
        elif self.spawn_side == "l":
            self.setx(self.xcor() + self.move_speed)
        else:
            print(f"self.spawn side variable must be set to l or r but it is set to: {self.spawn_side}.")
class HailNBoulders:
    def __init__(self):
        self.boulders_active = []
        self.boulder_spawn_chance = 120
        self.hail_active = []
        self.hail_spawn_chance = 30
        self.special_event_chance = 10000
        self.boulder_pool = []
        self.hail_pool = []
        self.hail_speed = 6
        self.boulder_speed = 5
        self.delay = 0
    def roll_boulder_spawn_chance(self):
        if random.randint(1, self.boulder_spawn_chance) == 2 and self.delay < 0:
            if not self.boulder_pool:
                temporary_object = Boulder(False)
                self.boulders_active.append(temporary_object)
                temporary_object.move_speed = self.boulder_speed
                self.delay = 30
            elif self.delay < 0:
                self.boulder_pool[0].showturtle()
                double_coinflip = random.randint(1, 4)
                if double_coinflip == 1:
                    self.boulder_pool[0].goto((600, -347))
                    self.boulder_pool[0].spawn_side = "r"
                elif double_coinflip == 2:
                    self.boulder_pool[0].goto((600, -235))
                    self.boulder_pool[0].spawn_side = "r"
                elif double_coinflip == 3:
                    self.boulder_pool[0].goto((-600, -347))
                    self.boulder_pool[0].spawn_side = "l"
                else:
                    self.boulder_pool[0].goto((-600, -235))
                    self.boulder_pool[0].spawn_side = "l"
                self.boulders_active.append(self.boulder_pool[0])
                self.boulder_pool.remove(self.boulder_pool[0])
                self.delay = 30

    def check_for_inactive_boulders(self):
        for boulder in self.boulders_active[:]:
            if -600 > boulder.xcor() or boulder.xcor() > 700:
                self.boulders_active.remove(boulder)
                boulder.hideturtle()
                if boulder.spawn_side == "l":
                    boulder.setx(-600)
                else:
                    boulder.setx(600)
                self.boulder_pool.append(boulder)
    def move_all_boulders(self):
        for boulder in self.boulders_active:
            boulder.move_speed = self.boulder_speed
            boulder.move_boulder()
    def check_level_up_all(self):
        global level_up_flag
        if level_up_flag:
            for boulder in self.boulder_pool:
                self.boulder_pool = []
                boulder.hideturtle()
                del boulder
            for hail in self.hail_pool:
                self.hail_pool = []
                hail.hideturtle()
                del hail
            self.hail_speed = int(round(self.hail_speed * 1.1))
            self.hail_spawn_chance = int(round(self.hail_spawn_chance * 0.9))
            self.boulder_spawn_chance = int(round(self.boulder_spawn_chance * 0.83))
            self.special_event_chance = int(round(self.special_event_chance * 0.95))
            self.boulder_speed = int(round(self.boulder_speed * 1.1))
            level_up_flag = False
                # Every level is 10% harder than the last
    def roll_hail_spawn_chance(self):
        if random.randint(1, self.hail_spawn_chance) == 2:
            if not self.hail_pool:
                temporary_object = OneHail()
                self.hail_active.append(temporary_object)
                temporary_object.move_speed = self.hail_speed

            else:
                e = self.hail_pool[0]
                self.hail_active.append(e)
                self.hail_pool.remove(e)
                e.goto(random.randint(-500, 500), 500)
                e.showturtle()

    def check_for_inactive_hail(self):
        for hail in self.hail_active[:]:
            if hail.ycor() < -500:
                self.hail_active.remove(hail)
                hail.hideturtle()
                self.hail_pool.append(hail)
    def move_all_hail(self):
        for hail in self.hail_active:
            hail.move_speed = self.hail_speed
            hail.move_hail()
    def special_event_roll(self):
        if random.randint(1, self.special_event_chance) == 2:
            for x in range(8):
                boulder = Boulder(True)
                if x == 0: boulder.goto((600, -350))
                elif x == 1: boulder.goto((700, -250))
                elif x == 2: boulder.goto((800, -350))
                elif x == 3: boulder.goto((900, -250))
                elif x == 4: boulder.goto((-600, -250))
                elif x == 5: boulder.goto((-700, -350))
                elif x == 6: boulder.goto((-800, -250))
                elif x == 7: boulder.goto((-900, -350))
                else: print("range logic mistake in hail_n_boulders at line 106")
                self.boulders_active.append(boulder)
                print("special thing happened")

















