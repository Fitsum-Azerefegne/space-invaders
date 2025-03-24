from turtle import Screen, Turtle
from spaceship import Spaceship
from bullets import Bullets
from invaders import create_invaders, move_invaders
import time
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Space invaders")
screen.tracer(0)

spaceship = Spaceship()
score_manager = Score(-380, 270)
invaders = create_invaders(5, 10)
invader_move_speed = 1.5
invader_direction = 1
invader_descend_amount = 20

spaceship.showturtle()
screen.listen()

screen.onkeypress(spaceship.start_move_left, "Left")
screen.onkeyrelease(spaceship.stop_move_left, "Left")
screen.onkeypress(spaceship.start_move_right, "Right")
screen.onkeyrelease(spaceship.stop_move_right, "Right")

bullets = []

def fire_bullet():
    if len(bullets) < 5:
        bullet = Bullets(spaceship)
        bullet.fire_bullet(spaceship)
        bullets.append(bullet)

def check_collisions(bullets, invaders, player_y_position):
    bullets_to_remove = []
    invaders_to_remove = []

    for bullet in bullets:
        for invader in invaders:
            if abs(bullet.xcor() - invader.xcor()) < 20 and abs(bullet.ycor() - invader.ycor()) < 20:
                bullets_to_remove.append(bullet)
                invaders_to_remove.append(invader)

    for bullet in bullets_to_remove:
        bullets.remove(bullet)
        bullet.hideturtle()
        del bullet

    for invader in invaders_to_remove:
        invaders.remove(invader)
        invader.hideturtle()
        del invader

screen.onkeypress(fire_bullet, "space")

global game_is_on
game_is_on = True

score = 0
game_over_text = Turtle()
game_over_text.hideturtle()
game_over_text.color("red")
game_over_text.penup()
player_y = -250

logo = Turtle()
logo.speed(0)
logo.color("white")
logo.penup()
logo.goto(0, 100)
logo.write("SPACE INVADERS", align="center", font=("Courier", 36, "bold"))

start_text = Turtle()
start_text.speed(0)
start_text.color("lightblue")
start_text.penup()
start_text.goto(0, -50)
start_text.write("Press any key to start", align="center", font=("Courier", 24, "normal"))

def start_game():
    logo.clear()
    logo.hideturtle()
    start_text.clear()
    start_text.hideturtle()
    screen.onkeypress(None, None) #Disable the any key press.
    run_game()

screen.onkeypress(start_game, None)

def run_game():
    global invaders
    global bullets
    global score_manager
    global game_is_on

    if 'invaders' in globals():
        for invader in invaders:
            invader.hideturtle()
            invader.goto(1000, 1000)
        invaders.clear()

    if 'bullets' in globals():
        for bullet in bullets:
            bullet.hideturtle()
            del bullet
        bullets.clear()

    if 'score_manager' in globals():
        score_manager.reset_score()

    invaders = create_invaders(5, 10)
    invader_move_speed = 1.5
    invader_direction = 1
    invader_descend_amount = 20

    bullets = []
    player_y = -250

    game_is_on = True

    def check_collisions(bullets_list, invaders_list, player_y_position):
        global game_is_on
        global score_manager
        bullets_to_remove = []
        invaders_to_remove = []

        for bullet in bullets_list:
            for invader in invaders_list:
                if abs(bullet.xcor() - invader.xcor()) < 20 and abs(bullet.ycor() - invader.ycor()) < 20:
                    bullets_to_remove.append(bullet)
                    invaders_to_remove.append(invader)
                    score_manager.increase_score(invader.value)

        for bullet in bullets_to_remove:
            if bullet in bullets_list:
                bullets_list.remove(bullet)
                bullet.hideturtle()
                del bullet

        for invader in invaders_to_remove:
            if invader in invaders_list:
                invaders_list.remove(invader)
                invader.hideturtle()
                del invader

        if not invaders_list:
            game_is_on = False
            return "win"

        for invader in invaders_list:
            if invader.ycor() < player_y_position:
                game_is_on = False
                return True

        return False

    while game_is_on:
        spaceship.move()
        invader_direction = move_invaders(invaders, invader_move_speed, invader_direction, invader_descend_amount)

        for invader in invaders:
            invader.animate()

        for bullet in bullets:
            bullet.move()
            if bullet.is_off_screen(screen.window_height()):
                bullet.hideturtle()
                bullets.remove(bullet)
                del bullet

        game_result = check_collisions(bullets, invaders, player_y)

        if game_result == "win":
            game_over_text.goto(0, 0)
            game_over_text.write("You Win!", align="center", font=("Courier", 36, "bold"))
            screen.update()
            time.sleep(3)
            break
        elif game_result:
            game_over_text.goto(0, 0)
            game_over_text.write("Game Over!", align="center", font=("Courier", 36, "bold"))
            screen.update()
            time.sleep(3)
            break

        screen.update()
        time.sleep(0.01)

screen.exitonclick()