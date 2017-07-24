# Studio Problems
import turtle
import random

def holiday():
    start = int(input('Start Date: '))
    length = int(input('Vacation Length: '))

    print("Day number you've returned on: ", (start + length) % 7)

def donuts():
    print("Welcome to the Loop Hole!")
    print("Today's Manager's Special is:")
    print("Crunch Jelly: A traditional jelly donut in which the jelly filling is made entirely of Capn' Crunch Oops! All Berries")
    qty = float(input("How many would you like? "))
    # >>> 3.33333
    retail = float(input("How much would you like to pay per donut (suggested price is $4.35 each)? "))
    # >>> 2.5
    print("Ok, let me prepare that for you....")
    total = round(retail * qty * 1.05, 2)
    print("After tax, your total is:", total)
    print("Thank you for snacking! Loop back around here soon!")

def turtle_racing():
    wn = turtle.Screen()       
    wn.bgcolor('lightblue')

    lance = turtle.Turtle()    
    andy = turtle.Turtle()
    lance.color('red')
    andy.color('blue')
    lance.shape('turtle')
    andy.shape('turtle')

    andy.up()                 
    lance.up()
    andy.goto(-100,20)
    lance.goto(-100,-20)

    for n in range(random.randrange(6, 10)):
        for t in wn.turtles():
            t.forward(random.randrange(2, 50))

    wn.exitonclick()

def wagon_wheel(t):
    # draw 4 squares rotated around the origin
    size = 100
    for num in range(5):
        for num in range(4):
            t.right(90)
            for num in range(4):
                t.forward(size)
                t.right(90)
        t.right(360/5)
    # draw them again, this time at a 360/6 turn

def accum_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fibA = 0
        fibB = 1
        for num in range(1, n):
            fibC = fibA + fibB
            fibA = fibB
            fibB = fibC
        return fibB

def recursive_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_fib(n-2) + recursive_fib(n-1)

def dynamic_fib(n):
    fibs = {0:0, 1:1}
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n in fibs:
        return fibs[n]
    else:
        for num in range(2, n+1):
            newfib = fibs[num-2] + fibs[num-1]
            fibs[num] = newfib
        return fibs[n]

def sherlock(guests):
   for guest in guests:
        if guest == "Dr. Watson" or guest == "Inspector Lestrade":
            return "Enter"
        else:
            return "Go Away! (sound of violin music...)"

def times_tables(n):
    for i in range(n+1):
        for j in range(n+1):
            print(i * j,'\t', end='')
        print('')

def roshambo():
    best_of = int(input("Best of how many games? "))
    games_to_win = (best_of//2)+1
    
    cpu_score = 0
    ply_score = 0

    while cpu_score < games_to_win and ply_score < games_to_win:
        ply = int(input("Rock (0), Paper (1), or Scissors (2)? "))
        cpu = random.randrange(0,2)
        throw = (ply, cpu)
        if ply == cpu:
            print("Tie. No score this round.")
        elif throw == (1,0) or throw == (2,1) or throw == (0,2):
            ply_score += 1
        else:
            cpu_score += 1
        print("Current Score:")
        print("Player:", ply_score, "CPU:", cpu_score)
    if cpu_score > ply_score:
        print("CPU Wins!")
    else:
        print("Player Wins!")   

def main():
    # holiday()     # Studio 1
    # donuts()      # Studio 2

    # Studio 3 is a turtle race, I'll just use some of my other turtle code....
    # turtle_racing()

    # wagon_wheel() # Studio 4
    # wn = turtle.Screen()
    # wn.bgcolor("lightgreen")

    # tess = turtle.Turtle()
    # tess.color("red")
    # tess.pensize(1)
    # tess.speed(0)

    # wagon_wheel(tess)

    # wn.exitonclick()

    # print(recursive_fib(0))
    # print(recursive_fib(1))
    # print(recursive_fib(2))
    # print(recursive_fib(3))
    # print(recursive_fib(4))
    # print(recursive_fib(30))

    # print(dynamic_fib(0))
    # print(dynamic_fib(1))
    # print(dynamic_fib(2))
    # print(dynamic_fib(3))
    # print(dynamic_fib(4))
    # print(dynamic_fib(100))

    # print(accum_fib(0))
    # print(accum_fib(1))
    # print(accum_fib(2))
    # print(accum_fib(3))
    # print(accum_fib(4))
    # print(accum_fib(100))

    # Studio 5
    # press = ["a reporter from the Times", "a reporter from the Observer"]
    # family_etc = ["Mycroft Holmes", "Mrs. Hudson"]
    # enemies = ["Professor Moriarty", "Charles Augustus Milverton", "John Woodley"]
    # potential_love_interest = ["Irene Adler"]
    # friends = ["Inspector Lestrade", "Dr. Watson"]

    # print(sherlock(press))
    # print(sherlock(family_etc))
    # print(sherlock(enemies))
    # print(sherlock(potential_love_interest))
    # print(sherlock(friends))

    # Studio 6

    # Bonus Missions - Mission 1
    # times_tables(6)

    # Bonus Missions - Mission 2
    roshambo()

if __name__ == "__main__":
    main()