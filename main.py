"""
Name: Vraj Bhavsar
About: This is a game built with Python called Paddle Board. Two players must play for the full thrilling experience of this game.

"""
import turtle

window = turtle.Screen()
window.title("Paddle Board Game By Vraj Bhavsar")
window.bgcolor('white')
window.setup(width=800, height=620)
window.tracer(0)

#left paddle 
left_paddle = turtle.Turtle()
left_paddle.color("blue")
left_paddle.shape('square')
left_paddle.penup()
left_paddle.shapesize(stretch_wid = 5, stretch_len = 1)
left_paddle.goto(-350,0)

#right paddle 
right_paddle = turtle.Turtle()
right_paddle.color("blue")
right_paddle.shape('square')
right_paddle.penup()
right_paddle.shapesize(stretch_wid = 5, stretch_len = 1)
right_paddle.goto(350,0)

#paddle ball 
paddle_ball = turtle.Turtle()
paddle_ball.color("black")
paddle_ball.shape("circle")
paddle_ball.goto(0,0)
paddle_ball.penup()
paddle_ball_x = 0.1
paddle_ball_y = 0.1

#score
score = turtle.Turtle()
score.color("red")
score.penup()
score.hideturtle()
score.goto(0,240)
score.write("You: 0  Opponent: 0", align = "center", font = ("Hydrophilia Iced", 24, "normal"))

score_you = 0
score_opp = 0

#main function
def left_paddle_upwards():
    y = left_paddle.ycor()
    y += 30
    left_paddle.sety(y)

def left_paddle_downwards():
    y = left_paddle.ycor()
    y -= 30
    left_paddle.sety(y)

def right_paddle_upwards():
    y = right_paddle.ycor()
    y += 30
    right_paddle.sety(y)

def right_paddle_downwards():
    y = right_paddle.ycor()
    y -= 30
    right_paddle.sety(y)

window.listen()
window.onkeypress(left_paddle_upwards, 'w')
window.onkeypress(left_paddle_downwards, 's')
window.onkeypress(right_paddle_upwards, 'Up')
window.onkeypress(right_paddle_downwards, 'Down')

while True:
    window.update()
    paddle_ball.setx(paddle_ball.xcor() + paddle_ball_x)
    paddle_ball.sety(paddle_ball.ycor() + paddle_ball_y)

    if paddle_ball.ycor() > 290:
        paddle_ball.sety(290)
        paddle_ball_y *= -1
    elif paddle_ball.ycor() < -290:
        paddle_ball.sety(-290)
        paddle_ball_y *= -1

    if paddle_ball.xcor() < -330 and paddle_ball.ycor() < left_paddle.ycor() + 50 and paddle_ball.ycor() > left_paddle.ycor() -50:
        paddle_ball_x *= -1
    elif paddle_ball.xcor() > 330 and paddle_ball.ycor() < right_paddle.ycor() + 50 and paddle_ball.ycor() > right_paddle.ycor() - 50:
        paddle_ball_x *= -1


    if paddle_ball.xcor() > 385:
        score_you += 1
        score.clear()
        score.write("You: {} Opponent: {}".format(score_you, score_opp), align='center', font=('Hydrophilia Iced', 24, 'normal'))
        paddle_ball.goto(0,0)
        paddle_ball_x *= -1

    elif paddle_ball.xcor() < -385:
        score_opp += 1
        score.clear()
        score.write("You: {} Opponent: {}".format(score_you, score_opp), align='center', font=('Hydrophilia Iced', 24, 'normal'))
        paddle_ball.goto(0, 0)
        paddle_ball_x *= -1









