import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from operator import itemgetter

n = int(readline())
ppp = list(map(int,readline().split()))

class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
        self.depth = n.bit_length()
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
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
        return pos + 1

q = sorted(enumerate(ppp,1),key=itemgetter(1),reverse=True)
bit = Bit(n+4)
bit.add(1,1)
bit.add(2,1)
bit.add(n+3,1)
bit.add(n+4,1)

ans = 0
for i, p in q:
  f = bit.sum(i+2)
  LL = max(2,bit.lower_bound(f-1))
  LR = bit.lower_bound(f)
  RL = bit.lower_bound(f+1)
  RR = min(n+3,bit.lower_bound(f+2))
  ans += p*((i+2-LR)*(RR-RL)+(LR-LL)*(RL-i-2))
  bit.add(i+2,1)
  
print(ans)