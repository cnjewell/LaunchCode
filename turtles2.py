import turtle
import random

def is_in_screen(screen, t):
    left_bound = - screen.window_width() / 2
    right_bound = screen.window_width() / 2
    top_bound = screen.window_height() / 2
    bottom_bound = -screen.window_height() / 2

    turtle_x = t.xcor()
    turtle_y = t.ycor()

    still_in = True
    if turtle_x > right_bound or turtle_x < left_bound:
        still_in = False
    if turtle_y > top_bound or turtle_y < bottom_bound:
        still_in = False

    return still_in

def are_turtles_in_screen(screen):
    left_bound = - screen.window_width() / 2
    right_bound = screen.window_width() / 2
    top_bound = screen.window_height() / 2
    bottom_bound = -screen.window_height() / 2

    turtles_out = 0
    still_in = True

    for t in screen.turtles():
        turtle_x = t.xcor()
        turtle_y = t.ycor()

        if turtle_x > right_bound or turtle_x < left_bound:
            turtles_out += 1
        if turtle_y > top_bound or turtle_y < bottom_bound:
            turtles_out += 1

    if turtles_out:  #if any turtles added to turtles_out, False 
        return False
    else:
        return True  #if no turtles added, then True they are all in

def teleport_turtles(screen):
    for t in screen.turtles():
        original_speed = t.speed()
        t.penup()
        tx = (random.randrange(0, screen.window_width())) - screen.window_width() / 2
        ty = (random.randrange(0, screen.window_height())) - screen.window_height() / 2
        t.goto(tx, ty)
        t.pendown()
        t.speed(original_speed)

def is_turtle_disaster(screen, t):
    collisions = 0
    bound = 25
    for innocent_bystander in screen.turtles():
        ix = innocent_bystander.xcor()
        iy = innocent_bystander.ycor()
        tx = t.xcor()
        ty = t.ycor()
        if t == innocent_bystander:  # t can't collide with itself
            continue
        if (ix-bound < tx and tx < ix+bound) and (iy-bound < ty and ty < iy+bound):
            collisions += 1
    return collisions


def main():
    wn = turtle.Screen()             # Set up the window and its attributes
    wn.bgcolor("lightgreen")


    #### Chapter 8 ####
    tess = turtle.Turtle()           # create tess and set some attributes
    tess.color("red")
    tess.pensize(1)
    tess.speed(0)
    tess.shape('turtle')

    alex = turtle.Turtle()
    alex.color("blue")
    alex.pensize(1)
    alex.speed(0)
    alex.shape('turtle')

    # Exercise 2
    # while is_in_screen(wn, tess):
    #     coin = random.randrange(0, 2)
    #     if coin == 0:
    #        tess.left(90)
    #     else:
    #        tess.right(90)

    # Exercise 3
    # teleport_turtles(wn) # random 'starting' point for all turtles in screen

    # while are_turtles_in_screen(wn):    
    #     for t in wn.turtles():
    #         t.left(random.randrange(0, 360))
    #         t.forward(50)

    # Exercise 4
    everybody_panic = False
    while everybody_panic == False:
        for t in wn.turtles():
            t.left(random.randrange(0, 6)*60) # think limited angle is prettier
            t.forward(50)
            if is_in_screen(wn, t) == False:
                t.back(50)
                t.dot() # dots where the turtle backs up to 
            if is_turtle_disaster(wn, t):
                t.stamp() # stamp on collisions
                t.back(50)

    wn.exitonclick()
    

if __name__ == "__main__":
    main()

