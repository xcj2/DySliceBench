class segment_tree_dual:
    def __init__(self, N, compose, funcval, ID_M=None):
        self.compose = compose
        self.ID_M = ID_M
        self.funcval = funcval

        self.height = (N-1).bit_length() #木の段数
        self.N0 = 1<<self.height #木の横幅 >= N
        self.laz = [self.ID_M]*(2*self.N0) #作用素の木
        self.val = None #値の配列

    #初期値の配列を作る
    def build(self,initial):
        self.val = initial[:]

    #laz[k] を子に伝える、k が一番下の場合は laz[k] を val に反映する
    def propagate(self,k):
        if self.laz[k] == self.ID_M: return;
        if self.N0 <= k:
            self.val[k-self.N0] = self.funcval(self.val[k-self.N0], self.laz[k])
            self.laz[k] = self.ID_M
        else:
            self.laz[(k<<1)  ] = self.compose(self.laz[(k<<1)  ],self.laz[k]);
            self.laz[(k<<1)+1] = self.compose(self.laz[(k<<1)+1],self.laz[k]);
            self.laz[k] = self.ID_M;
    
    # 遅延をすべて解消する
    def propagate_all(self):
        upto = self.N0 + len(self.val)
        for i in range(1,upto): self.propagate(i)

    # laz[k]およびその上に位置する作用素をすべて伝播
    def thrust(self,k):
        for i in range(self.height,-1,-1): self.propagate(k>>i)

    # 区間[l,r]に関数 f を作用
    def update(self, L,R,f):
        L += self.N0; R += self.N0+1
        """まず伝播させる（オペレータが可換なら必要ない）"""
        #self.thrust(L)
        #self.thrust(R-1)
        #登りながら関数 f を合成
        while L < R:
            if R & 1:
                R -= 1
                self.laz[R] = self.compose(self.laz[R],f)
            if L & 1:
                self.laz[L] = self.compose(self.laz[L],f)
                L += 1
            L >>= 1; R >>= 1
    
    # values[k] を取得。
    def point_get(self, k):
        res = self.val[k]
        k += self.N0
        while k:
            if self.laz[k] != self.ID_M:
                res = self.funcval(res, self.laz[k])
            k //= 2
        return res
    
    # values[k] = x 代入する
    def point_set(self, k): 
        self.thrust(k+self.N0)
        self.val[k] = x

###########################################################################
# coding: utf-8
# Your code here!
import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
 
n,m = [int(i) for i in readline().split()]
s = input()[::-1]


compose = min
funcval = min
ID_M = INF = 10**18

seg = segment_tree_dual(n+1, compose, funcval, ID_M)
seg.build([0]+[INF]*(n))

for i in range(n):
    if s[i] == "1": seg.val[i] = -1
    else:
        v = seg.point_get(i)
        #print(v,i)
        seg.update(i+1,min(n,i+m),v+1)
        #print(seg.laz)

seg.propagate_all()
#print(s)
#print(seg.val)

val = seg.val
if val[-1] == -1 or val[-1] == INF:
    print(-1)
    exit()

ans = []

now = n
time = val[-1]
while now:
    n2 = now-1
    time -= 1
    while s[n2] == "1" or val[n2] != time:
        n2 -= 1
    ans.append(now-n2)
    now = n2
    
print(*ans)    
    
    
    










