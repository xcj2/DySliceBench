def eratosthenes(N):
    is_prime = {i: True for i in range(2, N+1)}
    primes = []
    for i in range(2, N+1):
        if is_prime[i]:
            primes.append(i)
            if i**2 <= N:
                for j in range(i**2, N+1, i):
                    is_prime[j] = False
    return primes


def gcd(a, b):
    a, b = max(a, b), min(a, b)
    if b == 0:
        return a
    return gcd(b, a % b)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    allgcd = A[0]
    primes = eratosthenes(1000)
    divs = set()
    pairwise_coprime = True
    for a in A:
        if allgcd > 1:
            allgcd = gcd(allgcd, a)
        if not pairwise_coprime:
            continue
        for p in primes:
            if a % p == 0:
                if p in divs:
                    pairwise_coprime = False
                while a % p == 0:
                    a //= p
                divs.add(p)
            if a == 1:
                break
        if a != 1:
            if a in divs:
                pairwise_coprime = False
            divs.add(a)
    if pairwise_coprime:
        print("pairwise coprime")
    else:
        if allgcd == 1:
            print("setwise coprime")
        else:
            print("not coprime")


if __name__ == "__main__":
    main()
