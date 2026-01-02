from math import gcd

# segfunc: 問題に応じて設定
def segfunc(x, y):
    return gcd(x, y)


# 配列aで初期化
def init(a):
    for i in range(n):
        seg[i+num-1] = a[i]    
    for i in range(num-2, -1, -1) :
        seg[i] = segfunc(seg[2*i+1], seg[2*i+2]) 


# a[k]の値をxに更新
def update(k, x):
    k += num - 1
    seg[k] = x
    while k:
        k = (k - 1) // 2
        seg[k] = segfunc(seg[k*2+1], seg[k*2+2])


# [p, q)についてsegfuncを適用したものを返す
def query(p, q):
    if q <= p:
        return ide_ele
    
    p += num - 1
    q += num - 2
    res = ide_ele

    while q - p > 1:
        if p & 1 == 0:
            res = segfunc(res, seg[p])
        if q & 1 == 1:
            res = segfunc(res, seg[q])
            q -= 1
        p = p // 2
        q = (q - 1) // 2
    
    if p == q:
        res = segfunc(res, seg[p])
    else:
        res = segfunc(res, segfunc(seg[p], seg[q]))
    
    return res


n = int(input())
a = list(map(int, input().split()))

ide_ele = 0
num = 2 ** (len(bin(n - 1)) - 2)
seg = [ide_ele] * 2 * num
init(a)

res = 0
for i in range(n):
    res = max(res, gcd(query(0, i), query(i+1, n)))

print(res)
