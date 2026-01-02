# instead of AVLTree
class BITbisect():
    def __init__(self, max):
        self.max = max
        self.data = [0]*(self.max+1)
    
    # 0からiまでの区間和
    # 立っているビットを下から処理
    def query_sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    # i番目の要素にxを足す
    # 覆ってる区間すべてに足す
    def add(self, i, x):
        while i <= self.max:
            self.data[i] += x
            i += i & -i

    def insert(self, x):
        self.add(x, 1)

    def delete(self, x):
        self.add(x, -1)

    def count(self, x):
        return self.query_sum(x) - self.query_sum(x-1)
    
    def length(self):
        return self.query_sum(self.max)
    
    # 下からc番目(0-indexed)の数
    # O(log(N))
    def search(self, c):
        c += 1
        s = 0
        ind = 0
        l = self.max.bit_length()
        for i in reversed(range(l)):
            if ind + (1<<i) <= self.max:
                if s + self.data[ind+(1<<i)] < c:
                    s += self.data[ind+(1<<i)]
                    ind += (1<<i)
        if ind == self.max:
            return False
        return ind + 1
    
    def bisect_right(self, x):
        return self.query_sum(x)

    def bisect_left(self, x):
        if x == 1:
            return 0
        return self.query_sum(x-1)

    # listみたいに表示
    def display(self):
        print('inside BIT:', end=' ')
        for x in range(1, self.max+1):
            if self.count(x):
                c = self.count(x)
                for _ in range(c):
                    print(x, end=' ')
        print()

import sys
input = sys.stdin.readline
from operator import itemgetter

INF = 10**15

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(N):
    if i%2 == 1:
        a = A[i]
        A[i] = B[i]
        B[i] = a

INDs = []
def dfs(p,L):
    if p == N:
        if len(L) == (N+1)//2:
            INDs.append(L)
        return
    dfs(p+1, L+[p])
    dfs(p+1, L)
    return

dfs(0, [])

ans = INF
for IND in INDs:
    As = []
    Bs = []
    usingA = [False]*N
    for ind in IND:
        usingA[ind] = True
    for ind in range(N):
        if usingA[ind]:
            As.append((A[ind], ind))
        else:
            Bs.append((B[ind], ind))
    As.sort()
    Bs.sort()
    ok = True
    pre = -INF
    Array = [None]*N
    for i in range(N):
        if i%2 == 0:
            if As[i//2][0] < pre:
                ok = False
                break
            Array[As[i//2][1]] = i+1
            pre = As[i//2][0]
        else:
            if Bs[i//2][0] < pre:
                ok = False
                break
            Array[Bs[i//2][1]] = i+1
            pre = Bs[i//2][0]
    if not ok:
        continue
    
    bit = BITbisect(N)
    nowans = 0
    for j, a in enumerate(Array):
        nowans += j - bit.query_sum(a)
        bit.add(a, 1)
    
    if nowans < ans:
        ans = nowans

if ans == INF:
    print(-1)
else:
    print(ans)

