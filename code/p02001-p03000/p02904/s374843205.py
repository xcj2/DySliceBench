n,k = map(int,input().split())
p = list(map(int,input().split()))

def init_max(init_val):
    #set_val
    for i in range(n):
        seg[i+num-1]=init_val[i]    
    #built
    for i in range(num-2,-1,-1) :
        seg[i]=max(seg[2*i+1],seg[2*i+2]) 
    
def update_max(k,x):
    k += num-1
    seg[k] = x
    while k+1:
        k = (k-1)//2
        seg[k] = max(seg[k*2+1],seg[k*2+2])
    
def query_max(p,q):
    if q<=p:
        return ide_ele
    p += num-1
    q += num-2
    res=ide_ele
    while q-p>1:
        if p&1 == 0:
            res = max(res,seg[p])
        if q&1 == 1:
            res = max(res,seg[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = max(res,seg[p])
    else:
        res = max(max(res,seg[p]),seg[q])
    return res

def init_min(init_val):
    #set_val
    for i in range(n):
        seg[i+num-1]=init_val[i]    
    #built
    for i in range(num-2,-1,-1) :
        seg[i]=min(seg[2*i+1],seg[2*i+2]) 
    
def update_min(k,x):
    k += num-1
    seg[k] = x
    while k:
        k = (k-1)//2
        seg[k] = min(seg[k*2+1],seg[k*2+2])
    
def query_min(p,q):
    if q<=p:
        return ide_ele
    p += num-1
    q += num-2
    res=ide_ele
    while q-p>1:
        if p&1 == 0:
            res = min(res,seg[p])
        if q&1 == 1:
            res = min(res,seg[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = min(res,seg[p])
    else:
        res = min(min(res,seg[p]),seg[q])
    return res


#####単位元######
ide_ele = -1

#num:n以上の最小の2のべき乗
num =2**(n-1).bit_length()
seg=[ide_ele]*2*num

init_max(p)

a = [-1]*(n-k+1)
for i in range(n-k+1):
    a[i] = query_max(i,i+k)

#####単位元######
ide_ele = n

#num:n以上の最小の2のべき乗
num =2**(n-1).bit_length()
seg=[ide_ele]*2*num

init_min(p)

b = [-1]*(n-k+1)
for i in range(n-k+1):
    b[i] = query_min(i,i+k)

c = [1]*n
d = [True]*n
for i in range(n-2,-1,-1):
    if p[i] < p[i+1]:
        c[i] = c[i+1]+1
        if c[i] >= k:
            d[i] = False



res = 0
res2 = 0


for i in range(n-k):
    if not d[i]:
        res2 = 1
        continue
    if b[i] == p[i] and a[i+1] == p[i+k]:
        continue
    res += 1
if d[n-k]:
    res += 1

if n==k:
    print(1)
else:
    print(res+res2)
