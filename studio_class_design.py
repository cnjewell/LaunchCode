from math import sqrt
from test import testEqual

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

    def is_square(self):
        if abs(self.height) == abs(self.width):
            return True
        else:
            return False

    def is_smaller(self, other_rect):
        if self.area() < other_rect.area():
            return True
        else:
            return False

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

def gcd(numerator, denominator):
    while numerator % denominator != 0:
        old_num = numerator
        old_den = denominator

        numerator = old_den
        denominator = old_num % old_den

    return denominator

class Fraction:
    
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __repr__(self):
        return str(self.numer) + "/" + str(self.denom)

    def add(self, fraction2):
        """
        Returns a new Fraction that is the sum of self and fraction2
        Result will be in simplest terms via the simply() method
        """
        new_numer = self.numer * fraction2.denom + fraction2.numer * self.denom
        new_denom = self.denom * fraction2.denom
        sum_f = Fraction(new_numer, new_denom)
        sum_f.simplify()

        return sum_f

    def __add__(self, fraction2):
        new_numer = self.numer * fraction2.denom + fraction2.numer * self.denom
        new_denom = self.denom * fraction2.denom
        sum_f = Fraction(new_numer, new_denom)
        sum_f.simplify()

        return sum_f

    def multiply(self, other):
        """
        Returns a new Fraction that is the product of self and fraction2
        Result will be in simplest terms via the simply() method
        """
        new_numer = self.numer * other.numer
        new_denom = self.denom * other.denom
        product = Fraction(new_numer, new_denom)
        product.simplify()
        return product

    def __mul__(self, other):
        new_numer = self.numer * other.numer
        new_denom = self.denom * other.denom
        product = Fraction(new_numer, new_denom)
        product.simplify()
        return product

    def reciprocal(self):
        return self.denom, self.numer

    def simplify(self):
        common = gcd(self.numer, self.denom)
        self.numer = self.numer // common
        self.denom = self.denom // common

class BaseballPlayer:
    def __init__(self, init_name, init_jersey_num='00', init_handedness='right'):
        self.name = init_name
        self.jersey_num = init_jersey_num
        self.set_handedness(init_handedness)
        self.run_count = 0
        self.rbi_count = 0
        self.game_count = 0

    def endgame(game_runs, game_rbis):
        pass
        # add to rbi's
        # add to runs
        # add 1 to games

    def get_handedness(self):
        return self.handedness

    def set_handedness(self, handedness_input):
        if (handedness_input.lower() == 'right' 
            or handedness_input.lower() == 'left' 
            or handedness_input.lower() == 'switch'):
            self.handedness = handedness_input
        else:
            print("Baseball Player: 'right', 'left' or 'switch' handedness only. Defaulting to 'right'")
            self.handedness = 'right'

# class Student:
#     def __init__(self):
        # name - should be required upon init
        # ID # - should be generated and recorded somehwere? Too complicated?
 
        # grades - Must include a way to translate percent grades to grade points
        # credits taken - a counter
        # GPA - grade points/attempted credit hours (typically 3). 
        #       grade points = credit hours (i.e. 3) * letter grade factor
        # GPA is complicated...
        
        # class standing (Freshman, Graduated, etc.) based on credits taken

# class Course:
    # def __init__(self):
        # name
        # course number
        # seat limit
        # roster of student objects
        # add students
        # drop students
        # report average GPA of students on roster





