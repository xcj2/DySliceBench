def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def main():
    N = int(input())
    A = list(map(int, input().split()))

    all_prime = set()
    is_pairwise = True
    for a in A:
        facts = set(prime_factorize(a))
        if len(facts & all_prime) != 0:
            is_pairwise = False
            break

        all_prime |= facts

    if is_pairwise:
        print('pairwise coprime')
        return

    _gcd = A[0]
    is_setwise = False
    for a in A[1:]:
        _gcd = gcd(a, _gcd)
        if _gcd == 1:
            is_setwise = True
            break
    
    if is_setwise:
        print('setwise coprime')
    else:
        print('not coprime')

if __name__ == '__main__':
    main()