import sys
sys.setrecursionlimit(500000)

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]

def modinv(a, mod=10**9+7):
    return pow(a, mod-2, mod)

def combination(n, r, mod=10**9+7):
    r = min(r, n-r)
    if r < 0:
        return 0
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i+1, mod) % mod
    return res


def main():
    N, K = mi()
    MOD = 10**9+7
    for i in range(1, K+1):
        a = combination(N-K+1, i)*combination(K-1, i-1)
        print(a%MOD)



if __name__ == '__main__':
    main()
