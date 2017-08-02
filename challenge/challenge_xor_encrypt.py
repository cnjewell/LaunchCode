#Challenge - extended cryptography
# Encrypting non-alpha characters

def char_xor_key(char, key):
    return chr((ord(char) ^ ord(key)))

def main():
    # bin(), bit-wise operators
    print(bin(0b1101 ^ 0b1001)) # The original character, to the left, is concealed by the XOR operation
    print(bin(0b100 ^ 0b1001))
    # XOR Reverses

    # Write encryption using XOR bitwise operators

    print(bin(ord('a')))
    print(bin(ord('b')))
    print(bin(ord('c')))
    print(bin(ord('d')))
    print(bin(ord('e')))
    print(bin(ord('F')))
    print(type(bin(ord('f'))))

    print(char_xor_key(char_xor_key("a", "x"), "x"))

if __name__ == "__main__":
    main()