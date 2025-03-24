from turtle import Turtle

class Spaceship(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("turtle")
        self.penup()
        self.move_speed = 5 # Move by 10 pixels
        self.setheading(90)
        self.goto(0, -250)
        self.moving_left = False
        self.moving_right = False
        self.screen_width = 800

    def start_move_left(self):
        self.moving_left = True

    def stop_move_left(self):
        self.moving_left = False

    def start_move_right(self):
        self.moving_right = True

    def stop_move_right(self):
        self.moving_right = False

    def move(self):
        if self.moving_left:
            new_x = self.xcor() - self.move_speed  # Move left by 10 pixels
            if new_x > -self.screen_width / 2 + 25:  # Check left boundary
                self.goto(new_x, self.ycor())
        if self.moving_right:
            new_x = self.xcor() + self.move_speed  # Move right by 10 pixels
            if new_x < self.screen_width / 2 - 25:  # Check right boundary
                self.goto(new_x, self.ycor())