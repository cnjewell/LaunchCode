#U01CH06

def letter_grade(score):
    if score >= 90:
        return "A"
    elif score < 90 and score >= 80:
        return "B"
    elif score < 80 and score >= 70:
        return "C"
    elif score < 70 and score >= 60:
        return "D"
    else:
        return "F"

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return not(is_even(n))

def pick_activity(heat, moisture):
    if heat == "hot" and moisture == "dry":
        print("Hot & Dry: go swimming")
    elif heat == "hot" and moisture == "wet":
        print("Hot & Wet: Netflix and chill")
    elif heat == "cold" and moisture == "wet":
        print("Cold & Wet: Paint")
    elif heat == "cold" and moisture == "dry":
        print("Cold & Dry: Read at Cafe")
    else:
        print("gimme weather...")

def is_rightangled(a, b, c):
    hyp = max(a, b, c)
    return abs(((a ** 2 + b **2 + c **2)) - ((hyp ** 2) * 2)) < 0.001

def date_of_easter(year):
    
    #test for vaild year between 1900 and 2099
    year = int(year)
    if year < 1900 or year > 2099:
        print("Year beyond 1900-2099 range")
    else:
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7
        date = 22 + d + e
    
    # test for special years before returning, if so sub 7  1954, 1981, 2049, or 2076
        # test for greater than 31 dates and return April (date % 31)
        if year == 1954 or year == 1981 or year == 2049 or year == 2076:
            date = date - 7
        if date > 31:
            print("April", date % 31)
        else:
            print("March", date)

def is_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 4 == 0 and year % 400 == 0:
        return True
    else:
        return False

def main():
    # Exercise 2
    print(letter_grade(80))
    print(letter_grade(60))
    print(letter_grade(59))
    print(letter_grade(91))
    print(letter_grade(90))
    print(letter_grade(89))

    # Exercise 8
    print('')
    heat = "cold"
    moisture = "dry"
    pick_activity(heat, moisture)

    # Exercise 9
    print('')
    print(is_rightangled(1.5, 2.0, 2.5), '\t', True)
    print(is_rightangled(4.0, 8.0, 16.0), '\t', False)
    print(is_rightangled(4.1, 8.2, 9.1678787077), '\t', True)
    print(is_rightangled(4.1, 8.2, 9.16787), '\t', True)
    print(is_rightangled(4.1, 8.2, 9.168), '\t', False)
    print(is_rightangled(0.5, 0.4, 0.64031), '\t', True)

    # Exercise 10
    print('')
    print(is_rightangled(1.5, 2.0, 2.5), '\t', True)
    print(is_rightangled(16.0, 4.0, 8.0), '\t', False)
    print(is_rightangled(4.1, 9.1678787077, 8.2), '\t', True)
    print(is_rightangled(9.16787, 4.1, 8.2), '\t', True)
    print(is_rightangled(4.1, 8.2, 9.168), '\t', False)
    print(is_rightangled(0.5, 0.64031, 0.4), '\t', True)

    # Exercise 11
    print('')    
    date_of_easter(1899)
    date_of_easter(1900)
    date_of_easter(2099)
    date_of_easter(2100)
    date_of_easter(2017)
    date_of_easter(1900.00)
    date_of_easter("1900")

    # Weekly Graded Assignment
    print('')
    print(is_leap(1944), '\t', True)
    print(is_leap(2011), '\t', False)
    print(is_leap(1986), '\t', False)
    print(is_leap(1956), '\t', True)
    print(is_leap(1957), '\t', False)
    print(is_leap(1800), '\t', False)
    print(is_leap(1900), '\t', False)
    print(is_leap(1600), '\t', True)
    print(is_leap(2056), '\t', True)

if __name__ == "__main__":
    main()