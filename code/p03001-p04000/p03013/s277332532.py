import sys
sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1


def II(): return int(input())


def MI(): return map(int, input().split())


def MI1(): return map(int1, input().split())


def LI(): return list(map(int, input().split()))


def LLI(rows_number): return [LI() for _ in range(rows_number)]


def Fibo(n, memo={}):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = Fibo(n - 1, memo) + Fibo(n - 2, memo)
        return memo[n]


def solve():
    n, m = MI()

    s = 0
    mod = 1000000007
    ans = 1
    for _ in range(m):
        t = II() - 1
        d = t - s
        if d < 0:
            keiro = 0
        else:
            keiro = Fibo(d + 2)
        # print(s, t, d, keiro)
        ans = ans * keiro % mod
        s = t + 2
    d = n - s
    if d < 0:
        keiro = 0
    else:
        keiro = Fibo(d + 2)

    ans = ans * keiro % mod
    print(ans % mod)


if __name__ == '__main__':
    solve()
