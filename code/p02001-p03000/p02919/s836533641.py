
# 1-indexed　Binary Indexed Tree
class BIT:
    def __init__(self, n, init_list):
        self.num = n+1
        self.tree = [0]*self.num
        for i,e in enumerate(init_list):
            self.update(i,e)

    def update(self,k,x):
        k = k+1
        while k < self.num:
            self.tree[k] += x
            k += (k&(-k))
        return 
    
    # sum([l,r))
    def query(self, l,r):
        ret = 0
        while r>0:
            ret += self.tree[r]
            r -= r&(-r)
        while l>0:
            ret -= self.tree[l]
            l -= l&(-l)
        
        return ret


N = int(input())
A = list(map(int,input().split()))
#%%
idxlist = [0]*N
for i,a in enumerate(A):
    idxlist[a-1] = i+2

A = [N+1]*2 + A + [N+1]*2
#%%
ans = 0
seg = BIT(N+4,[1]*2+[0]*N+[1]*2)

def judge(l,r,key):
    if l>r:
        l,r = r,l
    res = seg.query(l,r+1)
    if res>key:
        return False
    else:
        return True

def bsearch(idx,ng,key):
    ok = idx
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if judge(idx,mid,key):
            ok = mid
        else:
            ng = mid
    return ng


for idx in reversed(idxlist):
    if A[idx]==N:
        seg.update(idx,1)
        continue
    ng_l = 0
    ng_r = N+3
    
    L1 = bsearch(idx,ng_l,0)
    L2 = bsearch(idx,ng_l,1)
    R1 = bsearch(idx,ng_r,0)
    R2 = bsearch(idx,ng_r,1)
    
    coef = 0
    if A[L1]!=N+1:
        coef += (L1-L2)*(R1-idx)
    if A[R1]!=N+1:
        coef += (R2-R1)*(idx-L1)
    ans += A[idx]*coef
    seg.update(idx,1)
    
print(ans)




