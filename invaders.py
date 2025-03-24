from turtle import Turtle
class Invader(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("lightgreen")
        self.penup()
        self.goto(x, y)
        self.speed(0)
        self.move_speed = 1.5
        self.direction = 1
        self.animation_frames = ["square", "triangle"]
        self.frame_index = 0
        self.animation_timer = 0
        self.animation_delay = 20
        self.value = 10
        self.descend_amount = 20  # How much the invaders descend
    def destroy(self):
        self.hideturtle()
        self.goto(1000, 1000)

    def animate(self):
        self.animation_timer += 1
        if self.animation_timer >= self.animation_delay:
            self.animation_timer = 0
            self.frame_index = (self.frame_index + 1) % len(self.animation_frames)
            self.shape(self.animation_frames[self.frame_index])

def move_invaders(invaders, move_speed, direction, descend_amount):
        """Moves all invaders as a group."""
        rightmost = max(invader.xcor() for invader in invaders)
        leftmost = min(invader.xcor() for invader in invaders)
        if abs(rightmost) > 360 or abs(leftmost) > 350:
            direction *= -1
            for invader in invaders:
                invader.goto(invader.xcor(), invader.ycor() - descend_amount)

        for invader in invaders:
            new_x = invader.xcor() + (move_speed * direction)
            invader.goto(new_x, invader.ycor())
        return direction


def create_invaders(rows, columns):
        invaders = []
        for row in range(rows):
            for col in range(columns):
                x = -200 + (col * 50)
                y = 200 - (row * 50)
                invader = Invader(x, y)
                invaders.append(invader)
        return invaders