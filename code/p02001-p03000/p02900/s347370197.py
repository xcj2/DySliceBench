import sys

sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return list(map(int, sys.stdin.readline().split()))
def II(): return int(sys.stdin.readline())
def LS(): return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]

from collections import Counter

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


def main():
    a, b = LI()
    a_s = prime_factorize(a)
    b_s = prime_factorize(b)
    a_keys = set(Counter(a_s).keys())
    b_keys = set(Counter(b_s).keys())
    print(str(1 + len(a_keys & b_keys)))

if __name__ == '__main__':
    main()

