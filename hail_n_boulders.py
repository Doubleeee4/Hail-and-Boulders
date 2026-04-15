from turtle import Turtle
import random
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
class Boing(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("circle")
        self.delay = 0
        self.shapesize(1.5, 1.5)
        self.color("maroon")
        self.hideturtle()
        self.move_speed = 9
        self.horizontal_spawn_side = ""
        self.vertical_tracker = "down"
        coinflip = random.randint(1,2)
        if coinflip == 1:
            self.goto(600, random.randint(-350, -240))
            self.horizontal_spawn_side = "r"
        else:
            self.goto(-600, random.randint(-350, -240))
            self.horizontal_spawn_side = "l"
    def boing_move(self):
        self.showturtle()
        if self.vertical_tracker == "up":
            if self.horizontal_spawn_side == "r":self.goto(self.xcor()-self.move_speed, self.ycor()+self.move_speed)
            if self.horizontal_spawn_side == "l": self.goto(self.xcor() + self.move_speed,self.ycor() + self.move_speed)
        if self.vertical_tracker == "down":
            if self.horizontal_spawn_side == "r":self.goto(self.xcor()-self.move_speed, self.ycor()-self.move_speed)
            if self.horizontal_spawn_side == "l": self.goto(self.xcor() + self.move_speed,self.ycor() - self.move_speed)
    def xy_check(self):
        if self.ycor() < -373:
            self.vertical_tracker = "up"
        if self.ycor() > -210:
            self.vertical_tracker = "down"
        if self.xcor() > 468:
            e = self.delay
            self.delay = 60
            if random.randint(1,4) == 1 and e < 1:
                self.horizontal_spawn_side = "r"
        if self.xcor() < -470:
            e = self.delay
            self.delay = 60
            if random.randint(1,4) == 1 and e < 1:
                self.horizontal_spawn_side = "l"

        self.delay -= 1
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

        self.showturtle()

    def move_boulder(self):
        if self.spawn_side == "r":
            self.setx(self.xcor() - self.move_speed)
        elif self.spawn_side == "l":
            self.setx(self.xcor() + self.move_speed)
class HailNBoulders:
    def __init__(self):
        self.boulder_speed_unrounded = 4
        self.boing_speed_unrounded = 5
        self.hail_speed_unrounded = 6
        self.level_tracker = 0
        self.boulders_active = []
        self.boulder_spawn_chance = 120
        self.boing_active = []
        self.boing_spawn_chance = 200
        self.hail_active = []
        self.hail_spawn_chance = 30
        self.special_event_chance = 10000
        self.boulder_pool = []
        self.boing_pool = []
        self.hail_pool = []
        self.hail_speed = 6
        self.boulder_speed = 4
        self.boing_speed = 5
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
                self.boulder_pool[0].move_speed = self.boulder_speed
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
    def roll_boing_spawn_chance(self):
        if random.randint(1, self.boing_spawn_chance) == 2 and self.delay < 0:
            if self.level_tracker > 4:
                if not self.boing_pool:
                    temporary_object = Boing()
                    temporary_object.delay = 60
                    self.boing_active.append(temporary_object)
                    temporary_object.move_speed = self.boing_speed
                    self.delay = 30
            elif self.delay < 0 and self.level_tracker > 5:
                self.boing_pool[0].showturtle()
                self.boing_pool[0].delay = 60
                coinflip = random.randint(1, 2)
                if coinflip == 1:
                    self.boing_pool[0].goto(600, random.randint(-350, -240))
                    self.boing_pool[0].horizontal_spawn_side = "r"
                else:
                    self.boing_pool[0].goto(-600, random.randint(-350, -240))
                    self.boing_pool[0].horizontal_spawn_side = "l"
                self.boing_active.append(self.boing_pool[0])
                self.boing_pool.remove(self.boing_pool[0])
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
    def check_for_inactive_boing(self):
        for boing in self.boing_active[:]:
            if -600 > boing.xcor() or boing.xcor() > 700:
                self.boing_active.remove(boing)
                boing.hideturtle()
                if boing.horizontal_spawn_side == "l":
                    boing.setx(-600)
                else:
                    boing.setx(600)
                self.boing_pool.append(boing)
    def move_all_boulders(self):
        for boulder in self.boulders_active:
            boulder.move_speed = self.boulder_speed
            boulder.move_boulder()
    def move_all_boing_and_y_check(self):
        for boing in self.boing_active:
            boing.move_speed = self.boing_speed
            boing.boing_move()
            boing.xy_check()
    def check_level_up_all(self):
        global level_up_flag
        if level_up_flag:
            self.level_tracker += 1
            for boulder in self.boulder_pool:
                self.boulder_pool = []
                boulder.hideturtle()
                del boulder
            for hail in self.hail_pool:
                self.hail_pool = []
                hail.hideturtle()
                del hail
            for boing in self.boing_pool:
                self.boing_pool = []
                boing.hideturtle()
                del boing
            if self.level_tracker < 10:
                self.hail_speed_unrounded = self.hail_speed_unrounded * 1.1
                self.boulder_speed_unrounded = self.boulder_speed_unrounded * 1.1
            self.hail_spawn_chance = int(round(self.hail_spawn_chance * 0.9))
            self.boulder_spawn_chance = int(round(self.boulder_spawn_chance * 0.83))
            self.special_event_chance = int(round(self.special_event_chance * 0.95))
            if self.level_tracker > 5:
                self.boing_spawn_chance = int(round(self.boing_spawn_chance * 0.93))
            if 11 > self.level_tracker > 5:
                self.boing_speed_unrounded = self.boing_speed_unrounded * 1.1
            if self.level_tracker > 11:
                self.hail_spawn_chance = int(round(self.hail_spawn_chance * 0.8))
                self.boulder_spawn_chance = int(round(self.boulder_spawn_chance * 0.8))
                self.boing_spawn_chance = int(round(self.boing_spawn_chance * 0.8))
            self.boulder_speed = round(self.boulder_speed_unrounded)
            self.boing_speed = round(self.boing_speed_unrounded)
            self.hail_speed = round(self.hail_speed_unrounded)
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
            for x in range(20):
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


















