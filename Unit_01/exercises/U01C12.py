# Chapter 12 & 13 - Classes and Objects
from math import sqrt
from test import testEqual
from itertools import combinations

class Point:

    def __init__(self, init_x, init_y):
        """ Create a new point at the given coordinates. """
        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def distance_from_point(self, point):
        return sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2)

    def reflect_x(self):
        self.x = self.x * -1

    def slope_from_origin(self):
        try:
            return (self.y) / (self.x) 
        except ZeroDivisionError:
            return None
    def move(self, dx, dy):         
        self.x += dx
        self.y += dy
    def __repr__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

class Car:
    def __init__(self, init_gas_level):
        self.gas_level = float(init_gas_level)
    def add_gas(self, amount):
        self.gas_level += float(amount)
    def fill_up(self):
        if self.gas_level >= 13.0:
            return 0
        else:
            top_off = 13.0 - self.gas_level
            self.gas_level = 13.0
            return top_off

class Rectangle:
    def __init__(self, init_llc, init_width, init_height):
        self.llc = init_llc
        self.width = init_width
        self.height = init_height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

    def transpose(self):
        self.width, self.height = self.height, self.width

    def contains(self, point):
        if (self.llc.x <= point.x 
            and point.x < self.llc.x + self.width
            and self.llc.y <= point.y
            and point.y < self.llc.y +self.height):
            
            return True
        
        else:
            return False

    def diagonal(self):
        return round(sqrt(self.width ** 2 + self.height ** 2), 10)

    def collision_detected(self, other):
        # for each rectangle, both self and other
        for rect1, rect2 in [(self, other), (other, self)]:
            
            # for each corner in said rect
            ulc1 = Point(rect1.llc.x, rect1.llc.y + rect1.height)
            urc1 = Point(rect1.llc.x + rect1.width, rect1.llc.y + rect1.height)
            lrc1 = Point(rect1.llc.x + rect1.width, + rect1.llc.y)
            llc1 = Point(rect1.llc.x, rect1.llc.y)
            for corner in [ulc1, urc1, lrc1, llc1]:
                
                # is corner within these bounds:
                # other.llc.x <= corner x <= other.llc.x + other.llc.width
                # AND same for y's/height
                if (rect2.llc.x <= corner.x <= rect2.llc.x + rect2.width
                    and rect2.llc.y <= corner.y <= rect2.llc.y + rect2.height):

                    return True
        else:
            return False

class Chatbot:
    """ An object that can engage in rudimentary conversation with a human. """

    def __init__(self, name):
        self.name = name

    def greeting(self):
        """ Returns the Chatbot's way of introducing itself. """
        return "Hello, my name is " + self.name +'\n'

    def response(self, prompt_from_human):
        """ Returns the Chatbot's response to something the human said. """
        return "It is very interesting that you say: '" + prompt_from_human + "'"

class BoredChatbot(Chatbot):
    
    def response(self, prompt_from_human):
        if len(prompt_from_human) > 20:
            return "zzz... Oh excuse me, I dozed off reading your essay."
        else:
            return Chatbot.response(self, prompt_from_human)


sally = BoredChatbot("Sally")

human_message = input(sally.greeting())

print(sally.response(human_message))
        

# p = Point(0,50)
# # q = Point(10,10)
# # print(p.distance_from_point(q))

# # p.reflect_x()
# # print(p)

# print(p.slope_from_origin())
# p.move(5, 5)
# print(p)
# print(p.slope_from_origin())

# r = Rectangle(Point(100,50), 5, 10)
# print(r.width)
# print(r.height)
# r.transpose()
# print(r.width)
# print(r.height)

# r = Rectangle(Point(0, 0), 10, 5)
# testEqual(r.contains(Point(0, 0)), True)
# testEqual(r.contains(Point(3, 3)), True)
# testEqual(r.contains(Point(3, 7)), False)
# testEqual(r.contains(Point(3, 5)), False)
# testEqual(r.contains(Point(3, 4.99999)), True)
# testEqual(r.contains(Point(-3, -3)), False)

# r = Rectangle(Point(0, 0), 10, 5)
# testEqual(r.diagonal(), 11.1803398875)

# r1 = Rectangle(Point(0,0), 12, 4)
# testEqual(r1.diagonal(), 12.6491106407)

# r2 = Rectangle(Point(0,0), 1,2)
# testEqual(r2.diagonal(), 2.2360679775)

# r1 = Rectangle(Point(0,0), 1,2)
# r2 = Rectangle(Point(0,0), 1,2)
# testEqual(r1.collision_detected(r2), True)
# r1 = Rectangle(Point(0,1), 2,2)
# r2 = Rectangle(Point(1,0), 2,2)
# testEqual(r1.collision_detected(r2), True)
# r1 = Rectangle(Point(5,5), 2,2)
# r2 = Rectangle(Point(0,1), 2,2)
# testEqual(r1.collision_detected(r2), False)
# r1 = Rectangle(Point(0,0), 2,2)
# r2 = Rectangle(Point(2,2), 2,2)
# testEqual(r1.collision_detected(r2), True)
# r1 = Rectangle(Point(0,0), 2,2)
# r2 = Rectangle(Point(-2,-2), 2,2)
# testEqual(r1.collision_detected(r2), True)
# r1 = Rectangle(Point(0,0), 2,2)
# r2 = Rectangle(Point(3,0), 2,2)
# testEqual(r1.collision_detected(r2), False)
# r1 = Rectangle(Point(0,0), 2,2)
# r2 = Rectangle(Point(2,0), 2,2)
# testEqual(r1.collision_detected(r2), True)
# r1 = Rectangle(Point(0,0), 2,2)
# r2 = Rectangle(Point(-1,1), 2,2)
# testEqual(r1.collision_detected(r2), True)
# r1 = Rectangle(Point(0,0), 2,2)
# r2 = Rectangle(Point(1,1), 2,2)
# testEqual(r1.collision_detected(r2), True)
# r1 = Rectangle(Point(0,0), 2,2)
# r2 = Rectangle(Point(-1,-1), 2,2)
# testEqual(r1.collision_detected(r2), True)
# r1 = Rectangle(Point(0,0), 2,2)
# r2 = Rectangle(Point(-1,-1), 4,4)
# testEqual(r1.collision_detected(r2), True)
# r1 = Rectangle(Point(-1,-1), 4,4)
# r2 = Rectangle(Point(0,0), 2,2)
# testEqual(r1.collision_detected(r2), True)
