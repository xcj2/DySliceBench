N = int(input())
P = list(map(int, input().split()))

def init_min(init_min_val):
    #set_val
    for i in range(N):
        seg_min[i+num_min-1]=init_min_val[i]    
    #built
    for i in range(num_min-2,-1,-1) :
        seg_min[i]=min(seg_min[2*i+1],seg_min[2*i+2]) 
    
def update_min(k,x):
    k += num_min-1
    seg_min[k] = x
    while k:
        k = (k-1)//2
        seg_min[k] = min(seg_min[k*2+1],seg_min[k*2+2])
    
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
ide_ele_min = 10**10

#num_min:n以上の最小の2のべき乗
num_min =2**(N-1).bit_length()
seg_min=[ide_ele_min]*2*num_min
init_min(P)

answer = 1

for i in range(1, N):
    MIN = query_min(0, i)
    if MIN > P[i]:
        answer += 1

print(answer)