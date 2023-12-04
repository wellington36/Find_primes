import time
import random


def Miller_Rabin_primality_test(n, k):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    # Factor out powers of 2 from n - 1
    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    # Repeat the test k times
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        # Repeat s times
        for _ in range(s):
            y = pow(x, 2, n)
            if y == 1 and x != 1 and x != n - 1:
                return False  # Composite
            x = y

        if x != 1:
            return False  # Composite

    return True  # Probably prime

def deterministic_prime_test(primes, n):
    temp = int(n**0.5)
    result = True
    i=0
    
    while (primes[i]<temp & result):
        
        if (n%primes[i] != 0):
            result = True
        else: result = False
        i+=1
        
    return result

if __name__ == '__main__':
    primes = [2]
    t0 = time.time()
    k = 5
    N = 1_000_000

    for i in range(3, N):
        result = Miller_Rabin_primality_test(i, k)
    
        if result:
            real_prime = deterministic_prime_test(primes, i)
        
            if real_prime:
                primes += [i]
            
    print(f"time: {time.time() - t0} | num of primes: {len(primes)}")
