import fractions, math
import time

def is_prime(n):
    """Returns true if n is prime, false otherwise."""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    
def centprime(n): # the naive implementation
    """Return a list of primes below N"""
    primes = []
    for i in range(0, n):
        if is_prime(i):
            primes.append(i)
    return primes

def sieve_eratosthenes(n):
    composites = []
    # count = 0
    for i in range(2,100):
        if i in composites:
            continue
        for j in range(i*2, n, i):
            composites.append(j)
    primes = []
    for num in range(2, n):
        if num not in composites:
            primes.append(num)
            # count += 1
    return primes
    # print("count:",count)

def sieve_eratosthenes2(n):
    primes = [True for x in range(n)]
    primes[0] = False
    
    for index in range(1, int(math.sqrt(n))): # only mark composites thru sqrt(n)
        if primes[index] == False:  #if the i is already marked composite, skip it
            continue
        # otherwise, use that index 

        # The following range returns the factorization of the number (num = index+1)
        # starting at num*2, ending at n+1, and incrementing by num
        for j in range((index+1)*2, n+1, index+1):
            primes[j-1] = False
    
    primelist = [i+1 for i,x in enumerate(primes) if x == True]
    
    print(len(primelist)) #check to see if I'm getting the right number of primes
    return primelist
    
def sieve_eratosthenes3(n):
    primes = [False for x in range(n)]
    primes[1] = True # 2 is prime
    primes[2] = True # 3 is prime

    # This section will find some co-primes
    m = 2
    while 3*m+1 <= n:
        if (3*m-1) % 2 != 0:
            primes[3*m-2] = True
        if (3*m+1) % 2 != 0:
            primes[3*m] = True
        m += 1
    
    # for each non-even number...:
    #   co-primes past 3 take the form of 3*n + or - 1
    # n = 2
    # while 3*n+1 <= searchspace:
        # if (3*n-1) % 2 != 0:   # if it isn't even and pops out of this pattern...
        #       then mark 3*n-1 as prime
        # if (3*n+1) % 2 != 0:
        #       then mark 3*n+1 as prime
        # increment n + 1
    
    # section from seieve of ero
    for index in range(1, 20): # only mark composites thru sqrt(n)
        if primes[index] == False:  #if the i is already marked composite, skip it
            continue
        # otherwise, use that index 
        for j in range((index+1)*2, n+1, index+1):
            primes[j-1] = False

    primelist = [i+1 for i,x in enumerate(primes) if x == True]
    print(len(primelist))
    return primelist
    
def sieve_atkin(n):
    pass

def atkin(limit):    
    is_prime = [False] * (limit + 1)
    is_prime[2] = True
    is_prime[3] = True

    square_limit = int(math.sqrt(limit))

    for x in range(1,square_limit+1):
        for y in range(1,square_limit+1):
            
            n = 4 * x ** 2 + y ** 2
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                is_prime[n] = not is_prime[n]

            n = 3 * x ** 2 + y ** 2
            if n <= limit and n % 12 == 7:
                is_prime[n] = not is_prime[n]

            n = 3 * x ** 2 - y ** 2
            if x > y and n <= limit and n % 12 == 11:
                is_prime[n] = not is_prime[n]

    for n in range(5, square_limit):
        if is_prime[n]:
            for k in range(n ** 2,limit+1,n ** 2):
                is_prime[k] = False

    return [i for i,x in enumerate(is_prime) if x == True]

def main():

    start = time.time()
    centprime(1000)
    base_time = time.time() - start

    start = time.time()
    sieve_eratosthenes2(10000)
    my_time = time.time() - start

    print("Base time:", base_time)
    print("My time:", my_time)
    print("Schmidt Score:", my_time / base_time)

    print('')

    start = time.time()
    sieve_eratosthenes3(10000)
    my_time = time.time() - start

    print("Base time:", base_time)
    print("My time:", my_time)
    print("Schmidt Score:", my_time / base_time)      

if __name__ == "__main__":
    main()
