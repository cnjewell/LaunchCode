# Encryption
# Vigenère cipher

import string
from itertools import cycle

def rot13(plaintext):
    output = ''
    for char in plaintext.upper():
        if char.isalpha():
            i = string.ascii_uppercase.index(char)
            output = output + string.ascii_uppercase[(i+13)%26]
        else:
            output = output + char
    return output

def ceasar_cipher(text, offset, mode='encrypt'):
    output = ''
    for char in text.upper():
        if char.isalpha():
            i = string.ascii_uppercase.index(char)
            if mode == 'encrypt':
                output = output + string.ascii_uppercase[(i+offset)%26]
            elif mode == 'decrypt':
                output = output + string.ascii_uppercase[(i+(26-offset))%26]
        else:
            output = output + char
    return output

def caesar_cracker(ciphertext):
    output = ''
    
    for num in range(26, 0, -1): #Counts backwards in order to calculate the offset easier... Ugly code...
        output += 'Offset: '
        output += ' '*(2-len(str(26-num))) + str(26-num)  #Ugly UGLY leading zeroes thing! UGLY!
        output += ' - '

        for char in ciphertext.upper():
            if char.isalpha():
                i = string.ascii_uppercase.index(char)
                output += string.ascii_uppercase[(i+num)%26]
            else:
                output += char
        output += "\n"
    return output

def vigenere(text, key, mode='encrypt'):
    if not(key.isalpha()):
        return 'Keys must contain only letters of the alphabet.'
    
    # no_spaces = ''
    # for char in text:
    #     if char.isalpha():
    #         no_spaces += char
    # text = no_spaces

    output = ''
    for char, key_char in zip(text.upper(), cycle(key.upper())):
        if char.isalpha():
            i = string.ascii_uppercase.index(char)
            j = string.ascii_uppercase.index(key_char)
            if mode == 'encrypt':
                output += string.ascii_uppercase[(i+j)%26]
            elif mode == 'decrypt':
                output += string.ascii_uppercase[(i-j)%26]
        else:
            output += char
    return output

def babbage(ciphertext):
    # find key length
        # run repeated_sequences(ciphertext)
        # return a list of the sequences
    # Perform frequency analysis of groups of letters that are KEYLENGTH letters apart
    # Cycle through letters for each group until freq dist closely matches English freq dist
    pass

def repeated_sequences(string):
    '''Returns a dict of sequences and the frequency each repeats, min = 2 repeats'''
    
    # Initialize a freq dict{}
    # for slice sized in range(2-5)
        # take a slice of the string
            # is the slice in the freq dict? If not, continue.
            # is the slice in the string after the slice occurred?
                # Great! how many times?
                # Record freq in dict under slice as the key
    # return freq dict{}
    pass

def frequency_analysis():
    pass


# print(rot13('abcde'))
# print(rot13('nopqr'))
# print(rot13(rot13('since rot thirteen is symmetric you should see this message')))

# print(caesar_cracker(rot13('This is the totally rad plaintext hidden under my totally sweet cipher!')))
# print(rot13('This is the totally rad plaintext hidden under my totally sweet cipher!'))
# print(ceasar_cipher('This is the totally rad plaintext hidden under my totally sweet cipher!', 2))

my_offset = 20
print(ceasar_cipher(ceasar_cipher('This is the totally rad plaintext hidden under my totally sweet cipher!', my_offset), my_offset, mode='decrypt'))
print(caesar_cracker(ceasar_cipher('This is the totally rad plaintext hidden under my totally sweet cipher!', my_offset)))

print(vigenere('This is the totally rad plaintext hidden under my totally sweet vigenere cipher!', 'key'))
print(vigenere(vigenere('This is the totally rad plaintext hidden under my totally sweet vigenere cipher!', 'key'), 'key', mode='decrypt'))

print()
print("Charles Babbage? How did you get in here, you devil? What a scoundrel!")
to_crack = vigenere("Charles Babbage? How did you get in here, you devil? What a scoundrel!", 'key')
print(to_crack)
