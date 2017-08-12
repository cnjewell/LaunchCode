# crypto_helper functions

import string

def alphabet_position(char):
    '''Returns the index of the alpha character within the alphabet. Case-insensitve.'''
    if char.islower():
        return string.ascii_lowercase.index(char)
    else:
        return string.ascii_uppercase.index(char)

def rotate_character(char, rot):
    '''Returns the letter (rot) number of letters after (char)'''
    if char.isalpha():
        if char.islower():
            return string.ascii_lowercase[(alphabet_position(char)+rot)%26]
        else:
            return string.ascii_uppercase[(alphabet_position(char)+rot)%26]
    else:
        return char # Pass through non-alpha characters

def xor_character(char, key):
    '''Returns a unicode charater that has been XOR'd by key'''
    return chr((ord(char) ^ ord(key)))