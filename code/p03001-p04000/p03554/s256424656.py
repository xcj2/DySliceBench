import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(readline())
B = list(map(int,readline().split()))
Q = int(readline())
m = map(int,read().split())
LR = sorted(zip(m,m))

class MaxSegTree():
    def __init__(self,N):
        self.Nelem = N
        self.size = 1<<(N.bit_length()) # 葉の要素数
        self.data = [0] * (2*self.size)
        
    def build(self,raw_data):
        # raw_data は 0-indexed
        for i,x in enumerate(raw_data):
            self.data[self.size+i] = x
        for i in range(self.size-1,0,-1):
            x = self.data[i+i]; y = self.data[i+i+1]
            self.data[i] = x if x>y else y
    
    def update(self,i,x):
        i += self.size
        self.data[i] = x
        i >>= 1
        while i:
            x = self.data[i+i]; y = self.data[i+i+1]
            self.data[i] = x if x>y else y
            i >>= 1
    
    def get_data(self,i):
        return self.data[i+self.size]

    def get_max(self,L,R):
        # [L,R] に対する値を返す
        L += self.size
        R += self.size + 1
        # [L,R) に変更
        x = 0
        while L < R:
            if L&1:
                y = self.data[L]
                if x < y: x = y
                L += 1
                
            if R&1:
                R -= 1
                y = self.data[R]
                if x < y: x = y
            L >>= 1; R >>= 1
        return x

"""
・ある場所まで確定して、そこから先を全て1で埋めた場合
・ある場所まで確定して、そこから先を全て0で埋めた場合
の加算スコア
"""
add0 = [0] * (N+1)
add1 = [0] * (N+1)
x = sum(B)
add1[0] = x
add0[0] = N-x
for i,x in enumerate(B,1):
    if x == 0:
        add0[i]=add0[i-1]-1; add1[i] = add1[i-1]
    else:
        add1[i]=add1[i-1]-1; add0[i] = add0[i-1]

"""
ある場所を右端としてとった時点での
・残りをすべて0で埋めたときのスコア
・残りをすべて1で埋めたときのスコア
dp0, dp1 をseg木で管理
"""

dp0 = MaxSegTree(N+1)
dp0.build([add0[0]] + [0] * N)
dp1 = MaxSegTree(N+1)
dp1.build([add1[0]] + [0] * N)

for L,R in LR:
    # dp1[R] を計算したい。[L,inf) が1で埋まったときのスコア
    x = dp1.get_data(R)
    y = dp0.get_max(0,L-1) + add1[L-1] - add0[L-1] # 0埋め部分を1埋めに修正してdp1[R]に遷移
    z = dp1.get_max(L,R-1) # そのままdp1[R]に遷移
    if y < z: y = z
    if x < y:
        dp1.update(R,y)
        dp0.update(R,y - add1[R] + add0[R])

# 一致を数えていたので、距離に修正
answer = N - dp0.data[1]
print(answer)