def primeFactor(N):
    i, n, ret, d, sq = 2, N, {}, 2, 99
    while i <= sq:
        k = 0
        while n % i == 0: n, k, ret[i] = n//i, k+1, k+1
        if k > 0 or i == 97: sq = int(n**(1/2)+0.5)
        if i < 4: i = i * 2 - 1
        else: i, d = i+d, d^6
    if n > 1: ret[n] = 1
    return ret

def divisors(N):
    pf = primeFactor(N)
    ret = [1]
    for p in pf:
        ret_prev = ret
        ret = []
        for i in range(pf[p]+1):
            for r in ret_prev:
                ret.append(r * (p ** i))
    return sorted(ret)

def f(b, n):
    re = 0
    while n:
        re += n % b
        n //= b
    return re

N = int(input())
S = int(input())
if N < S:
    print(-1)
elif N == S:
    print(N+1)
else:
    for b in divisors(N-S):
        b += 1
        if f(b, N) == S:
            print(b)
            break
    else:
        print(-1)
