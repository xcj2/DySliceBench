from collections import defaultdict

alpha = defaultdict(int)
num = 0
for i in sorted(map(chr,range(97,123))):
    alpha[i] = 1 << num
    num += 1

n = int(input())
S = tuple(alpha[i] for i in input())

def init(init_val):
    #set_val
    for i in range(n):
        seg[i+num-1] = init_val[i]
    #built
    for i in range(num-2,-1,-1):
        seg[i] = seg[2*i+1] | seg[2*i+2]
    
def update(k,x):
    k += num-1
    seg[k] = x
    while k:
        k = (k-1)//2
        seg[k] = seg[k*2+1] | seg[k*2+2]
    
def query(p,q):
    if q<=p:
        return 0
    p += num-1
    q += num-2
    res=0
    while q-p>1:
        if p&1 == 0:
            res |= seg[p]
        if q&1 == 1:
            res |= seg[q]
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res |= seg[p]
    else:
        res |= (seg[p] | seg[q])
    cnt = 0
    i = 0
    while res:
        cnt += res & 1
        i += 1
        res >>= 1
    return cnt
#num:n以上の最小の2のべき乗
num =2**(n-1).bit_length()
seg=[0 for _ in range(2*num)]

init(S)

Q = int(input())
for _ in range(Q):
    x,y,z = map(str,input().split())
    x = int(x); y = int(y)
    if x == 1:
        update(y-1, alpha[z])
    else:
        z = int(z)
        print(query(y-1,z))