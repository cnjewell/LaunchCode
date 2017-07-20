# U01C07 - Exceptions

def some_function():
    # Imagine code that could raise value or unicode errors
    pass

def line(n):
    output = '' 
    for i in range(n):
        output = output + "#"
    return output

def spaces(n):
    output = '' 
    for i in range(n):
        output = output + " "
    return output

def square(n):
    output = ''
    for i in range(n):
        output = output + line(n) + "\n"
    return output

def rectangle(w, h):
    output = ''
    for i in range(h):
        output = output + line(w) + "\n"
    return output

def stairs(n):
    output = ''
    for i in range(n):
        output = output + line(1+i) + "\n"
    return output

def space_line(s, l):
    output = ''
    for i in range(s):
        output = output + ' '
    output = output + line(l)
    return output

def triangle(n):
    output = ''
    for i in range(n):
        output = output + spaces(n-1-i)
        output = output + line(1+i*2)
        output = output + spaces(n-1-i)
        output = output + "\n"
    return output

def diamond(n):
    output = ''
    for i in range(n):
        output = output + spaces(n-1-i)
        output = output + line(1+i*2)
        output = output + spaces(n-1-i)
        output = output + "\n"
    for i in sorted(range(n-1), reverse=True):
        output = output + spaces(n-1-i)
        output = output + line(1+i*2)
        output = output + spaces(n-1-i)
        output = output + "\n"
    return output

def main():
    
    # Exercise 4
    try:
        some_function()
    except UnicodeError:
        print("Unicode Error is happening!")
    except ValueError:
        print("Value Error is happening!")

    # Exercise 5
    print(line(5))
    print('')

    # Exercise 6
    print(square(5))
    print('')

    # Exercise 7
    print(rectangle(5,3))
    print('')

    # Exercise 8
    print(stairs(5))
    print('')

    # Exercise 9
    print(space_line(3,5))
    print('')

    # Exercise 10
    print(triangle(6))
    print(triangle(1))
    print(triangle(0))
    print(triangle(20))
    print('')

    # Exercise 11
    print(diamond(5))
    print(diamond(2))
    print(diamond(0))
    print(diamond(1))
    print(diamond(10))
    print('')

if __name__ == "__main__":
    main()