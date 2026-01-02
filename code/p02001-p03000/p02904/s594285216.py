import sys
input = sys.stdin.readline
N, K = map(int,input().split())
P = list(map(int,input().split()))
count = 0
first = 1
def init(init_val,n):
    #set_val
    for i in range(n):
        seg[i+num-1]=init_val[i]
    #built
    for i in range(num-2,-1,-1) :
        seg[i]=segfunc(seg[2*i+1],seg[2*i+2])

def segfunc(x,y):
    return max([x,y])

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
num =2**(N-1).bit_length()
seg=[ide_ele]*2*num

def init2(init_val,n):
    #set_val
    for i in range(n):
        seg2[i+num-1]=init_val[i]
    #built
    for i in range(num-2,-1,-1) :
        seg2[i]=segfunc2(seg2[2*i+1],seg2[2*i+2])

def segfunc2(x,y):
    return min([x,y])

def update2(k,x):
    k += num-1
    seg2[k] = x
    while k:
        k = (k-1)//2
        seg2[k] = segfunc2(seg2[k*2+1],seg2[k*2+2])

def query2(p,q):
    if q<=p:
        return ide_ele2
    p += num-1
    q += num-2
    res=ide_ele2
    while q-p>1:
        if p&1 == 0:
            res = segfunc2(res,seg2[p])
        if q&1 == 1:
            res = segfunc2(res,seg2[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = segfunc2(res,seg2[p])
    else:
        res = segfunc2(segfunc2(res,seg2[p]),seg2[q])
    return res

#####単位元######
ide_ele2 = 10**9

#num:n以上の最小の2のべき乗
num =2**(N-1).bit_length()
seg2=[ide_ele2]*2*num

l = [0]*(N-1)
for i in range(len(l)):
    if P[i]>=P[i+1]:
        l[i] = 1
l2 = [0]*(N-K+1)
tmp = sum(l[0:K-1])
for i in range(N-K+1):
    if tmp==0:
        l2[i]=1
    if i != N-K:
        tmp += (l[i+K-1]-l[i])
init(P,N)
init2(P,N)
for i in range(N-K+1):
    if l2[i]==1:
        if first == 1:
            count += 1
            first = 0
        continue
    elif  (P[i-1] < query2(i,i+K-1)) and (P[i+K-1] > query(i,i+K-1)) and (i!=0):
        continue
    else:
        count += 1
print(count)
