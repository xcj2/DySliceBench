
n, q = map(int, input().split())
size = 1
while size < n:
    size *= 2
size = size
seg_tree = [0]*(size*2)

def update(i, x):
    ind = size-1+i
    seg_tree[ind] += x
    while ind>1:
        ind = ind//2
        left = seg_tree[ind*2]
        right = seg_tree[ind*2+1]
        seg_tree[ind] = left + right

def _find(s,t,i,l,r):
    if r < s or t < l:return 0
    if s <= l and r <= t:
        return seg_tree[i]
    else:
        left = _find(s,t,i*2,l, (l+r)//2)
        right = _find(s,t,i*2+1,(l+r)//2+1,r)
        return left+right

def find(s,t):
    return _find(s,t,1,1,size)

for _ in range(q):
    com, x, y = map(int, input().split())
    if not com:
        update(x, y)
    else:
        print(find(x,y))
