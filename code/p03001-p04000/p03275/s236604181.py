n=int(input())
a=list(map(int,input().split()))
ary=a.copy()
ary=sorted(list(set(ary)))
from bisect import bisect_left
aa=[bisect_left(ary,x) for x in a]
class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
        self.depth = n.bit_length()

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

def chk(x):
    c=[1 if ai<=x else -1 for ai in aa]
    cc=[0]
    tmp=0
    mi,ma=0,0
    for xx in c:
        tmp+=xx
        cc.append(tmp)
        mi=min(mi,tmp)
        ma=max(ma,tmp)
    # cc[r+1]-cc[l]>0となるl,rの組の数(l<=r)
    # cc[r+1]>cc[l]
    bit=Bit(ma-mi+1)
    ret=0
    for xx in cc:
        xx-=mi
        xx+=1
        bit.add(xx,1)
        ret+=bit.sum(xx-1)
    return ret>(((n+1)*n)//2)//2

l,r=0,n
while r-l>1:
    x=(l+r)//2
    if chk(x):
        l,r=l,x
    else:
        l,r=x,r
print(ary[l] if chk(l) else ary[r])
#print(l,chk(l),r)
