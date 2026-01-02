import sys,bisect
input = sys.stdin.readline
n,d,a = map(int,input().split())

def segfunc(x,y):
    return x+y

def init(init_val):
    #set_val
    for i in range(n):
        seg[i+num-1]=init_val[i]    
    #built
    for i in range(num-2,-1,-1) :
        seg[i]=segfunc(seg[2*i+1],seg[2*i+2]) 
    
def update(k,x):
    k += num-1
    seg[k] = x
    while k:
        k = (k-1)//2
        seg[k] = segfunc(seg[k*2+1],seg[k*2+2])
    
def query(p,q):
    if q<=p:
        return ide_ele
    p += num-1
    q += num-2
    res=ide_ele
    while q-p>1:
        if p&1 == 0:
            res = segfunc(res,seg[p])
        if q&1 == 1:
            res = segfunc(res,seg[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = segfunc(res,seg[p])
    else:
        res = segfunc(segfunc(res,seg[p]),seg[q])
    return res

#####単位元######
ide_ele = 0

#num:n以上の最小の2のべき乗
num =2**(n-1).bit_length()
seg=[ide_ele]*2*num


xh = []
dg = 10**10

for i in range(n):
    x,h = map(int,input().split())
    xh.append(x*dg+h)

xh.sort()

res = 0

for i in range(n):
    x,h = xh[i]//dg,xh[i]%dg
    k1 = bisect.bisect_left(xh,(x-2*d)*dg)
    
    r = query(k1,i)

    h -= r*a
    if h <= 0:
        continue

    if h%a == 0:
        res += h//a
        update(i,h//a)
    else:
        res += h//a+1
        update(i,h//a+1)
    
print(res)