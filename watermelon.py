import turtle
my_turtle = turtle.Turtle()

#def the green part of watermelon 
def draw_green(x,y,color):
    my_turtle.pensize(20)
    my_turtle.penup()
    my_turtle.goto(x,y)
    my_turtle.pendown()

    my_turtle.color(color)

#make range for this function 
    for g in range(1):
        my_turtle.setheading(-90)
        my_turtle.circle(110,180)

#def the red part of the watermelon 
def draw_red(x,y,color):
    my_turtle.pensize(15)
    my_turtle.penup()
    my_turtle.goto(x,y)
    my_turtle.pendown()

#I will write the color that I want this to be will be in main    
    my_turtle.color(color)

#this will allow me to fill in the red part
    my_turtle.begin_fill()

#make range for this function 
    for l in range(1):
        my_turtle.setheading(-90)
        my_turtle.circle(105,175)
        
#this will allow me to end my fill        
    my_turtle.end_fill()

#def the seed part of the watermelon 
def draw_seeds(x,y):
    my_turtle.pensize(10)
    my_turtle.penup()
    my_turtle.goto(x,y)
    my_turtle.pendown()

#pick a color for the seeds 
    my_turtle.color("black")

#this will allow me to fill in the seeds
    my_turtle.begin_fill()

#make range for this function 
    for s in range(1):
        my_turtle.circle(10)

#this will allow me to end my fill        
    my_turtle.end_fill()

#def a touchup that I realized needed to be made
def draw_line(x,y,size):
    my_turtle.pensize(20)
    my_turtle.penup()
    my_turtle.goto(x,y)
    my_turtle.pendown()

#this is where I chose the color of the line/touchup
    my_turtle.color("red")

    for r in range(1):
        my_turtle.setheading(0)
        my_turtle.forward(size)        

#this is the main function and the only one that I am calling
def main():
    my_turtle.speed(0)
    draw_green(0,0,"green")
    draw_red(5,10,"red")
    draw_line(5,10,208)
    draw_seeds(200,-20)
    draw_seeds(40,-20)
    draw_seeds(120,-25)
    draw_seeds(80,-70)
    draw_seeds(160,-73)

main()