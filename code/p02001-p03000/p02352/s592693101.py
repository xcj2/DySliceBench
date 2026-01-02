import sys
input = sys.stdin.readline

n, q = map(int, input().split())

Len = (n-1).bit_length()
size = 2**Len
tree = [0]*(2*size)
lazy = [0]*(2*size)
INF = 2**31 -1

def gindex(l,r):
    box = []
    L = (l+size)>>1;R=(r+size)>>1
    lc = 0 if l & 1 else (L&-L).bit_length()
    rc = 0 if r & 1 else (R&-R).bit_length()
    for i in range(Len):
        if rc <= i:
            box.append(R)
        if L < R and lc <= i:
            box.append(L)
        L >>= 1; R >>= 1
    return box
        
        

def propagates(ids):
    for i in reversed(ids):
        v = lazy[i]
        if v is None:
            continue
        lazy[2*i] += v
        tree[2*i] += v
        lazy[2*i+1] += v
        tree[2*i+1] += v
        lazy[i]=0

def update(l,r,x):
    L = size+l
    R = size+r
    while L<R:
        if R&1:
            R -= 1
            lazy[R] += x
            tree[R] += x
        if L&1:
            lazy[L] += x
            tree[L] += x
            L+=1
        L>>=1;R>>=1
    ids = gindex(l,r)
    for i in ids:
        if 2*i+1<size*2:
            tree[i]= min(tree[i*2],tree[i*2+1]) + lazy[i]
        
def query(l, r):
    ids = gindex(l, r)
    propagates(ids)
    L = size + l
    R = size + r
    s = INF
    while L<R:
        if R&1:
            R-=1
            s =min(s, tree[R])
        if L&1:
            s =min(s, tree[L])
            L+=1
        L>>=1;R>>=1
    return s

ans = []
for i in range(q):
    a, *b = map(int, input().split())
    if a:
        ans.append(query(b[0],b[1]+1))
    else:
        update(b[0],b[1]+1,b[2])
        
print('\n'.join(map(str,ans)))
