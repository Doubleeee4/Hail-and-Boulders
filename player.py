import turtle



class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("circle")
        self.color("red")
        self.shapesize(2, 2)
        self.goto((0,-300))
        self.speed("fastest")
    def move_up(self):
        if self.ycor() <= -215:
            self.goto((self.xcor(), self.ycor() + 5))
    def move_down(self):
        if self.ycor() >= -369:
            self.goto((self.xcor(), self.ycor() - 5))
    def move_right(self):
        if self.xcor() <= 465:
            self.goto((self.xcor() + 5, self.ycor()))
    def move_left(self):
        if self.xcor() >= -470:
            self.goto((self.xcor() - 5, self.ycor()))





