import sys
def input():
    return sys.stdin.readline()[:-1]
inf=float("inf")
n,m=map(int,input().split())
lrc=[list(map(int,input().split())) for i in range(m)]
lrc.sort()
# print(lrc)
li=[float('inf')]*n
li[0]=0
#####segfunc######
def segfunc(x,y):
   return min(x,y)

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

ide_ele = float('inf')

num =2**(n-1).bit_length()
seg=[ide_ele]*2*num
init(li)
# print(seg)
for i in range(m):
    tmp=query(lrc[i][0]-1,lrc[i][1]-1)
    tmp2=query(lrc[i][1]-1,lrc[i][1])
    if tmp2>lrc[i][2]+tmp:
        update(lrc[i][1]-1,lrc[i][2]+tmp)
    # print(seg[-num+n-2])
# print(seg)
if seg[-num+n-2]==float('inf'):
    print(-1)
else:
    print(seg[-num+n-2])