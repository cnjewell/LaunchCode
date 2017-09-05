# def sort_contacts(contacts):
    # return sorted([(k, v[0], v[1]) for k, v in contacts.items()])

# def sort_contacts(contacts):
#     contact_names = contacts.keys()
#     name_list = []
#     for name in contact_names:
#         contact_names.sort()
#         name_list = name_list + name
#     print(name_list)

def sort_contacts(contacts):
    key_list = list(contacts.keys())
    key_list.sort()
    
    #values_list = list(contacts.values())
    #print(values_list)
    
    new_list = []
    for item in key_list:
        new_list.append( (item, contacts[item][0], contacts[item][1]))
    
    return sorted(new_list)
    
    #tuple = ("")
    #for item in new_list:
        #tuple += item + " "
        
    #str1 = ', '.join(str(item) for item in new_list)
    #return str1
        
    
    #contacts.get(key_list[0])
    #print(key_list[1])
    #print(key_list[2])




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