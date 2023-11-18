import time

def find_prime(n):
    MIN_NUMBER = 2
    MAX_NUMBER = n
    primeArray = []
    
    for i in range(MIN_NUMBER,MAX_NUMBER):
        result = False
        temp = int(i**0.5)
        
        for prime in primeArray[:temp]:
            if (i%prime == 0):
                result = True
                break
            
        if not result: primeArray.append(i)

    return primeArray


if __name__ == '__main__':
    N = 10_000_000

    start = time.time()

    primes = find_prime(N)

    end = time.time()

    print(f"Lage prime: {len(primes)}")
    print(f"Wellington's algorithm: {end - start}")
