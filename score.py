from turtle import Turtle

class Score:
    def __init__(self, x, y):
        self.score = 0
        self.display = Turtle()
        self.display.speed(0)
        self.display.color("white")
        self.display.penup()
        self.display.hideturtle()
        self.display.goto(x, y)
        self.update_display()

    def increase_score(self, amount):
        self.score += amount
        self.update_display()

    def update_display(self):

        self.display.clear()
        self.display.write(f"Score: {self.score}", align="left", font=("Courier", 18, "normal"))

    def get_score(self):
        return self.score

    def reset_score(self):
        self.score = 0
        self.update_display()