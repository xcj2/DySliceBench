from operator import itemgetter
import sys
input = sys.stdin.readline

# 二部探索木の代わり
# max_Xが大きい場合、0を含む場合は座標圧縮する

class BITbisect():
    def __init__(self, max_X):
        self.max_X = max_X + 1
        self.bit = [0]*(self.max_X+1)

    # x番目にaを加える
    def add(self, x, a):
        while x <= self.max_X:
            self.bit[x] += a
            x += x & -x

    def insert(self, x):
        self.add(x, 1)

    def delete(self, x):
        self.add(x, -1)

    # xまでに出現している個数
    def query_sum(self, x):
        s = 0
        while x > 0:
            s += self.bit[x]
            x -= x & -x
        return s

    def exist(self, x):
        if self.query_sum(x) - self.query_sum(x-1) > 0:
            return True
        return False
    
    def count(self, x):
        return self.query_sum(x) - self.query_sum(x-1)

    # xより大きくてbitに入ってるもののうち最小のもの
    # O((logN)^2)
    def upper(self, x):
        qx = self.query_sum(x) + 1
        if qx > self.query_sum(self.max_X):
            return False
        l = 0
        r = self.max_X
        while l < r:
            m = (l+r)//2
            if self.query_sum(m) < qx:
                if l == m:
                    return r
                l = m
            else:
                r = m
        if m == self.max_X:
            return False
        return m

    # x以下でbitに入っているもののうち最大のもの
    # O((logN)^2)
    def lower(self, x):
        qx = self.query_sum(x)
        if qx == 0:
            return False
        l = 0
        r = self.max_X
        while l < r:
            m = (l+r)//2
            if self.query_sum(m) < qx:
                if l == m:
                    return r
                l = m
            else:
                r = m
        return m

    # listみたいに表示
    def display(self):
        print('inside BIT:', end=' ')
        for x in range(1, self.max_X):
            if bit.exist(x):
                c = bit.count(x)
                for _ in range(c):
                    print(x, end=' ')
        print()


N = int(input())
A = list(map(int, input().split()))

B = []
for i, a in enumerate(A):
    B.append((i+1, a))
B.sort(key=itemgetter(1))

bit = BITbisect(N)

ans = 0
for i, a in B:
    l = bit.lower(i)
    r = bit.upper(i)
    if l is False:
        l = 0
    if r is False:
        r = N+1
    ans += (i-l)*(r-i)*a
    bit.insert(i)
print(ans)