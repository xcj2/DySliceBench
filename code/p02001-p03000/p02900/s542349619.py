import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def factorization(num):
    import math
    # 因数分解した結果をタプルのリストで返す
    # [(prime, count), ...]
    MAX_PRIME = int(math.sqrt(num)) + 1
    primes = []
    is_prime = [True] * (MAX_PRIME+1)
    for i in range(2, MAX_PRIME+1):
        if is_prime[i]:
            primes.append(i)
            for j in range(2*i, MAX_PRIME+1, i):
                is_prime[j] = False
    insu = []
    tmp = num
    max_count = 0
    for i in range(len(primes)):
        count = 0
        while tmp%primes[i] == 0:
            tmp //= primes[i]
            count += 1
        if count > 0:
            insu.append((primes[i], count))
            max_count = max(max_count, count)
        if tmp == 1:
            break
    if tmp != 1:
        insu.append((tmp, 1))
    return insu

def main():
    A, B = map(int, input().split())
    gcd_ = gcd(A, B)

    insu = factorization(gcd_)
    print(len(insu) + 1)

if __name__ == "__main__":
    main()