# GPA = grade points(3 * letter grade factor) /  attempted credit hours (len(grades) * 3)

# Letter grade factors:
# A     = 4.00  = 100
# A-    = 3.70  = 
# B+    = 3.33  = 
# B     = 3.00  = 
# B-    = 2.70  = 
# C+    = 2.30  = 
# C     = 2.00  = 
# C-    = 1.70  = 
# D+    = 1.30  = 
# D     = 1.00  = 
# D-    = 0.70  = 65
# F     = 0.00  = 

# grades 100 - 65 maps to 4.00 to 0.00
def linear_conversion(old_value, old_min, old_max, new_min, new_max):
    '''Maps old_value within a new range'''
    old_range = (old_max - old_min)
    new_range = (new_max - new_min)
    return (((old_value - old_min) * new_range) / old_range) + new_min

grade = 98
print(round(linear_conversion(grade, 65, 100, 0, 4), 2))

def earned_credits(grade):
    return round(linear_conversion(grade, 65, 100, 0, 4), 2)

print(earned_credits(grade))

# grades - Must include a way to translate percent grades to grade points
# attempted credit hours = len(grades) * 3

# GPA - grade points/attempted credit hours (typically 3). 
#       grade points = credit hours (i.e. 3) * letter grade factor
# GPA is complicated...

# Grade percentage for course mapped to 4.00 point range * 3 credit hours = earned grade points