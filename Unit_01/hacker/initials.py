def get_initials(name):
    parts = name.split()
    initials = ''
    for part in parts:
        initials += part[0]
    return initials.upper()

def main():
    print('What is your full name?')
    name = input()
    print(get_initials(name))

if __name__ == "__main__":
    main()