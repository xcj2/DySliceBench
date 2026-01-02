import sys
input = sys.stdin.readline

n,d,a = map(int,input().split())
xh = [list(map(int,input().split())) for _ in range(n)]

xh.sort()

class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0]*(n+1)
        self.depth = n.bit_length()

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
        if not (0 <= i <= self.size): raise ValueError("error!")
        s = 0
        while i>0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        if not (0 <= i < self.size): raise ValueError("error!")
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def lower_bound(self, x):
        """ 累積和がx以上になる最小のindexと、その直前までの累積和 """
        sum_ = 0
        pos = 0
        for i in range(self.depth, -1, -1):
            k = pos + (1 << i)
            if k <= self.size and sum_ + self.tree[k] < x:
                sum_ += self.tree[k]
                pos += 1 << i
        return pos + 1, sum_

    def __getitem__(self, key):
        if not (0 <= key < self.size): raise IndexError("error!")
        return self.sum(key+1) - self.sum(key)

    def __setitem__(self, key, value):
        # 足し算と引き算にはaddを使うべき
        if not (0 <= key < self.size): raise IndexError("error!")
        self.add(key, value - self[key])

class BitImos:
    """
    ・範囲すべての要素に加算
    ・ひとつの値を取得
    の2種類のクエリをO(logn)で処理
    """
    def __init__(self, n):
        self.bit = Bit(n+1)

    def add(self, s, t, x):
        # [s, t)にxを加算
        self.bit.add(s, x)
        self.bit.add(t, -x)

    def get(self, i):
        return self[i]

    def __getitem__(self, key):
        # 位置iの値を取得
        return self.bit.sum(key+1)

bit = BitImos(n)
ans = 0
att = [0]*n
cnt = 0

for i in range(n):
    tmp = xh[i][0] + 2 * d
    while cnt < n:
        if xh[cnt][0] <= tmp:
            cnt += 1
        else:
            break
    att[i] = min(cnt-1, n-1)

for i,xh1 in enumerate(xh):
    x,h = xh1
    if bit.get(i) < h:
        at = -(-(h - bit.get(i)) // a)
        ans += at
        bit.add(i, att[i]+1, at*a)

print(ans)
