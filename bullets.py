from turtle import Turtle

class Bullets(Turtle):
    def __init__(self, spaceship):
        super().__init__()
        self.color("red")
        self.shape("triangle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.setheading(90)
        self.goto(spaceship.xcor(), spaceship.ycor() + 20)
        self.move_speed = 10
        self.state = "ready"

    def fire_bullet(self, spaceship):
        if self.state == "ready":
            self.state = "fire"
            self.goto(spaceship.xcor(), spaceship.ycor() + 20)

    def move(self):
        if self.state == "fire":
            self.forward(self.move_speed)

    def is_off_screen(self, screen_height):
        return self.ycor() > screen_height / 2