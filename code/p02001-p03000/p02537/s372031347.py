import sys

sys.setrecursionlimit(10**6)
int1 = lambda x: int(x)-1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

class SegtreeMax():
    def __init__(self, aa):
        self.inf = 10 ** 16
        self.n = n = len(aa)
        self.tree_width = tree_width = 1 << (n - 1).bit_length()
        self.tree = [-self.inf] * (tree_width * 2 - 1)
        self.tree[tree_width-1:tree_width-1+n]=aa
        for u in range(tree_width - 2, -1, -1):
            self.tree[u] = max(self.tree[u * 2 + 1], self.tree[u * 2 + 2])

    def update(self, i, a):
        seg_i = self.tree_width - 1 + i
        self.tree[seg_i] = a
        while seg_i != 0:
            seg_i = (seg_i - 1) // 2
            self.tree[seg_i] = max(self.tree[seg_i * 2 + 1], self.tree[seg_i * 2 + 2])

    def element(self, i):
        return self.tree[self.tree_width - 1 + i]

    # [l,r)の最大値
    def max(self, l, r, seg_i=0, segL=0, segR=-1):
        if segR == -1: segR = self.tree_width
        if r <= segL or segR <= l: return -self.inf
        if l <= segL and segR <= r: return self.tree[seg_i]
        segM = (segL + segR) // 2
        ret0 = self.max(l, r, seg_i * 2 + 1, segL, segM)
        ret1 = self.max(l, r, seg_i * 2 + 2, segM, segR)
        return max(ret0, ret1)

    # [l,r)でrから左を見たとき、初めにaを超える値のインデックス
    def OverL(self, l, r, a, u=0, ul=0, ur=-1):
        if ur == -1: ur = self.tree_width
        if r <= ul or ur <= l or self.tree[u]<=a: return -1
        if ur-ul==1:return ul
        um = (ul + ur) // 2
        ret = self.OverL(l, r, a, u * 2 + 2, um, ur)
        if ret != -1: return ret
        return self.OverL(l, r, a, u * 2 + 1, ul, um)

    # [l,r)でlから右を見たとき、初めにaを超える値のインデックス
    def OverR(self, l, r, a, u=0, ul=0, ur=-1):
        if ur == -1: ur = self.tree_width
        if r <= ul or ur <= l or self.tree[u] <= a: return self.n
        if ur - ul == 1: return ul
        um = (ul + ur) // 2
        ret = self.OverR(l, r, a, u * 2 + 1, ul,um)
        if ret != self.n: return ret
        return self.OverR(l, r, a, u * 2 + 2, um,ur)

mx=300005
n,k=MI()
st=SegtreeMax([0]*mx)
for _ in range(n):
    a=II()
    val=st.max(max(0,a-k),min(mx,a+k+1))
    st.update(a,val+1)
print(st.tree[0])
