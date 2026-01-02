import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
p = list(map(lambda x: int(x)-1, input().split()))

def init(bit, values):
    for i,v in enumerate(values):
        add(bit,i+1,v)
#a1 ~ aiまでの和 O(logn)
def query(bit,i):
    res = 0
    while i > 0:
        res += bit[i]
        i -= i&(-i)
    return res

#ai += x(logN)
def add(bit,i,x):
    if i==0:
        raise RuntimeError
    while i <= len(bit)-1:
        bit[i] += x
        i += i&(-i)
    return

def index(bit, v):
    """a1,...,aiの和がv以上になる最小のindexを求める
    存在しないとき配列サイズを返す
    """
    i = 0
    n = len(bit)-1
    k = 1<<((n-1).bit_length())
#     k = 1
#     while 2*k<n:
#         k *= 2
    while k>0:
        if i+k<n+1 and bit[i+k]<v:
            v -= bit[i+k]
            i += k
        k //= 2
    if v==1:
        return i+1
    else:
        return n+1

ind = [None]*n
for i,num in enumerate(p):
    ind[num] = i
bit = [0]*(n+1)
l = [None]*n
l2 = [None]*n
r = [None]*n
r2 = [None]*n
for num in range(n-1, -1, -1):
    i = query(bit, ind[num])
    if i==0:
        l[ind[num]] = -1
        l2[ind[num]] = -1
    elif i==1:
        l[ind[num]] = index(bit, i) - 1
        l2[ind[num]] = -1
    else:
        l[ind[num]] = index(bit, i) - 1
        l2[ind[num]] = index(bit, i-1) - 1
    r[ind[num]] = index(bit, i+1) - 1
    r2[ind[num]] = index(bit, i+2) - 1
    add(bit, ind[num]+1, 1)

    
ans = 0
for i, (num, li, li2, ri, ri2) in enumerate(zip(p, l, l2, r, r2)):
    v = 0
    if li>=0:
        v += (ri-i)*(li-li2)
    if ri<n:
        v += (i-li)*(ri2-ri)
#     print(i,li,li2, ri, ri2,v)
    ans += v * (num+1)
print(ans)