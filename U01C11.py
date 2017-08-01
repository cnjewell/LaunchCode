# U01C11 - Dict and Tuples
import string

def letter_frequency(text):
    freq = {}
    # count the letters
    for char in text.lower():
        if char.isalpha():
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

    # Print letter/freq pairs
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if letter in freq:
            print(letter, freq[letter])

def clock_in(worker_dict, worker, hour):
    worker_alias = worker_dict[worker]
    worker_alias[0] = hour

def clock_out(worker_dict, worker, hour):
    worker_alias = worker_dict[worker]
    worker_alias[1] = hour
    worker_alias[2] = worker_alias[1] - worker_alias[0]

def english_to_piratese(text):
    piratese = {"sir":"matey", "hotel":"fleabag inn", "student":"swabbie", "boy":"matey", "madam":"proud beauty", "professor":"foul blaggart", "restaurant":"galley", "your":"yer", "excuse":"arr", "students":"swabbies", "are":"be", "lawyer":"foul blaggart", "the restroom":"th\' head", "my":"me", "hello":"avast", "is":"be", "man":"matey"}    
    translation = text
    for (k,v) in piratese.items():
        translation = translation.replace(k, v)
    return translation

def set_inventory(inventory, fruit, quantity=0):
    inventory[fruit] = quantity

def sort_contacts(contacts_dict):
    name_list = []
    for name in contacts_dict.keys():
        name_list += [name]
    name_list.sort()
    
    return_list = []
    for name in name_list: # iterate through the now sorted names
        return_list.append((name, contacts_dict[name][0], contacts_dict[name][1]))

    return return_list

def main():
    # letter_frequency("Chistopher")

    # workers = {"George Spelvin": [0,0,0], "Jane Doe": [0,0,0], "John Smith": [0,0,0]}
    # print(workers.get("George Spelvin"))   # should print [0,0,0]
    # clock_in(workers, "George Spelvin", 8)
    # clock_out(workers, "George Spelvin", 17)
    # print(workers.get("George Spelvin"))   # should print [8, 17, 9]
    # print(workers)

    # speechbubble = "hello my man, please excuse your professor to the restroom!"
    # print(english_to_piratese(speechbubble))
    # print("avast me matey, please arr yer foul blaggart to th' head!")

    # new_inventory = {}
    # set_inventory(new_inventory, 'strawberries', 10)
    # print('strawberries' in new_inventory, True)
    # print(new_inventory['strawberries'], 10)
    # set_inventory(new_inventory, 'strawberries', 25)
    # print(new_inventory['strawberries'] , 25)

    freud_contacts = {"Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"), "Welles, Orson": ("1-312-720-8888", "orson@notlive.com"), "Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")}
    print(sort_contacts(freud_contacts))
    print(sort_contacts({"Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
        "Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
        "Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")}) == [('Freud, Anna', '1-541-754-3010',
        'anna@psychoanalysis.com'), ('Horney, Karen', '1-541-656-3010', 'karen@psychoanalysis.com'),
        ('Welles, Orson', '1-312-720-8888', 'orson@notlive.com')])
    print(sort_contacts({"Summitt, Pat": ("1-865-355-4320", "pat@greatcoaches.com"),
        "Rudolph, Wilma": ("1-410-5313-584", "wilma@olympians.com")}) ==
        [('Rudolph, Wilma', '1-410-5313-584', 'wilma@olympians.com'),
        ('Summitt, Pat', '1-865-355-4320', 'pat@greatcoaches.com')])
    print(sort_contacts({"Dinesen, Isak": ("1-718-939-2548", "isak@storytellers.com")}) ==
        [('Dinesen, Isak', '1-718-939-2548', 'isak@storytellers.com')])
    print(sort_contacts({"Rimbaud, Arthur": ("1-636-555-5555", "arthur@notlive.com"),
        "Swinton, Tilda": ("1-917-222-2222", "tilda@greatActors.com"),
        "Almodovar, Pedro": ("1-990-622-3892", "pedro@filmbuffs.com"), "Kandinsky, Wassily":
        ("1-333-555-9999", "kandinsky@painters.com")}) == [('Almodovar, Pedro', '1-990-622-3892',
        'pedro@filmbuffs.com'), ('Kandinsky, Wassily', '1-333-555-9999', 'kandinsky@painters.com'),
        ('Rimbaud, Arthur', '1-636-555-5555', 'arthur@notlive.com'), ('Swinton, Tilda',
        '1-917-222-2222', 'tilda@greatActors.com')])

if __name__ == "__main__":
    main()
        