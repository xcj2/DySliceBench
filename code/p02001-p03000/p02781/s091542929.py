#!python3

from math import factorial

iim = lambda: map(int, input().rstrip().split())

def cmb(a, b):
    c = a - b
    if c < b:
        b = c
    if b == 0: return 1

    ans = 1
    for i in range(b):
        ans *= a - i

    return ans // factorial(b)

def cnt(N, K):
    if K == 0:
        return 1

    n10 = 10 ** (K-1)
    if N < n10:
        return 0

    n10 *= 10
    n9 = 9 ** K

    ans = 0
    a = n10
    i = 0
    while a < N:
        a *= 10; i += 1
    a //= 10; i -= 1
    if i >= 0:
        ans = cmb(i+K, K) * n9
        #print(f"{i+K}C{K}", ans)

    n, b = divmod(N, a)
    if n > 1:
        ans += (n - 1) * cnt(a-1, K - 1)
    ans += cnt(b, K - 1)


    return ans

def resolve():
    N = int(input())
    K = int(input())

    print(cnt(N, K))

if __name__ == "__main__":
    resolve()
