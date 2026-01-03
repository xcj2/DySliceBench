import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())

N,K = MI()
A = [0]  # 累積和
for i in range(N):
    A.append(A[-1]+I()-K)

# Ai<=Aj たる i<j の個数を数え上げる

B = sorted(list(set(A)))
d = {}
for i in range(len(B)):
    d[B[i]] = i+1

for i in range(N+1):
    A[i] = d[A[i]]

# Aを大小関係を保ち座標圧縮


class BIT():
    def __init__(self,init_value):
        self.n = len(init_value)
        self.tree = [0]*(self.n+1)
        for i in range(1,self.n+1):
            x = init_value[i-1]
            while i <= self.n:
                self.tree[i] += x
                i += i & (-i)
    def update(self,i,x):  # i(1-index)番目の値を+x
        while i <= self.n:
            self.tree[i] += x
            i += i & (-i)
        return
    def query(self,i):  # 1番目からi(1-index)番目までの和を返す
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & (-i)
        return res


BIT = BIT([0]*(N+1))
ans = 0
for i in range(N+1):
    ans += BIT.query(A[i])
    BIT.update(A[i],1)
print(ans)
