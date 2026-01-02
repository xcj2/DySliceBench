class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0]*(n+1)

    def __iter__(self):
        psum = 0
        for i in range(self.size):
            csum = self.sum(i+1)
            yield csum - psum
            psum = csum
        raise StopIteration()

    def __str__(self):  # O(nlogn)
        return str(list(self))

    def sum(self, i):
        # [0, i) の要素の総和を返す
        s = 0
        while i>0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def __getitem__(self, key):
        return self.sum(key+1) - self.sum(key)

    def __setitem__(self, key, value):
        # 足し算と引き算にはaddを使うべき
        self.add(key, value - self[key])

mod = 10**9+7
N, K = map(int, input().split())
A = list(map(int, input().split()))
bit = Bit(max(A)+1)
ans = 0
for i, a in enumerate(A):
    ans += i - bit.sum(a+1)
    bit.add(a, 1)
ans *= K
from itertools import combinations
cnt = 0
for a, b in combinations(A, 2):
    if a!=b:
        cnt += 1
cnt *= K*(K-1)//2
ans += cnt
print(ans%mod)
