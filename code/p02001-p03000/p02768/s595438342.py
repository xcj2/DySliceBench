import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def powr(i, j, d):
    p = j
    ans = 1
    while p != 0:
        if p % 2 == 1:
            ans = (ans * i) % d
        i = i**2 % d
        p >>= 1
    return ans

def div(i, j):
    # 1/i mod(j)
    # calc i**(j-2) mod(j)
    return powr(i, j-2, j)

# def make_comb(m, d):
#     fac = [0] * (m+1)
#     ifac = [0] * (m+1)
#     # nCk
#     fac[0] = 1
#     ifac[0] = 1
#     for i in range(m):
#         fac[i+1] = (fac[i] * (i+1)) % d
#         ifac[i+1] = (ifac[i] * div(i+1, d)) % d
#     def comb(n, k):
#         if n == 0 and k == 0:
#             return 1
#         if n < k or n < 0:
#             return 0
#         return (fac[n] * ifac[k] * ifac[n-k]) % d
#     return comb

def nck(n, k, d):
    ans = 1
    for i in range(n-(k-1), n+1):
        ans *= i % d
        ans %= d
    for i in range(1, k+1):
        ans *= div(i, d)
        ans %= d
    return ans % d

def main():
    n, a, b = list(map(int, input().strip().split()))
    d = 10**9+7
    # comb = make_comb(10**6, d)
    ans = (powr(2, n, d) - 1 - nck(n, a, d) - nck(n, b, d)) % d
    if ans < 0:
        print(ans + d)
    else:
        print(ans)

    # print(comb(10, 2))
    # print(comb(5, 2))


if __name__ == '__main__':
    main()
