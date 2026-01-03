
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
    idxlist[a-1] = i


ans = 0
seg = BIT(N,[0]*N)

def judge(l,r):
    if l>r:
        l,r = r,l
    res = seg.query(l,r+1)
    if res:
        return False
    else:
        return True


for idx in idxlist:    
    ng_l = -1
    ng_r = N
    left = idx
    while abs(left-ng_l)>1:
        mid = (left+ng_l)//2
        if judge(idx,mid):
            left = mid
        else:
            ng_l = mid
    
    right = idx
    while abs(ng_r-right)>1:
        mid = (right+ng_r)//2
        if judge(idx,mid):
            right = mid
        else:
            ng_r = mid
    
    ans += A[idx]*(idx-left+1)*(right-idx+1)
    seg.update(idx,1)
    
print(ans)



