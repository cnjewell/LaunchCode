from math import sqrt
from test import testEqual

def gcd(numerator, denominator):
    while numerator % denominator != 0:
        old_num = numerator
        old_den = denominator

        numerator = old_den
        denominator = old_num % old_den

    return denominator

def linear_conversion(old_value, old_min, old_max, new_min, new_max):
    '''Maps old_value within a new range'''
    old_range = (old_max - old_min)
    new_range = (new_max - new_min)
    return (((old_value - old_min) * new_range) / old_range) + new_min

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

class Student:
    def __init__(self, iname, istudent_id):
        self.name = iname
        self.student_id = istudent_id
        self.grades = []
    
    def record_grade(self, grade):
        self.grades.append(grade)

    def earned_credits(self, grade):
        return round(linear_conversion(grade, 65, 100, 0, 4), 2)

    def get_GPA(self):
        earned_credit_total = 0
        for grade in self.grades:
            earned_credit_total += self.earned_credits(grade)
        return round(earned_credit_total / len(self.grades), 2)
        
    def get_standing(self):
        # class standing (Freshman, Graduated, etc.) based on credits taken
            # How many credits for each status? 
            # Let's say 12 credits per year
        standing = {1 : "Freshman", 2 : "Sophomore", 3 : "Junior", 4 : "Senior", 5 : "Graduated"}
        earned_credit_total = 0
        for grade in self.grades:
            earned_credit_total += self.earned_credits(grade)
        print(earned_credit_total)
        print(earned_credit_total / 12)
        if int(earned_credit_total / 12) > 5:
            return standing[5]
        else:
            return standing[int(earned_credit_total / 12)]


class Course:
    def __init__(self, iname, icourse_id, iseat_limit):
        self.name = iname
        self.course_id = icourse_id
        self.seat_limit = iseat_limit
        self.roster = []
    
    def add_student(self, student):
        if self.seat_limit > len(self.roster):
            self.roster.append(student)
        else:
            return False
    
    def drop_student(self, student):
        if student in self.roster:
            self.roster.remove(student)
    
    def get_avg_GPA(self):
        # for student in roster
            # accumulate their GPA's
        # divide GPA sum by class size, round it
        sum_GPAs = 0
        for student in self.roster:
            sum_GPAs += student.get_GPA()
        return sum_GPAs / len(self.roster)


fred = Student("Fred", "456")
saul = Student("Saul", "310")
beth = Student("Beth", "418")

stupid_class = Course("English", "ES101", 30)

stupid_class.add_student(fred)
stupid_class.add_student(saul)
stupid_class.add_student(beth)

fred.record_grade(100)
fred.record_grade(90)
fred.record_grade(70)
fred.record_grade(99)
fred.record_grade(99)
fred.record_grade(99)
fred.record_grade(99)
fred.record_grade(99)
fred.record_grade(99)
fred.record_grade(99)

saul.record_grade(100)
saul.record_grade(90)
saul.record_grade(40)
saul.record_grade(90)
saul.record_grade(80)
saul.record_grade(75)
saul.record_grade(90)

stupid_class.drop_student(beth)

print(fred.get_GPA())
print(saul.get_GPA())
print(stupid_class.get_avg_GPA())

print(fred.get_standing())
print(saul.get_standing())


