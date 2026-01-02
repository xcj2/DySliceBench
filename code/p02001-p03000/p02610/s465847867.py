import sys
input = sys.stdin.buffer.readline

T = int(input())


def update_max(k,x):
    k += num_max-1
    seg_max[k] = x
    while k:
        k = (k-1)//2
        seg_max[k] = max(seg_max[k*2+1],seg_max[k*2+2])
    
def query_max(p,q):
    if q<=p:
        return ide_ele_max
    p += num_max-1
    q += num_max-2
    res=ide_ele_max
    while q-p>1:
        if p&1 == 0:
            res = max(res,seg_max[p])
        if q&1 == 1:
            res = max(res,seg_max[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = max(res,seg_max[p])
    else:
        res = max(max(res,seg_max[p]),seg_max[q])
    return res
def update_min(k,x):
    k += num_min-1
    seg_min[k] = x
    while k:
        k = (k-1)//2
        seg_min[k] = min(seg_min[k*2+1],seg_min[k*2+2])
def init_min(init_min_val):
    #set_val
    for i in range(n):
        seg_min[i+num_min-1]=init_min_val[i]    
    #built
    for i in range(num_min-2,-1,-1) :
        seg_min[i]=min(seg_min[2*i+1],seg_min[2*i+2])
def init_max(init_max_val):
    #set_val
    for i in range(n):
        seg_max[i+num_max-1]=init_max_val[i]    
    #built
    for i in range(num_max-2,-1,-1) :
        seg_max[i]=max(seg_max[2*i+1],seg_max[2*i+2]) 
def query_min(p,q):
    if q<=p:
        return ide_ele_min
    p += num_min-1
    q += num_min-2
    res=ide_ele_min
    while q-p>1:
        if p&1 == 0:
            res = min(res,seg_min[p])
        if q&1 == 1:
            res = min(res,seg_min[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = min(res,seg_min[p])
    else:
        res = min(min(res,seg_min[p]),seg_min[q])
    return res

#####単位元######
ide_ele_max = -1
#####単位元######
ide_ele_min = 10**10


dg = 10**6

for testcase in range(T):
    n = int(input())
    #num_max:n以上の最小の2のべき乗
    num_max =2**(n-1).bit_length()
    seg_max=[ide_ele_max]*2*num_max
    #num_min:n以上の最小の2のべき乗
    num_min =2**(n-1).bit_length()
    seg_min=[ide_ele_min]*2*num_min
    init_min(list(range(n)))
    init_max(list(range(n)))

    res = 0
    tank = []
    res = 0
    for i in range(n):
        K,L,R = map(int,input().split())
        K -= 1
        if L <= R:
            tank.append((R-L)*dg+K*2+1)
            res += L
        else:
            tank.append((L-R)*dg+K*2)
            res += R
    tank.sort(reverse = True)
    s = 0
    for e in tank:
        pt,amari = divmod(e,dg)
        idx,right = divmod(amari,2)
        if right == 0:
            kk = query_max(0,idx+1)
            if kk != -1:
                res += pt
                update_max(kk,-1)
        else:
            kk = query_min(idx+1,n)
            if kk != 10**10:
                res += pt
                update_min(kk,10**19)

    print(res)