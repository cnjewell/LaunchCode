def initials_only(name):
    parts = name.split()
    initials = ''
    for part in parts:
        initials += part[0]
    return initials

def main():
    print('What is your full name?')
    name = input()
    print(initials_only(name))

if __name__ == "__main__":
    main()