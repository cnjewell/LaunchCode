# Unit 1, Chapter 4: Exercises

#Note: Turtle problems in turtles.py

number = int(input('Number:'))
for num in range(number):
    print("We like Python's turtles!")



for num in range(100):
    print(99-num, 'bottles of beer on the wall!', 99-num, 'bottles of beer! Take one down, pass it around,', 99-num-1, 'bottles of beer on the wall!')



for num in range(51):
    if num % 2 == 0:
        print(num)



months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

for month in months:
    print('One of the months of the year is', month)



#Unit 1, Chapter 4, Exercise 16
# The Pythagorean Theorem tells us that the length of the hypotenuse 
# of a right triangle is related to the lengths of the other two sides. 
# Look through the math module and see if you can find a function that 
# will compute this relationship for you. Once you find it, 
# write a short program to try it out.

#Unit 1, Chapter 4, Graded Assignment
def squares_list(num_list):
    for num in nums:
        print(num)
    for num in nums:
        print("The square of", num, "is", num * num)

def main():
    nums = [12, 10, 32, 3, 66, 17, 42, 99, 20]
    squares_list(nums)
if __name__ == "__main__":
    main()
