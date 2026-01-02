from heapq import *
import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

class SegtreeMax():
    def __init__(self, aa):
        n=len(aa)
        self.inf = 10 ** 16
        tree_width = 2
        while tree_width < n:
            tree_width *= 2
        self.tree_width = tree_width
        self.tree = [0] * (tree_width * 2 - 1)
        self.tree[self.tree_width-1:self.tree_width-1+len(aa)]=aa
        for i in range(tree_width-2,-1,-1):
            self.tree[i]=max(self.tree[i*2+1],self.tree[i*2+2])

    def update(self, i, a):
        seg_i = self.tree_width - 1 + i
        self.tree[seg_i] = a
        while seg_i != 0:
            seg_i = (seg_i - 1) // 2
            self.tree[seg_i] = max(self.tree[seg_i * 2 + 1], self.tree[seg_i * 2 + 2])

    def element(self, i):
        return self.tree[self.tree_width - 1 + i]

    # [l,r)の最小値
    def max(self, l, r, seg_i=0, segL=0, segR=-1):
        if segR == -1: segR = self.tree_width
        if r <= segL or segR <= l: return 0
        if l <= segL and segR <= r: return self.tree[seg_i]
        segM = (segL + segR) // 2
        ret0 = self.max(l, r, seg_i * 2 + 1, segL, segM)
        ret1 = self.max(l, r, seg_i * 2 + 2, segM, segR)
        return max(ret0, ret1)

for _ in range(II()):
    n=II()
    hp=[]
    hpr=[]
    ans=0
    for _ in range(n):
        k,l,r=MI()
        if r<l:heappush(hp,(r-l,l,r,k))
        elif r>l:heappush(hpr,(-r+l,l,r,k))
        else:ans+=r

    st=SegtreeMax(list(range(n+5)))
    for i in range(n+1):st.update(i,i)
    while hp:
        d,l,r,k=heappop(hp)
        i=st.max(0,k+1)
        if i:
            ans+=l
            st.update(i,0)
        else:
            ans+=r

    st=SegtreeMax(list(range(n+5)))
    for i in range(n+1):st.update(i,i)
    while hpr:
        d,l,r,k=heappop(hpr)
        k=n-k
        i=st.max(0,k+1)
        if i:
            ans+=r
            st.update(i,0)
        else:
            ans+=l

    print(ans)
