def prime_factorize(n):
    ans = []
    while True:
        if n % 2 == 0:
            ans.append(2)
            n //= 2
        else:
            break
    div = 3

    while div*div <= n:
        if n % div == 0:
            ans.append(div)
            n //= div
        else:
            div += 2

    if n != 1:
        ans.append(n)

    return ans


def eratosthenes_shieve(n):
    is_prime = [True for i in range(n+1)]
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, n+1):
        if not is_prime[i]:
            continue
        for j in range(i*2, n+1, i):
            is_prime[j] = False
    
    return [i for i in range(len(is_prime)) if is_prime[i]]


def eratosthenes_shieve_pf(n):
    primes = eratosthenes_shieve(int(n**0.5)+1)
    ans = []
    for p in primes:
        while n % p == 0:
            ans.append(p)
            n //= p

    if n != 1:
        ans.append(n)

    return ans


def main():
    n = int(input())
    # ans = prime_factorize(n)
    ans = eratosthenes_shieve_pf(n)
    s = "{}: ".format(n)
    for i in ans:
        s += str(i) + " "
    print(s[:-1])


if __name__ == "__main__":
    main()

