MAXN = 2 ** 17

ide_ele = 2 ** 31 - 1

n,q = map(int,input().split())

num = 2**(n-1).bit_length()
seg = [ide_ele] * 2 * num

def init(init_val):
    for i in range(n):
        seg[i+num-1] = init_val[i]
    for i in range(num-2 ,-1, -1) :
        seg[i] = segfunc(seg[2*i+1],seg[2*i+2])
        
def update(k,x):
    k += num-1
    seg[k] = x
    while k:
        k = (k-1)//2
        seg[k] = min(seg[k*2+1] , seg[k*2+2])
        
def query(p,q):
    p += num
    q += num
    res = ide_ele
    
    while q-p > 0:
        if p&1 == 1:
            res = min(res,seg[p-1])
            p += 1
            
        if q&1 == 1:
            q -= 1
            res = min(res,seg[q-1])
            
        p >>= 1
        q >>= 1
    return res

for i in range(q):
    com = input().split()
    if com[0] == "0":
        x,y = int(com[1]),int(com[2])
        update(x,y)
    else:
        x,y = int(com[1]),int(com[2])+1
        print(query(x,y))
