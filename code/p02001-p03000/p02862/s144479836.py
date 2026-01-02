import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
from math import factorial

fac = [0] * (10**6+5)
ifac = [0] * (10**6+5)
d = 10**9 + 7

def mpow(x, n):
    ans = 1
    while n != 0:
        if n&1:
            ans = ans * x % d
        x = x*x % d
        n = n >> 1
    return ans

def comb(a, b):
    if a == 0 and b == 0:
        return 1
    if a < b or a < 0:
        return 0
    tmp = ifac[a-b] * ifac[b] % d
    return tmp * fac[a] % d

def main():
    global fac, ifac
    x, y = map(int, input().strip().split())
    if (x + y) % 3 != 0:
        print(0)
        return
    k = (x+y) // 3
    q = x - k
    if x - 2 * q < 0 or q < 0:
        print(0)
        return

    fac[0] = 1
    ifac[0] = 1
    for i in range(10**6+1):
        fac[i+1] = fac[i]*(i+1) % d
        ifac[i+1] = ifac[i]*mpow(i+1, d-2) % d

    print(comb(k, q) % d)

if __name__ == '__main__':
    main()
