# vigenere.py per the "Crytpo" External Assignment

from crypto_helper import alphabet_position, rotate_character
from sys import argv

def encrypt(plaintext, key):
    output = ''
    
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            output += rotate_character(char, alphabet_position(key[key_index]))
            key_index = (key_index + 1) % len(key)
        else:
            output += char

    return output

def main():
    if len(argv) != 2:
        print("usage: python vigenere.py keyword")
        print("Missing Argument: Exactly 1 arg required.")
        exit()
    
    if argv[1].isalpha() == False:
        print("usage: python vigenere.py keyword")
        print("Keyword Error: Alpha characters only.")
        exit()

    print("Type a message:")
    plaintext = input()
    # print("Encryption key:")
    # cipherkey = input()
    print(encrypt(plaintext, argv[1]))

if __name__ == "__main__":
    main()