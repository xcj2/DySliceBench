import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))


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


N,Q = MI()
A = LI()
BIT = BIT(A)
for _ in range(Q):
    p,q,r = MI()
    if p == 0:
        BIT.update(q+1,r)
    else:
        print(BIT.query(r)-BIT.query(q))
