#challenge problems

def euler_totient(test_number):
    count = 0
    for x in range(1, test_number):
        for n in range(2, x+1):
            if x % n == 0 and test_number % n == 0:
                break # because there's no need to keep testing n's once you have one
        else: 
            # only executes if there are no breaks
            print(x, "has no common factors with", test_number)
            count += 1

    print("\nPhi (", test_number, ') = ',count)
    # count is to test against an online Euler Totient Calculator that gives the count. 
    # I guess count is really phi(n)

def main():

    euler_totient(19)




if __name__ == "__main__":
    main()