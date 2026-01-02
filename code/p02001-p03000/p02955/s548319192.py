N, K = map(int, input().split())
A = [int(a) for a in input().split()]

S = sum(A)
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

D = divisors(S)

def chk(n):
    global K
    B = sorted([A[i]%n for i in range(N)])
    r = 0
    i, j = 0, N-1
    k = 0
    while i <= j:
        if r > 0:
            k += n-B[j]
            r -= n-B[j]
            j -= 1
        else:
            k += B[i]
            r += B[i]
            i += 1
    return 1 if k <= K*2 else 0

for d in D[::-1]:
    if chk(d):
        print(d)
        break