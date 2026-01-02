
import sys
import collections

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
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
    n = I()
    ans = 0
    for c in range(1, n):
        t = list(collections.Counter(prime_factorize(n-c)).values())
        s = 1
        for key in t:
            s *= key+1
        ans += s
    print(ans)

if __name__ == '__main__':
    main()