import turtle
import random

def draw_polygon(t, sides, color="hotpink", length=50, fill="purple"):
    t.color(color)
    t.fillcolor(fill)
    t.begin_fill() 
    for side in range(sides):
        t.forward(length)
        t.left(360/sides)
    t.end_fill()

def draw_equi_triangle(t, size):
    draw_polygon(t, 3, length=size)

def draw_square(t, length=50):
    for side in range(4):
        t.forward(length)
        t.left(90)

def draw_star(t, points):
    for num in range(points):
        t.forward(100)
        t.right(180-180/points)

def draw_path(t, turns_list):
    for turn in turns_list:
        t.left(turn)
        t.forward(100)

def draw_sprite(t, legs, length=50):
    for leg in range(legs):
        t.forward(50)
        t.back(50)
        t.right(360/legs)

def draw_fancy_square(t, size, sprite_size, sprite_legs):
    for i in range(4):
        t.forward(size)
        draw_sprite(t, sprite_legs, length=sprite_size)
        t.left(90)

def draw_spiral(t, offset, angle, layers):
    accum = 2
    for i in range(layers):
        t.left(angle)
        t.forward(accum)
        accum += offset

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    if height >= 200:
        t.fillcolor("red")
    elif height >= 100 and height < 200:
        t.fillcolor("yellow")
    else:
        t.fillcolor("green")
        
    t.begin_fill()               # start filling this shape
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape

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

def main():
    wn = turtle.Screen()             # Set up the window and its attributes
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()           # create tess and set some attributes
    tess.color("red")
    tess.pensize(2)



    #### CHAPTER 4 ####
    # Exercise 5 & 6
    #draw_polygon(tess, 5)

    # Exercise 7
    pirate_path = [160, -43, 270, -97, -43, 200, -940, 17, -86]
    #draw_path(tess, pirate_path)

    # Exercise 9
    #draw_star(tess, 7)

    # Exercise 11
    # Creative Turtle drawing

    # Exercise 13
    # draw_sprite(tess, 12)

    #### CHAPTER 5 ####
    # Exercise 1
    # for num in range(4):
    #     draw_polygon(tess, 4, length=20)
    #     tess.penup()
    #     tess.forward(40)
    #     tess.pendown()    

    # Exercise 2
    # sz = 20
    # for num in range(5):
    #     draw_square(tess, length=sz)
    #     tess.penup()
    #     tess.right(90)
    #     tess.forward(10)
    #     tess.right(90)
    #     tess.forward(10)
    #     tess.right(180)
    #     tess.pendown()
    #     sz += 20

    # Exercise 3
    # draw_polygon(tess, 8, length=50)



    # Exercise 4
    # alex = turtle.Turtle()
    # alex.color("blue")
    # alex.pensize(1)
    # alex.speed(0)

    # tess.speed(0)

    # draw_spiral(alex, 1.5, 89, 150)
    # draw_spiral(tess, 2, 90, 150)



    # Exercise 5
    # draw_equi_triangle(tess, 30)

    # Exercise 7
    # draw_star(tess, 5)

    # Exercise 8
    # tess.penup()
    # tess.left(180)
    # tess.forward(200)
    # tess.left(180)
    # tess.pendown()  #initialize start position so it fits

    # for i in range(5):
    #     draw_star(tess, 5)
    #     tess.penup()
    #     tess.forward(350)
    #     tess.right(144)
    #     tess.pendown()

    # Exercise 9
    # Already n-pointed star fn

    # Exercise 10
    # draw_sprite(tess, 9, length=100)

    # Exercise 12 - "Fancy Square"
    # draw_fancy_square(tess, 100, 150, 12)

    ### Chapter 6 ####
    # Exercise 3 & 4
    # data = [48, 117, 200, 240, 160, 260, 220]

    # Not sure how to make negative work...
    
    # max_height = max(data)
    # min_height = min(data)
    # num_bars = len(data)
    # border = 10
    # wn.setworldcoordinates(0-border, 0-border, 40 * num_bars + border, max_height + border)

    # for x in data:
    #     draw_bar(tess, x)


    wn.exitonclick()

if __name__ == "__main__":
    main()

