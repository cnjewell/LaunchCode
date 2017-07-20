# Studio Problems
import turtle

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

def main():
    # holiday()     # Studio 1
    # donuts()      # Studio 2

    # Studio 3 is a turtle race, I'll just use some of my other turtle code....

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
    press = ["a reporter from the Times", "a reporter from the Observer"]
    family_etc = ["Mycroft Holmes", "Mrs. Hudson"]
    enemies = ["Professor Moriarty", "Charles Augustus Milverton", "John Woodley"]
    potential_love_interest = ["Irene Adler"]
    friends = ["Inspector Lestrade", "Dr. Watson"]

    print(sherlock(press))
    print(sherlock(family_etc))
    print(sherlock(enemies))
    print(sherlock(potential_love_interest))
    print(sherlock(friends))

if __name__ == "__main__":
    main()