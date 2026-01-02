import sys
input = sys.stdin.readline
n, q = map(int, input().split())

size = 2**((n-1).bit_length())
tree = [None]*(size*2)
INF = (-1, 2**31-1)

def _find(i):
    ind = size+i
    s = INF
    while ind:
        if tree[ind]:
            s = max(s, tree[ind])
        ind = ind//2
    return s
def find(i):
    return _find(i)[1]

def update(s, t, v):
    L = s+size;R = t+size
    while L<R:
        if L&1:
            tree[L]=v
            L+=1
        if R&1:
            R-=1
            tree[R]=v

        L>>=1;R>>=1

res = []
for i in range(q):
    a, *b = map(int, input().split())
    if a:res.append(find(b[0]))
    else:update(b[0],b[1]+1,(i,b[2]))
print('\n'.join(map(str,res)))
