#challenge problems
import fractions 
import time

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

def phi(n):
    count = 0
    for i in range(n):
        if fractions.gcd(n, i) == 1: 
            print(i)
            count += 1
    print("phi({0}) =".format(n), count)

def dynamic_fib(n):
    fibs = {0:0, 1:1}
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n in fibs:
        return fibs[n]
    else:
        for num in range(2, n+1):
            newfib = fibs[num-2] + fibs[num-1]
            fibs[num] = newfib
        return fibs[n]

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
    print(primes)
    # print("count:",count)

def sieve_eratosthenes2(n):
    primes = [True for x in range(n)]
    primes[0] = False
    # count = 0
    for index in range(1, 100): # only mark composites of primes < 100
        if primes[index] == False:  #if the i is already marked composite, skip it
            continue
        for j in range((index+1)*2, n+1, index+1):
            primes[j-1] = False
    primeprint = []
    for num in enumerate(primes, start=1):
        if num[1] == True:
            primeprint.append(num[0])
            # count += 1
    print(primeprint)
    # print(count)


def sieve_atkin(n):
    pass

def main():
    # euler_totient(19)
    # phi(12)
    start = time.time()
    # sieve_eratosthenes(10000)
    sieve_eratosthenes2(10000)
    print("time", time.time() - start)

if __name__ == "__main__":
    main()

#Seems like once you have checked the first 1% of the number range for the sieve, you can stop

# import time
# start = time.time()
# print(#big ol fn)
# print("time", time.time() - start)
# # 10,000 primes

# In Runestone
# sieve_eratosthenes = time 38.1347799301 with no sort
# centprime = time 103.50208497
# print(103.50208497/23.4353151321)
# print(80/0.05)

# 0.363729953766