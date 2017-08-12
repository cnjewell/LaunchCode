# vigenere.py per the "Crytpo" External Assignment

from helpers import alphabet_position, rotate_character, xor_character
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

# def xor_encrypt(plaintext, key):
#     output = ''

#     key_index = 0
#     for char in plaintext:
#         output += xor_character(char, key[key_index])
#         key_index = (key_index + 1) % len(key)

#     return output

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

    # speechbubble = "Bitwise operations only make sense for integers. Negative numbers are treated as their 2’s complement value (this assumes that there are enough bits so that no overflow occurs during the operation)."
    # print(xor_encrypt(speechbubble, "The crow flies at midnight"))
    # print(xor_encrypt(xor_encrypt(speechbubble, "The crow flies at midnight"), "The crow flies at midnight"))

if __name__ == "__main__":
    main()