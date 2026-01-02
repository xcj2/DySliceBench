import sys
input = sys.stdin.readline

def modPow(a, x, p):
    res = 1
    while x > 0:
        if x % 2 != 0:
            res = res * a % p
        a = a * a % p
        x = x // 2
    return res

def modInverse(a, p):
    return modPow(a, p - 2, p)

def modBinomial(n, k, p):
    numerator = 1
    for i in range(k):
        numerator = (numerator * (n - i)) % p

    denominator = 1
    for i in range(1, k + 1):
        denominator = (denominator * i) % p

    return (numerator * modInverse(denominator, p)) % p


def main():
    X, Y = [int(x) for x in input().split()]

    MOD = 10 ** 9 + 7
    y = (X - 2 * Y) // (-3)
    x = (X - y) // 2

    if y < 0 or x < 0:
        print(0)
        exit()
    if X == x * 2 + y and Y == x + 2 * y:
        print(modBinomial(x + y, x, MOD))
    else:
        print(0)









if __name__ == '__main__':
    main()

