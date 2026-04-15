from turtle import Turtle
import hail_n_boulders


class Text(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.level = 0
        self.level_pb = int(str(open("Level PB.txt").read()))
        self.speed("fastest")
        self.goto(0, 350)
        self.level_scale = 3
        self.font = ('Arial', 20, 'normal')
        self.first_writing = True
        self.clock_ = 0

    def rewrite_plus_level_update(self):
        if self.clock_ == int(self.clock_) or self.first_writing:
            hail_n_boulders.level_up_flag = True
            self.first_writing = False
            self.level_scale += 10
            self.level += 1
            if self.level > self.level_pb:
                self.level_pb = self.level
            self.clear()
            self.goto(0, 350)
            self.write(f"Level:{self.level} Personal best:{self.level_pb}", False, "center", self.font )
            self.pu()
            self.goto(-500, -190)
            self.pd()
            self.goto(500, -190)
            self.pu()



    def game_over_text(self):
        self.goto(0, 0)
        self.write("Game Over", False, "center", self.font)

    def save_level_pb(self):
        with open("Level PB.txt", "w") as data:
            data.write(str(self.level_pb))

    def level_clock(self):
        self.clock_ = round(self.clock_ + 0.002, 3)