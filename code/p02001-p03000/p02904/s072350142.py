from operator import add
import sys
input=sys.stdin.readline


class SegTree():
    def __init__(self, N, e, operator_func=add):
        self.e = e # 単位元
        self.size = N
        self.node = [self.e] * (2*N)
        self.operator_func = operator_func # 処理(add or xor max minなど)

    def set_list(self, l):
        for i in range(self.size):
            self.node[i+self.size-1] = l[i]
        for i in range(self.size-1)[::-1]:
            self.node[i] = self.operator_func(self.node[2*i+1], self.node[2*i+2])
    
    def update(self, k, x):
        k += self.size-1
        self.node[k] = x
        while k >= 0:
            k = (k - 1) // 2
            self.node[k] = self.operator_func(self.node[2*k+1], self.node[2*k+2])

    def get(self, l, r):
        # [l, r) についてqueryを求める
        x = self.e
        l += self.size
        r += self.size

        while l<r:
            if l&1:
                x = self.operator_func(x, self.node[l-1])
                l += 1
            if r&1:
                r -= 1
                x = self.operator_func(x, self.node[r-1])
            l >>= 1
            r >>= 1
        return x


N, K = map(int, input().split())
P = list(map(int, input().split()))
tree = SegTree(N, 10**12, min)
tree_min = SegTree(N, 10**12, min)
tree_max = SegTree(N, -10**12, max)
tree_min.set_list(P)
tree_max.set_list(P)

for i in range(N):
    tree.update(i, P[i]-P[i-1] if i else P[i])

f = lambda l,r:tree.get(l+1, r)>=0

ans = N-K+1
isOrig = 0
for i in range(N-K):
    if f(i, i+K):
        ans -= 1
        isOrig = 1
    elif tree_min.get(i, i+1+K)==P[i] and tree_max.get(i, i+1+K)==P[i+K]:
        ans -= 1
if f(N-K, N):
    ans -= 1
    isOrig = 1
ans += isOrig
print(ans)