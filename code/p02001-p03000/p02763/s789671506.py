N = int(input())
S = list(input())
Q = int(input())

'''
'init(a)': 配列aで初期化。O(N)
'update(k,x)': a[k]をxに変更 O(logN)
'query(p,q)': [p,q)について "segfunc" したものを返す O(logN)
'ide_ele' : 単位元。
'''

#####segfunc######


def segfunc(x, y):
    return x | y


def init(init_val):
    # set_val
    for i in range(N):
        seg[i+num-1] = init_val[i]
    # built
    for i in range(num-2, -1, -1):
        seg[i] = segfunc(seg[2*i+1], seg[2*i+2])


def update(k, x):
    k += num-1
    seg[k] = x
    while k:
        k = (k-1)//2
        seg[k] = segfunc(seg[k*2+1], seg[k*2+2])


def query(p, q):
    if q <= p:
        return ide_ele
    p += num-1
    q += num-2
    res = ide_ele
    while q-p > 1:
        if p & 1 == 0:
            res = segfunc(res, seg[p])
        if q & 1 == 1:
            res = segfunc(res, seg[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = segfunc(res, seg[p])
    else:
        res = segfunc(segfunc(res, seg[p]), seg[q])
    return res


#####単位元######
ide_ele = 0

# num:n以上の最小の2のべき乗
num = 2**(N-1).bit_length()
seg = [ide_ele]*2*num


init_val = []
for s in S:
    init_val.append(1 << (ord(s)-ord('a')))
init(init_val)

for _ in range(Q):
    t, s, u = input().split()
    if t == '1':
        update(int(s)-1, 1 << (ord(u)-ord('a')))
    else:
        print(bin(query(int(s)-1, int(u))).count('1'))
