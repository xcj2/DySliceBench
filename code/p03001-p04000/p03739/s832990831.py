import  copy
n = int(input())
a = list(map(int, input().split()))
check = copy.deepcopy(a)
#####segfunc######
def segfunc(x,y):
    return x+y

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
num =2**(n-1).bit_length()
seg=[ide_ele]*(2*num - 1)
init(a)
ans_1 = 0
pre_sum = (-1) * a[0]
for i in range(n):
    q_sum = query(0,i+1)
    if q_sum * pre_sum >= 0:
        if pre_sum < 0:
            update(i, abs(pre_sum) + 1)
        else:
            update(i, (-1) * (pre_sum+1))
    pre_sum = query(0,i+1)
for i in range(n):
    ans_1 += abs(check[i] - seg[i + num - 1])
if a[0] == 0:
    a[0] = 1
else:
    if a[0] < 0:
        a[0] = 1
    else:
        a[0] = -1
ans_2 = 0
pre_sum = (-1) * a[0]
init(a)
for i in range(n):
    q_sum = query(0,i+1)
    if q_sum * pre_sum >= 0:
        if pre_sum < 0:
            update(i, abs(pre_sum) + 1)
        else:
            update(i, (-1) * (pre_sum+1))
    pre_sum = query(0,i+1)
for i in range(n):
    ans_2 += abs(check[i] - seg[i + num - 1])
print(min(ans_1,ans_2))