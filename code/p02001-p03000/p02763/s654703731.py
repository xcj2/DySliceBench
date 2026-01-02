import sys
input = sys.stdin.readline

n = int(input())
s = str(input())
A = list(s)
A = A[0:n]

A = [{ord(c)-ord('a')} for c in A]
#print(A)

def segfunc(x, y):
    return x | y

def init(init_val):
    # set_val
    for i in range(n):
        seg[i+num-1] = init_val[i]
    # built
    for i in range(num-2, -1, -1):
        seg[i] = segfunc(seg[2*i+1], seg[2*i+2])

def update(k, x):
    k += num - 1
    seg[k] = x
    while k:
        k = (k-1)//2
        seg[k] = segfunc(seg[2*k+1], seg[2*k+2])

def query(p, q):
    if q <= p:
        return ide_ele
    p += num - 1
    q += num - 2
    res = ide_ele
    while q-p>1:
        if p%2 == 0:
            res = segfunc(res, seg[p])
        if q%2 == 1:
            res = segfunc(res, seg[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = segfunc(res, seg[p])
    else:
        res = segfunc(segfunc(res, seg[p]), seg[q])
    return res

# identity element
ide_ele = set()

# num: n以上の最小の2のべき乗
num = 2**(n-1).bit_length()
seg = [ide_ele]*2*num

init(A)

q = int(input())

for _ in range(q):
    c, x, y = map(str, input().split())
    if c == '1':
        x = int(x)-1
        y = {ord(y)-ord('a')}
        update(x, y)
    else:
        l = int(x)-1
        r = int(y)-1
        print(len(query(l, r+1)))