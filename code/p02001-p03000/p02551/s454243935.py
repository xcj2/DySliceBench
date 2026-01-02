import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())


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

A,B = [0]*N,[0]*N
A[0],B[0] = N-2,N-2
A[N-1],B[N-1] = -(N-2),-(N-2)

I,J = BIT(A),BIT(B)
i_min,j_min = N,N
ans = (N-2)**2

for _ in range(Q):
    a,x = MI()
    if a == 1:
        ans -= I.query(x)
        if x < i_min:
            i_min = x
            y = J.tree[1]
            J.update(1,x-2-y)
            J.update(j_min,-(x-2-y))
    else:
        ans -= J.query(x)
        if x < j_min:
            j_min = x
            y = I.tree[1]
            I.update(1,x-2-y)
            I.update(i_min,-(x-2-y))

print(ans)
