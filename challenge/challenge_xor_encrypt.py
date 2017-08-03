#Challenge - extended cryptography
# Encrypting non-alpha characters

def char_xor_key(char, key):
    return chr((ord(char) ^ ord(key)))

def xor_hex(char, key):
    return hex((ord(char) ^ ord(key)))

def unxor_hex(char, key):
    return chr(int(char, base=16) ^ ord(key))

def xor_hex_encrypt(plaintext, key):
    output = ''

    key_index = 0
    for char in plaintext:
        output += xor_hex(char, key[key_index]) + ' '
        key_index = (key_index + 1) % len(key)

    return output

def xor_hex_decrypt(ciphertext, key):
    output = ''

    key_index = 0
    for char in ciphertext.split():
        output += unxor_hex(char, key[key_index])
        key_index = (key_index + 1) % len(key)

    return output

def main():
    # bin(), bit-wise operators
    # print(bin(0b1101 ^ 0b1001)) # The original character, to the left, is concealed by the XOR operation
    # print(bin(0b100 ^ 0b1001))
    # XOR Reverses

    # Write encryption using XOR bitwise operators

    # print(bin(ord('a')))
    # print(bin(ord('b')))
    # print(bin(ord('c')))
    # print(bin(ord('d')))
    # print(bin(ord('e')))
    # print(bin(ord('F')))
    # print(type(bin(ord('f'))))

    # print(char_xor_key(char_xor_key("a", "x"), "x"))

    test = xor_hex("a", "x") 
    print(test)

    # U+1F422
    print(chr(0x1F422))
    speechbubble = "Since the char encoding is unicode, you can even safely encrypt your Emoji 🐢"
    test2 = xor_hex_encrypt(speechbubble, "foxy brown")
    print(test2)
    print(type(test2))
    untest2 = xor_hex_decrypt(test2, "foxy brown")
    print(untest2)

if __name__ == "__main__":
    main()