N, Q = map(int, input().split())

def init(N): #セグ木の初期化
    n = 1
    while n < N: n *= 2
    return n

def Update(i, x, n, L): #aiをxに変更する
    K = n - 1 + i
    L[K] = x
    while K > 0:
        K = (K - 1)//2
        L[K] = min(L[2 * K + 1], L[2 * K + 2])

def Find(s, t, k, l, r, L): #[s:t)の最小値を出力する
    if r <= s or t <= l: return 2**31-1
    elif s <= l and r <= t: return L[k]
    else:
        vl = Find(s, t, 2*k+1, l, (l+r)//2, L)
        vr = Find(s, t, 2*k+2, (l+r)//2, r, L)
        return min(vl, vr)

n = init(N)
SegTree = [2**31-1] * (2 * n - 1)
for i in range(Q):
    com, x, y = map(int, input().split())
    if com == 0:
        Update(x, y, n, SegTree)
    elif com == 1:
        print(Find(x, y+1, 0, 0, n, SegTree))
