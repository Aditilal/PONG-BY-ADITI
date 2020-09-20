import turtle

wn = turtle.Screen()
wn.title("Pong by @Aditi")
wn.bgcolor("black")
wn.setup(width=800 , height=600)
wn.tracer(0)
#score
score_a=0
score_b=0

#paddle A
paddle_a=turtle.Turtle()
paddle_a.shape("square")
paddle_a.speed(0)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)
paddle_a.shapesize(stretch_wid=5,stretch_len=1)






#paddle B
paddle_b=turtle.Turtle()
paddle_b.shape("square")
paddle_b.speed(0)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)
paddle_b.shapesize(stretch_wid=5,stretch_len=1)





#ball
ball=turtle.Turtle()
ball.shape("circle")
ball.speed(0)
ball.color("purple")
ball.penup()
ball.goto(0,0)
ball.dx=0.15
ball.dy=-0.15

#Scores
pen=turtle.Turtle()
pen.speed(0)
ball.penup()
pen.color("green")
pen.goto(0,260)

pen.write("Player A : 0      Player B :0",align="center",font=("Courier",26,"bold"))


#Function
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)
def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)
def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)
def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)
    

#keyboard work
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")



#Main game loop
while True:
    wn.update()

#ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
#border checking
    if ball.ycor() > 250:
        ball.sety(250) 
        ball.dy *=-1  
    if ball.ycor() < -250:
        ball.sety(-250) 
        ball.dy *=-1   
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1 
        score_a+=1
        pen.clear()
        pen.write("Player A : {}     Player B :{}".format(score_a,score_b),align="center",font=("Courier",26,"bold"))
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1 
        score_b+=1 
        pen.clear() 
        pen.write("Player A : {}     Player B :{}".format(score_a,score_b),align="center",font=("Courier",26,"bold"))   
# balls and collisions
    if ball.xcor() > 340 and ball.xcor()<350 and(ball.ycor() < paddle_b.ycor()+40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *=-1 
    if ball.xcor() < -340 and ball.xcor()>-350 and(ball.ycor() < paddle_a.ycor()+40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1             
                      
    

