

class SegTree:  # モノイドに対して適用可能、Nが2冪でなくても良い
    def __init__(self,N,seg_func,unit):
        self.N = 1 << (N-1).bit_length()
        self.func = seg_func
        self.unit = unit
        self.tree = [self.unit]*(2*self.N)

    def build(self,init_value):  # 初期値を[N,2N)に格納
        for i in range(len(init_value)):
            self.tree[i+self.N] = init_value[i]
        for i in range(self.N-1,0,-1):
            self.tree[i] = self.func(self.tree[i << 1],self.tree[i << 1 | 1])

    def set_val(self,i,x):  # i番目(0-index)の値をxに変更
        i += self.N
        self.tree[i] = x
        i >>= 1
        while i:
            self.tree[i] = self.func(self.tree[i << 1],self.tree[i << 1 | 1])
            i >>= 1

    def fold(self,L,R):  # [L,R)の区間取得
        L += self.N
        R += self.N
        vL = self.unit
        vR = self.unit
        while L < R:
            if L & 1:
                vL = self.func(vL,self.tree[L])
                L += 1
            if R & 1:
                R -= 1
                vR = self.func(self.tree[R],vR)
            L >>= 1
            R >>= 1
        return self.func(vL,vR)


import sys
sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())


N,K = MI()
ST = SegTree(300001,max,0)

# dp[i][j] = A1~Ai を用いて、末尾が j になり条件を満たす数列の長さの最大値
# dp[i][j] = 1+max(dp[i-1][Ai-K],…,dp[i-1][Ai+K]) if j == Ai else dp[i-1][j]
# この dp をセグメントツリーにのせて考える

for i in range(N):
    a = I()
    ST.set_val(a,1+ST.fold(max(0,a-K),min(300000,a+K)+1))

print(ST.fold(0,300001))
