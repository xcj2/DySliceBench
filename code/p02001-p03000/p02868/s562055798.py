import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N,M = map(int,readline().split())
m = map(int,read().split())
LRC = zip(m,m,m)

R_to_L = [[] for _ in range(N+1)]
R_to_C = [[] for _ in range(N+1)]

for l,r,c in LRC:
    R_to_L[r].append(l)
    R_to_C[r].append(c)

INF = 10**18

class MinSegTree():
    def __init__(self,N):
        self.Nelem = N
        self.size = 1<<(N.bit_length()) # 葉の要素数
        
    def build(self,raw_data):
        # raw_data は 0-indexed
        INF = 10**18
        self.data = [INF] * (2*self.size)
        for i,x in enumerate(raw_data):
            self.data[self.size+i] = x
        for i in range(self.size-1,0,-1):
            x = self.data[i+i]; y = self.data[i+i+1]
            self.data[i] = x if x<y else y
    
    def update(self,i,x):
        i += self.size
        self.data[i] = x
        i >>= 1
        while i:
            x = self.data[i+i]; y = self.data[i+i+1]
            self.data[i] = x if x<y else y
            i >>= 1
    
    def get_value(self,L,R):
        # [L,R] に対する値を返す
        L += self.size
        R += self.size + 1
        # [L,R) に変更
        x = 10**18
        while L < R:
            if L&1:
                y = self.data[L]
                if x > y: x = y
                L += 1
                
            if R&1:
                R -= 1
                y = self.data[R]
                if x > y: x = y
            L >>= 1; R >>= 1
        return x

dp = MinSegTree(N+1)
dp.build([INF]  * (N+1))

dp.update(1,0)

for r in range(2,N+1):
    x = INF
    for l,c in zip(R_to_L[r], R_to_C[r]):
        y = dp.get_value(l,r-1) + c
        if x>y:
            x=y
    dp.update(r,x)
    if r == N:
        answer = x

if answer == INF:
    answer = -1
print(answer)
