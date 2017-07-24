import math, time

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

# print(atkin(10000))
print(len(atkin(10000)))

start = time.time()
atkin(10000)
print(time.time() - start)