# caesar.py per the "Crytpo" External Assignment

import helpers
from sys import argv, exit

def encrypt(plaintext, rot):

    output = ''
    
    for char in plaintext:
        output += helpers.rotate_character(char, rot)
    
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

