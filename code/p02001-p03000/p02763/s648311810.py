"""segfunc"""


# 論理和を返す
def segfunc(x, y):
    return x | y


def init(init_val):
    # set_val
    for i in range(N):
        seg[i-1+num] = init_val[i]

    # built
    for i in range(num-2, -1, -1):  # 木の下の方から埋めていく, nではなくnumであることに注意
        seg[i] = segfunc(seg[2*i+1], seg[2*i+2])  # 子のインデックス


# 更新
def update(k, x):
    k += num-1  # 場所kに対するseg木の葉のindex?
    seg[k] = x
    while k:
        k = (k-1)//2  # 親のノードのindexを取得
        seg[k] = segfunc(seg[2*k+1], seg[2*k+2])


def query(p, q):
    if q <= p:  # 半開区間なので、等しくてもアウト？
        return ide_ele
    p += num-1
    q += num-2  # 半開区間なので、q側を-2している？
    res = ide_ele
    while q-p > 1:
        if p % 2 == 0:
            res = segfunc(res, seg[p])
        if q % 2 == 1:
            res = segfunc(res, seg[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = segfunc(res, seg[p])
    else:
        res = segfunc(segfunc(res, seg[p]), seg[q])
    return res


# 単位元
ide_ele = 0

N = int(input())
ss = list(input())
s = []
for i in range(N):
    s.append(1<<(ord(ss[i]))-97)

# num: n以上の最小の2のベキ乗
num = 2**(N-1).bit_length()
seg = [ide_ele]*2*num

init(s)


def popcnt(n):
    c = (n & 0x5555555555555555) + ((n>>1) & 0x5555555555555555)
    c = (c & 0x3333333333333333) + ((c>>2) & 0x3333333333333333)
    c = (c & 0x0f0f0f0f0f0f0f0f) + ((c>>4) & 0x0f0f0f0f0f0f0f0f)
    c = (c & 0x00ff00ff00ff00ff) + ((c>>8) & 0x00ff00ff00ff00ff)
    c = (c & 0x0000ffff0000ffff) + ((c>>16) & 0x0000ffff0000ffff)
    c = (c & 0x00000000ffffffff) + ((c>>32) & 0x00000000ffffffff)
    return c


q = int(input())
for i in range(q):
    qq, xx, yy = map(str, input().split())
    if qq == '1':
        xx = int(xx)
        update(xx-1,1<<(ord(yy)-97))
    else:
        xx, yy = int(xx), int(yy)
        res = query(xx-1,yy)
        print(popcnt(res))
