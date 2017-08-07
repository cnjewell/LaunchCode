from test import testEqual

def reverse(s):
    if len(s) < 2:
        return s
    else:
        return reverse(s[1:]) + s[0]

def alpha_only(s):
    if len(s) == 1:
        if s[0].isalpha():
            return s[0]
        else:
            return ''
    else:
        if s[0].isalpha():
            return s[0]+ alpha_only(s[1:])
        else: 
            return '' + alpha_only(s[1:])

def is_palindrome(s):
    return alpha_only(s) == reverse(alpha_only(s))

def factorial(n):
    if n < 0:
        return None
    elif n < 2:
        return 1
    else:
        return n * factorial(n-1)

def reverse_list(alist):
    if len(alist) < 2:
        return alist
    else:
        return reverse_list(alist[1:]) + [alist[0]]

def recursive_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_fib(n-2) + recursive_fib(n-1)

# Pascal's Triangle
    # triange = []          #creating a 2D list. A list of rows.
    # for row in range(n):
        # if this is the first row:
            # just append a [1]
        # else construct a new row:
            # append = [1] + [ sum each pair of ints in last row ] + [1]
    # print triangle

# Pascal Recursive
#### From StackOverflow
# def printPascal(n):
#     if n == 0:
#         return [[1]]
#     else:
#         final_r = printPascal(n - 1)
#         last = [0] + final_r[-1] + [0] # note: this does not modify final_r
#         new_row = [last[k] + last[k - 1] for k in range(1, len(last))]
#         return final_r + [new_row]

# Modify recursive tree
# Fractal Mountain
# Hilbert Curve
# Koch Snowflake

# Tower of Hanoi
# Cannibal Puzzle
# Die Hard Jug Puzzle

#   base case
#   change state, move towards base case
#   call itself

testEqual(reverse("hello"),"olleh")
testEqual(reverse("l"),"l")
testEqual(reverse("follow"),"wollof")
testEqual(reverse(""),"")
testEqual(is_palindrome("hello"), False)
testEqual(is_palindrome("aibohphobia"), True)

print(alpha_only("Cage! Match!"))

s = "madam i'm adam"
print(is_palindrome(s))


print(factorial(5))

alist = [1, 2, 3, 4, 5]
print(reverse_list(alist))

