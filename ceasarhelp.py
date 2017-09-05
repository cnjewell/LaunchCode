import string
def alphabet_position(letter):
    letter = letter.lower()
    return list(string.ascii_lowercase).index(letter) 
print(alphabet_position('B'))
def rotate_character(char, rot):
    i = string.ascii_letters.index(char)
    return string.ascii_letters[(i + rot) % 26]
print(rotate_character('Z', 2))
def encrypt(text, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in text:
        if char == ' ':
            encrypted = encrypted + ' '
        else:
            rotated_index = alphabet.index(char) + rot
            if rotated_index < 26:
                encrypted = encrypted + alphabet[rotated_index]
            else:
                encrypted = encrypted + alphabet[rotated_index % 26]
    return encrypted
def main():
    print(encrypt('Abcde', 3))
    print(encrypt('nopqr', 8))
    print(encrypt('abcde', 13))
  
if __name__ == "__main__":
    main()