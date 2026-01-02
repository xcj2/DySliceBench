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

from bisect import bisect_left, bisect_right
from operator import itemgetter
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
STX = [list(map(int, input().split())) for _ in range(N)]
D = [int(input()) for _ in range(Q)]

bit = BITbisect(Q+1)

for i, d in enumerate(D):
    bit.insert(i+1)

STX.sort(key=itemgetter(2))

ans = [-1]*Q
for s, t, x in STX:
    #print(s, t, x)
    #bit.display()
    il = bisect_left(D, s-x)
    ir = bisect_right(D, t-x-1)
    #print(il, ir)
    ind_l = bit.bisect_right(il)
    ind_r = bit.bisect_right(ir)
    #print(ind_l, ind_r)
    for ind in range(ind_l, ind_r):
        il = bit.search(ind_l)
        bit.delete(il)
        ans[il-1] = x


for a in ans:
    print(a)