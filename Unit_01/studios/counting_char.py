import test

def count_char(text):
    char_dict = {}
    for char in text:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    return char_dict

def factors(n):
    return [x for x in range(1, n+1) if n % x == 0]
# example: [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

def reverse_dict(in_dict):
    out_dict = {}

    for in_key, in_val in in_dict.items():
        if in_val in out_dict:
            out_dict[in_val] = out_dict[in_val] + [in_key]
        else:
            out_dict[in_val] = [in_key]        
    
    return out_dict
    

speechbubble = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa. Donec nec velit non ligula efficitur luctus."
# print(count_char(speechbubble))

# print(factors(2))
# print(factors(3))
# print(factors(5))
# print(factors(10))
# print(factors(20))
# print(factors(35))

lorem_dict = count_char(speechbubble)

print(reverse_dict(lorem_dict))


