import sys
from itertools import accumulate
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


class BIT:
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


N = I()
A = LI()


def f(x):  # A[l:r+1] の中央値が x 以上になる (l,r) の個数が、全体の半分以上あるか
    B = [0] + [1 if A[i] >= x else -1 for i in range(N)]
    B = list(accumulate(B))
    B = [b+N+1 for b in B]  # 全て正になるように補正
    # Bi <= Bj たる (i,j) の個数を数える
    bit = BIT([0]*(2*N+2))
    count = 0
    for i in range(N+1):
        b = B[i]
        count += bit.query(b)
        bit.update(b,1)
    if count >= (N*(N+1)+3)//4:
        return True
    return False


ok = 1
ng = 10**9+1
while ok+1 < ng:
    mid = (ok+ng)//2
    if f(mid):
        ok = mid
    else:
        ng = mid

print(ok)
