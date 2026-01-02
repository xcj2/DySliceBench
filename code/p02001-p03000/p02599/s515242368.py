from sys import stdin
input = stdin.readline
n, q = map(int ,input().split())
c = list(map(int, input().split()))
data = []
for i in range(q):
    data.append([i] + list(map(int, input().split())))
data.sort(key=lambda x : x[2])
ans = [0 for i in range(q)]
#####segfunc######
def segfunc(x,y):
    return x + y

def init(init_val):
    #set_val
    for i in range(len(init_val)):
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
num = 2**(n-1).bit_length()
seg=[ide_ele]*(2*num - 1)
good_ball = dict()
pre_r = 0
count = 0
for i in range(q):
    index, l, r = data[i]
    l, r = l-1, r-1
    for j in range(pre_r, r+1):
        if c[j] in good_ball: 
            update(good_ball[c[j]], 0)           
        update(j, 1)
        good_ball[c[j]] = j
    pre_r = r + 1
    ans[index] = query(l, r+1)
for i in range(q):
    print(ans[i])