# Studio Problems
import turtle
import random
import string

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

def is_sorted(string):
    '''Returns True if string is sorted from least to greatest, otherwise False'''
    for char_index in range(len(string)-1):
        if string[char_index] > string[char_index+1]:
            return False
    else:
        return True

def char_after_intro(string):
    after_comma = False
    for index, char in enumerate(string):
        if char in ",":
            after_comma = True
        if after_comma == True:
            return len(string[index+1:])
    else:
        return 0

def pig_latinizer(string):
    words_list = string.split()
    latinized_output = ''
    for index, word in enumerate(words_list):
        if word[0] in "AaEeIiOoUu":
            #If the first letter of word is a vowel, don't move the first letter to end
            latinized_output += word + 'ay'
        else:
            latinized_output += word[1:] + word[0] + 'ay'
        if index != len(words_list)-1:
            # Add a space between words, unless this is the first word!
            latinized_output += ' '
    return latinized_output
    # final_string = ' '.join(latinized)
    # return final_string

def print_every(i, nums):
    for index in range(0, len(nums), i):
        print(nums[index])

def check_group(ages):
    for age in ages:
        if age < 70:
            return False
    else:
        return True

def password_checker(password):
    """
    A valid password has no spaces,
    and at least one non-alphabetical character
    """
    non_alpha = 0
    for char in password:
        if not(char.isalpha()) and char != " ":
            non_alpha += 1

    if " " not in password and non_alpha:
        return True
    else:
        return False

def stretch(to_stretch, stretch_value=2, stretch_chars=string.ascii_lowercase):
    stretched_output = ''
    for char in to_stretch:
        if char in stretch_chars:
            stretched_output += char * stretch_value
        else:
            stretched_output += char
    return stretched_output

def bubble_sort(sortlist):
    is_sorted = False
    num_swaps = 1
    while num_swaps > 0:
        num_swaps = 0 ## Number of swaps made
        for index in range(0, len(sortlist)-1):
            a = sortlist[index] 
            b = sortlist[index + 1]
            if a > b:
                sortlist[index] = b
                sortlist[index + 1] = a
                num_swaps += 1
    else:
        return sortlist
    
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
    # roshambo()

    # Studio 7 - Sorted
    # print(is_sorted('ABC'))
    # print(is_sorted('aBc'))
    # print(is_sorted('dog'))

    # Studio 7 - Bonus Mission #1
    # print(char_after_intro("Before you go to bed, you need to brush your teeth."))
    # print(char_after_intro("Under the warm sun, the cat slept deeply."))

    # Studio 7 - Bonus Mission #2
    # print(pig_latinizer("python code wins"))
    # print(pig_latinizer("all open androids"))

    # Studio 8 - Bugz 
    # 01 - Printing the ith element
    # in a list of numbers, print every ith number
    # print_every(3, [4, 7, 2, 10, 1, 0, 9, 6])
    # should print 4, then print 10, then print 9

    # 02 - Seniors Bar
    # this group should not be allowed inside the bar
    # group = [78, 71, 25, 84]
    # print(check_group(group), False)

    # # this group should also not be allowed inside the bar
    # group2 = [ 2, 99 ]
    # print(check_group(group2), False)

    # # this loner is allowed
    # group3 = [ 99 ]
    # print(check_group(group3), True)

    # 03 - Password Check
    # pw1 = "i <3 makonnen"
    # print(password_checker(pw1), False)
    # # should print False


    # pw2 = "puzzlesareforfun"
    # print(password_checker(pw2), False)
    # # should print False

    # pw2 = "puzzlesr4fun"
    # print(password_checker(pw2), True)
    # # should print True

    # Studio 8 - Bonus Missions
    # Stretch
    # print(stretch("chihuahua"))
    # print(stretch("chihuahua", 4))
    # print(stretch("chihuahua", 4, "ha"))

    # print(bubble_sort([0]), [0])  # Sorts a single element, returns same list
    # print(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])  # Sorted list is the same
    # print(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
    # print(bubble_sort([4, 5, 3, 1, 2]), [1, 2, 3, 4, 5])

if __name__ == "__main__":
    main()