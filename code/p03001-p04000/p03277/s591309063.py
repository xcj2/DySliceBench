import sys
class BIT:
    def __init__(self, node_size):
        self._node = node_size+1
        self.bit = [0]*self._node

    def add(self, index, add_val):
        while index < self._node:
            self.bit[index] += add_val
            index += index & -index

    def sum(self, index):
        res = 0
        while index > 0:
            res += self.bit[index]
            index -= index & -index
        return res
def cheak(x):
  c = [0] * n
  for i in range(n):
    if a[i] >= x:
      c[i] = 1
    else:
      c[i] = -1
  ru = [0] * (n+1)
  for i in range(1,n+1):
    ru[i] = c[i-1] + ru[i-1]
  ans = 0
  bit = BIT(n+2)
  MIN = min(ru)
  for i in range(len(ru)):
    ans += i - bit.sum(ru[i]-MIN+1)
    bit.add(ru[i]-MIN+1, 1)
  if ans <= n*(n+1)//4:
    return 1
  else:
    return 0
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
b = sorted(a)
dai = n-1
syo = 0
while True:
  if dai-syo <= 1:
    break
  kon = b[(dai+syo)//2]
  d = cheak(kon)
  if d == 1:
    syo = (dai+syo)//2
  else:
    dai = (dai+syo)//2
if cheak(b[dai]) == 1:
  print(b[dai])
else:
  print(b[syo])