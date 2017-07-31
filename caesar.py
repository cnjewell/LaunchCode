# caesar.py per the "Crytpo" External Assignment

import crypto_helper
from sys import argv, exit

def encrypt(plaintext, rot):

    output = ''
    
    for char in plaintext:
        output += crypto_helper.rotate_character(char, rot)
    
    return output

def main():
    if len(argv) != 2:
        print("usage: python caesar.py n")
        exit()
    
    if argv[1].isdigit() == False:
        print("usage: python caesar.py n")
        exit()

    print("Type a message:")
    plaintext = input()
    print(encrypt(plaintext, int(argv[1])))

if __name__ == "__main__":
    main()

# print(alphabet_position('a'))
# print(alphabet_position('A'))
# print(alphabet_position('Z'))

# print(rotate_character("A", 13))
# print(rotate_character("a", 13))
# print(rotate_character("XYZ", 3))

# print(encrypt("Hello World!", 5))
# print(encrypt("LaunchCode", 1))
# print(encrypt("A", 13))

