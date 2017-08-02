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

def plot_yintercept_form(m, b, screen):
    '''
    Given the slope, m, and the y-intercept, b,
    return two (x,y) tuples to represent the ends of 
    the line based on the current bounds of the 
    plotting canvas/screen 
    '''
    pass

def plot_regression(textfile):
    infile = open(textfile, 'r')
    
    # load up all values into a list of tuples
    points = []
    aline = infile.readline()
    while aline:
        point = aline.split()
        points += [(int(point[0]), int(point[1]))]
        aline = infile.readline()
    
    # y = mx + b
    # m is slope, b is y-intercept, x is some arbitrary x

    # This y equation determines the y-intercept for the regression line
    # y = m * (x - mean(x)) + mean(y)
    
    # This m equation determines the slope of the regression line
    # m = sum(xi * yi - n * mean(x) * mean(y)) / sum(xi ** 2 - n * mean(x) ** 2)
    # n is the number of points    

    # To plot the line, I must pick an x? Any x? Or an x at the far edge of the data set?


    pass

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
    # plotRegression('labdata.txt')



if __name__ == "__main__":
    main()