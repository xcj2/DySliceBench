
def mod_inverse(a, p):
    return pow(a, p-2, p)  # フェルマーの小定理より

def mod_binominal(n, r, p):
    numerator= 1
    for i in range(r):
        numerator = (numerator * (n - i)) % p

    denominator = 1
    for i in range(1, r+1):
        denominator = (denominator * i) % p

    return (numerator * mod_inverse(denominator, p)) % p

def resolve():
    n, a, b = map(int, input().split())
    p = 10**9+7

    ans = pow(2, n, p) - mod_binominal(n, a, p) - mod_binominal(n, b, p) - 1
    print((ans + p) % p)


if __name__ == "__main__":
    resolve()