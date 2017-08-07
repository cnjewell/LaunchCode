# from test import testEqual
#test must be from Runestone only...
import math

def sum_to(n):
    return int(round((n*(n+1))/2))

def sum_to_accum(n):
    sum = 0
    for num in range(n):
        sum = sum + num + 1
    return sum

def area_of_circle(r):
    return math.pi * r ** 2


def main():
    
    # Exercise 6
    print(sum_to(0))
    print(sum_to(5))
    print(sum_to(10))
    
    # Exercise 11
    print(sum_to_accum(100))


    # Chapter 5 - Weekly Graded Assignment
    t = area_of_circle(0)
    print(t)
    # testEqual(t, 0)
    t = area_of_circle(1)
    print(t)
    # testEqual(t,math.pi)
    t = area_of_circle(100)
    print(t)
    # testEqual(t, 31415.926535897932)
    t = area_of_circle(-1)
    print(t)
    # testEqual(t, math.pi)
    t = area_of_circle(-5)
    print(t)
    # testEqual(t, 25 * math.pi)
    t = area_of_circle(2.3)
    print(t)
    # testEqual(t, 16.61902513749)


if __name__ == "__main__":
    main()