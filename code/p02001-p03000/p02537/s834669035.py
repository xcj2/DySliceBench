INT_MIN = 0

def init(n_):
    n = 1
    while n < n_:
        n *= 2
    dat = [INT_MIN] * (2*n-1)
    return n, dat

def update(k, a):
    k += n-1
    dat[k] = a
    while k > 0:
        k = (k-1) // 2
        dat[k] = max(dat[k * 2 + 1], dat[k * 2 + 2])

def query(l, r, n):
    res = INT_MIN
    l += n
    r += n
    while l < r:
        if l & 1:
            res = max(res, dat[l-1])
            l += 1
        if r & 1:
            r -= 1
            res = max(res, dat[r-1])
        l >>= 1
        r >>= 1
    return res

N, K = map(int, input().split())
A = [int(input()) for i in range(N)]
MAX_Ai = 3*10**5+1
n, dat = init(MAX_Ai)

for ai in A:
    max_len = query(max(ai-K, 0), min(ai+K+1, MAX_Ai), n)
    update(ai, max_len+1)
ans = query(0, MAX_Ai, n)
print(ans)