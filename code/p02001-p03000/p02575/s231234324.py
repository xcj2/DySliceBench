H, W = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(H)]

A = W+1
identity = -(1<<62)
sqrtA = 500
n_buckets = A // sqrtA + 1
Data = [0] * (n_buckets * sqrtA)
Data[0] = 1<<30
Bucket_min = [0] * n_buckets
Lazy = [identity] * n_buckets

def eval_data(k):
    if Lazy[k] != identity:
        l, r = k*sqrtA, (k+1) * sqrtA
        for i in range(l, r):
            Data[i] = i-Lazy[k]
        Lazy[k] = identity

def update(s, t, x):
    for k in range(s//sqrtA, (t-1)//sqrtA+1):
        l, r = k*sqrtA, (k+1)*sqrtA
        if s <= l and r <= t:
            Bucket_min[k] = l-x
            Lazy[k] = x
        else:
            eval_data(k)
            for i in range(max(l,s), min(r,t)):
                Data[i] = i-x
            Bucket_min[k] = min(Data[l:r])

def get_min(s, t):
    res = 1 << 62
    bl, br = s//sqrtA+1, t//sqrtA
    if bl > br:
        eval_data(br)
        return min(Data[s:t])
    if bl < br:
        res = min(Bucket_min[bl:br])
    ll, rr = bl*sqrtA, br*sqrtA
    if s < ll:
        eval_data(bl-1)
        mi = min(Data[s:ll])
        if res > mi:
            res = mi
    if rr < t:
        eval_data(br)
        mi = min(Data[rr:t])
        if res > mi:
            res = mi
    return res

Ans = []
for i, (a, b) in enumerate(AB, 1):
    update(a, b+1, a-1-get_min(a-1, a))
    ans = get_min(1, W+1)
    Ans.append(ans + i if ans < 1<<25 else -1)
print("\n".join(map(str, Ans)))
