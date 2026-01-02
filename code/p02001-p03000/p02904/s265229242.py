N,K=map(int,input().split())
P=list(map(int,input().split()))

LIS=[1 for i in range(0,N)]
s=0
t=1
while N>t:
    if P[t]>=P[t-1]:
        t+=1
        if t==N:
            ans=N-s
            while t>s:
                LIS[s]=ans
                s+=1
                ans-=1
    else:
        ans=t-s
        while t>s:
            LIS[s]=ans
            s+=1
            ans-=1
        t+=1

nochange=set([])
for i in range(0,N-K+1):
    if LIS[i]>=K:
        nochange.add(i)

n=N
#セグメント木
#####segfunc######
def segfunc(x,y):
    return (min(x[0],y[0]),max(x[1],y[1]))

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
ide_ele =(10**20,0)

#num:n以上の最小の2のべき乗
num =2**(n-1).bit_length()
seg=[ide_ele]*2*num
PP=[(P[i],P[i]) for i in range(0,N)]
init(PP)
ans=[]
if 0 not in nochange:
    ans.append(0)
for i in range(1,N-K+1):
    if i in nochange:
        continue
    else:
        M=query(i,i+K)[1]
        m=query(i-1,i-1+K)[0]
        if m==P[i-1] and M==P[i+K-1]:
            continue
        else:
            ans.append(i)

if nochange:
    print(len(ans)+1)
else:
    print(len(ans))
