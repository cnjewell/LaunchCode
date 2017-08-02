import string
from test import testEqual

def intlen(n):
    return len(str(n))

def remove(substr, original_string):
    x = original_string.find(substr)
    if x == -1:
        return original_string
    else:
        output = original_string[:x] + original_string[x+len(substr):]
        return output

def reverse(text):
    output = ''
    for char in text:
        output = char + output
    return output

def is_palindrome(text):
    if text == reverse(text):
        return True
    else:
        return False

def mirror(text):
    return text + reverse(text)

def substitution_cipher(plaintext):
    sub_cipher = "KUMAHLFXRNQPZYVTOBSGEWIDJC"
    output = ''
    for char in plaintext.upper():
        i = string.ascii_uppercase.index(char)
        output = output + sub_cipher[i]
    return output

def decrypt_substitution(ciphertext, cipher):
    decrypted_output = ''
    for char in ciphertext.upper():
        i = cipher.index(char)
        decrypted_output = decrypted_output + string.ascii_uppercase[i]
    return decrypted_output

def rot13(mess):
    output = ''
    for char in mess.upper():
        if char.isalpha():
            i = string.ascii_uppercase.index(char)
            output = output + string.ascii_uppercase[(i+13)%26]
        else:
            output = output + char
    return output

# def analyze_text(text):
#     alpha_count = 0
#     e_count = 0
#     for char in text:
#         if char.isalpha():
#             alpha_count += 1
#         if char == 'e' or char == 'E':
#             e_count += 1
#     e_percent = 0.0
#     if e_count != 0:
#         e_percent = round((e_count/alpha_count) * 100, 10)
#     return "The text contains {0} alphabetic characters, of which {1} ({2}%) are 'e'.".format(alpha_count,e_count,e_percent)

def analyze_text(text):
    alpha_count = 0
    e_count = 0
    for char in text:
        if char.isalpha():
            alpha_count += 1
        if char == 'e' or char == 'E':
            e_count += 1
    e_percent = 0.0
    if e_count != 0:
        e_percent = float((e_count/alpha_count) * 100)
    return "The text contains {0} alphabetic characters, of which {1} ({2}%) are 'e'.".format(alpha_count,e_count,e_percent)


def main():
    # # Exercise 2
    # print(intlen(59))
    # print(intlen(100))

    # # Exercise 3       
    # print(remove('an', 'banana'), 'bana')
    # print(remove('cyc', 'bicycle'), 'bile')
    # print(remove('iss', 'Mississippi'), 'Missippi')
    # print(remove('egg', 'bicycle'), 'bicycle')
    # print(remove('oo', 'Yahoohoo'), 'Yahhoo')

    # # Exercise 4
    # print(reverse("happy"), "yppah")
    # print(reverse("Python"), "nohtyP")
    # print(reverse(""), "")

    # # Exercise 5
    # print(is_palindrome('abba'), True)
    # print(is_palindrome('abab'), False)
    # print(is_palindrome('straw warts'), True)
    # print(is_palindrome('a'), True)
    # print(is_palindrome(''), True)

    # # Exercise 6
    # print(mirror('good'), 'gooddoog')
    # print(mirror('Python'), 'PythonnohtyP')
    # print(mirror(''), '')
    # print(mirror('a'), 'aa')

    # # Exercise 7 
    # # Substitution Cipher
    # print(substitution_cipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    # print(substitution_cipher("Christopher"))

    # # Exercise 8 
    # print(decrypt_substitution("MXBRSGVTXHB", "KUMAHLFXRNQPZYVTOBSGEWIDJC"))

    # # Exercise 9
    print(rot13('abcde'))
    print(rot13('nopqr'))
    print(rot13(rot13('since rot thirteen is symmetric you should see this message')))

    # # Weekly Graded Assignment
    print('')
    text1 = "Eeeee"
    answer1 = "The text contains 5 alphabetic characters, of which 5 (100.0%) are 'e'."
    testEqual(analyze_text(text1), answer1)

    text2 = "Blueberries are tasteee!"
    answer2 = "The text contains 21 alphabetic characters, of which 7 (33.3333333333%) are 'e'."
    testEqual(analyze_text(text2), answer2)

    text3 = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
    answer3 = "The text contains 55 alphabetic characters, of which 0 (0.0%) are 'e'."
    testEqual(analyze_text(text3), answer3)
    
    text1 = "Eeeee"
    answer1 = "The text contains 5 alphabetic characters, of which 5 (100.0%) are 'e'."
    print(analyze_text(text1), answer1)

    text2 = "Blueberries are tasteee!"
    answer2 = "The text contains 21 alphabetic characters, of which 7 (33.3333333333%) are 'e'."
    print(analyze_text(text2), answer2)

    text3 = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
    answer3 = "The text contains 55 alphabetic characters, of which 0 (0.0%) are 'e'."
    print(analyze_text(text3), answer3)

    # print(float(1/3))
if __name__ == "__main__":
    main()