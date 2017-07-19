import turtle

def draw_polygon(t, sides, color="hotpink", length=50, fill="purple"):
    t.color(color)
    t.fillcolor(fill)
    t.begin_fill() 
    for side in range(sides):
        t.forward(length)
        t.left(360/sides)
    t.end_fill()

def draw_star(t, points):
    for num in range(points):
        t.forward(100)
        t.right(180-180/points)

def draw_path(t, turns_list):
    for turn in turns_list:
        t.left(turn)
        t.forward(100)

def draw_sprite(t, legs):
    
    for leg in range(legs):
        t.forward(50)
        t.back(50)
        t.right(360/legs)


def main():
    wn = turtle.Screen()             # Set up the window and its attributes
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()           # create tess and set some attributes
    tess.color("red")
    tess.pensize(2)

    # Unit 1, Chapter 4
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
    # Draw a sprite with n legs, where n is given with input()
    #draw_sprite(tess, 12)



    wn.exitonclick()

if __name__ == "__main__":
    main()


#### Turtle code to canabalize later. ####

# def draw_bar(t, height):
#     """ Get turtle t to draw one bar, of height. """
#     t.begin_fill()               # start filling this shape
#     t.left(90)
#     t.forward(height)
#     t.write(str(height))
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()                 # stop filling this shape

# def main():
#     data = [48, 117, 200, 240, 160, 260, 220]
#     max_height = max(data)
#     num_bars = len(data)
#     border = 10

#     wn = turtle.Screen()             # Set up the window and its attributes
#     wn.setworldcoordinates(0-border, 0-border, 40 * num_bars + border, max_height + border)
#     wn.bgcolor("lightgreen")

#     tess = turtle.Turtle()           # create tess and set some attributes
#     tess.color("blue")
#     tess.fillcolor("red")
#     tess.pensize(3)

#     for x in data:
#         draw_bar(tess, x)

#     wn.exitonclick()

# if __name__ == "__main__":
#     main()

