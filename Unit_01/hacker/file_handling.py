import turtle

def sevenscores():
    infile = open('studentdata.txt', 'r')

    studentline = infile.readline()
    while studentline:
        items = studentline.split()
        if len(items) > 7:
            dataline = items[0]
            print(dataline)
        studentline = infile.readline() 
    
    infile.close()

def student_avg():
    infile = open('studentdata.txt', 'r')

    studentline = infile.readline()
    while studentline:
        items = studentline.split()
        studentavg = 0
        for score in items[1:]:
            studentavg += int(score)
        studentavg = studentavg / len(items[1:])
        print(items[0], studentavg)
        studentline = infile.readline()
    
    infile.close()

def student_min_max():
    infile = open('studentdata.txt', 'r')

    studentline = infile.readline()
    while studentline:
        items = studentline.split()
        scores = [int(score) for score in items[1:]]
        print(items[0], max(scores), min(scores))
        studentline = infile.readline()
    
    infile.close()

def plot_regression(textfile):
    infile = open(textfile, 'r')
    
    # load up all values into a list of tuples
    points = []
    aline = infile.readline()
    while aline:
        point = aline.split()
        points += [(int(point[0]), int(point[1]))]
        
        aline = infile.readline()
    print(points)

    # Calulate m and y
    point_count = len(points)
    mean_x = sum([row[0] for row in points]) / point_count 
    mean_y = sum([row[1] for row in points]) / point_count
    
    sum_top = 0
    sum_btm = 0
    for x,y in points:
        sum_top = x * y - point_count * mean_x * mean_y
        sum_btm = x ** 2 - point_count * mean_x ** 2
    
    regression_slope = sum_top/sum_btm
    print(regression_slope)

    # Max and min to determine length of regression line
    max_x = max([row[0] for row in points])
    max_y = max([row[1] for row in points])
    min_x = min([row[0] for row in points])
    min_y = min([row[1] for row in points])

    abs_max = abs(max([max_x, max_y, min_x, min_y]))
    abs_min = abs(min([max_x, max_y, min_x, min_y]))

    y_intercept = regression_slope * (max_x - mean_x) + mean_y
    print(y_intercept)

    rightmost_y = regression_slope * max_x
    leftmost_y  = regression_slope * min_x

    ## START TURTLE CRAP ##
    wn = turtle.Screen()
    #llx, lly, urx, ury
    wn.setworldcoordinates(abs_min - 50, abs_min - 50, abs_max + 50, abs_max + 50)
    
    alex = turtle.Turtle()
    alex.hideturtle()

    # draw plane lines 
    alex.color('red')
    alex.penup()
    alex.goto(0, 0)
    alex.pendown()
    for increment in range(10, max_x, 10):
        alex.goto(increment, 0)
        alex.write(increment)

    alex.penup()
    alex.goto(0, 0)
    alex.pendown()
    alex.goto(0, max_y)
    for increment in range(10, max_y, 10):
        alex.goto(0, increment)
        alex.write(increment, align="right")

    alex.color('black')
    # plot data points
    for point in points:
        alex.penup()
        alex.goto(point[0], point[1])
        alex.pendown()
        alex.dot()
        alex.write(point)

    # plot regression line thing 
    alex.penup()
    alex.goto(min_x, leftmost_y)
    alex.pendown()
    alex.goto(max_x, rightmost_y)

    wn.exitonclick()

    # y_intercept = m * (x - mean(x)) + mean(y)
    # regression_slope = sum(xi * yi - point_count * mean(x) * mean(y)) / sum(xi ** 2 - point_count * mean(x) ** 2)

    # y = mx + b
    # m is slope, b is y-intercept, x is some arbitrary x

    # This y equation determines the y-intercept for the regression line
    # y = m * (x - mean(x)) + mean(y)
    
    # This m equation determines the slope of the regression line
    # m = sum(xi * yi - n * mean(x) * mean(y)) / sum(xi ** 2 - n * mean(x) ** 2)
    # n is the number of points    

def mystery_plot(textfile, t):
    infile = open(textfile, 'r')

    aline = infile.readline()
    while aline:
        if aline == "UP\n":
            t.penup()
        elif aline == "DOWN\n":
            t.pendown()
        else:
            point = aline.split()
            t.goto(int(point[0]), int(point[1]))
        aline = infile.readline()

    infile.close()

def main():
    print()
    # sevenscores()
    # student_avg()
    # student_min_max()
    plot_regression('labdata.txt')
    

if __name__ == "__main__":
    main()