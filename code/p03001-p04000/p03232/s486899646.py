# -*- coding: utf-8 -*-

import sys
import itertools
import math

def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def perm(n, r):
    return math.factorial(n) // math.factorial(n - r)

MOD = 1000000007

def powm(n, p):
    if p == 0:
        return 1
    elif p % 2 == 0:
        x = powm(n, p // 2)
        return (x * x) % MOD
    else:
        x = powm(n, p - 1)
        return (x * n) % MOD

def invm(n):
    return powm(n, MOD - 2)

def makeTbFac(N):
    tbFac = list(range(N+1))
    tbFac[0] = 1
    for i in range(1,N+1):
        tbFac[i] *= tbFac[i-1]
        tbFac[i] %= MOD
    return tbFac

def prob(i,j):
    return 1 / (abs(j-i) + 1)

def coef(j,N):
    U = 0
    for k in range(0, N):
        U += prob(k,j)
    return U * math.factorial(N)

def probm(i,j):
    return invm(abs(j-i) + 1)

def coefm(j,N,tbFac):
    U = 0
    for k in range(0, N):
        U += probm(k,j)
        U %= MOD
    return U * tbFac[N] % MOD

def cost(xs):
    L = len(xs)
    if L == 0:
        return 0
    if L == 1:
        return xs[0]
    if L == 2:
        return 3 * (xs[0] + xs[1])
    if L == 3:
        return 11 * (xs[0] + xs[2]) + xs[1] * 12

    T = 0
    for i in range(L):
        s = sum(xs) * math.factorial(L-1)
        leftLen = i
        rightLen = L-i-1
        left = 0
        right = 0
        if leftLen > 0:
            #left = cost(xs[:i]) * math.factorial(rightLen) * comb(L-1, rightLen)
            left = cost(xs[:i]) * perm(L-1, rightLen)
        if rightLen > 0:
            #right = cost(xs[i+1:]) * math.factorial(leftLen) * comb(L-1, leftLen)
            right = cost(xs[i + 1:]) * perm(L - 1, leftLen)
        T += (s + left + right) % MOD
    return T % MOD

def main():
    """
    for N in range(10):
        ls = list(range(N))
        cnt = [0] * N
        for p in itertools.permutations(ls, N):
            blocks = [True] * N
            for i in p:
                cnt[i]+=1
                k = i - 1
                while k >= 0 and blocks[k]:
                    cnt[k]+=1
                    k-=1
                k = i + 1
                while k < N and blocks[k]:
                    cnt[k]+=1
                    k+=1
                blocks[i] = False
        print(cnt)
    """
    N = int(input())
    As = [int(x) for x in input().split()]

    tbFac = makeTbFac(N)

    def makeTbInvSum(N):
        tb = [0] * N
        for k in range(1, N):
            tb[k] = (tb[k-1] + invm(k)) % MOD
        return tb

    tbInvSum = makeTbInvSum(N+1)

    ret = 0
    for i in range(N):
        co1 = tbInvSum[i+1] * tbFac[N] % MOD
        co2 = tbInvSum[N-i] * tbFac[N] % MOD
        coef = co1 + co2 - tbFac[N]
        ret += As[i] * coef
        ret %= MOD

    #ret = cost(As)

    # 出力
    print("{}".format(ret))

if __name__ == '__main__':
    main()

