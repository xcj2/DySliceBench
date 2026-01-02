#####segfunc######
def segfunc(x,y):
    return max(x,y)

def init(init_val):
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
    
n,k = map(int,input().split())
a = [int(input()) for i in range(n)]
#n = int(input())
#a = tuple(map(int,input().split()))

#####単位元######
ide_ele = 0

#num:n以上の最小の2のべき乗
num =2**(max(a)-1).bit_length()
seg=[ide_ele]*2*num
#init(a)

ans = 0
max_a = max(a)

for i in range(n):
    tmp = query(max(0,a[i]-k),min(a[i]+k+1,max_a+1))
    #print(i,a[i],max(0,a[i]-k),min(a[i]+k,max(a)))
    update(a[i],tmp+1)
    #print(tmp)
    #print(st.query(0, max(a)))
    #ans = max(ans,tmp+1)
    #print(seg[0],k)
#print(seg)
#print(query(0,max(a)),seg[0])
print(seg[0])