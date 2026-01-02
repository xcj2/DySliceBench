import sys
from collections import deque
from collections import defaultdict
import math
sys.setrecursionlimit(20000000)
input = sys.stdin.readline
q = int(input())
tei = 0
x = []
nnn = []
import bisect
def press(a):
    n = len(a)
    b = set(a)
    b = list(b)
    b.sort()
    c = [0] * n
    for i in range(n):
        c[i] = bisect.bisect_left(b,a[i])
    return b,c
for i in range(q):
        nnn.append(input().rstrip())
for i in range(q):
        nn = nnn[i]
        if int(nn[0]) == 1:
                _,a,b = map(int,nn.split())
                x.append(a)
x.sort()
mo,za = press(x)
mo = x
d = dict()
for i in range(len(x)):
        d[mo[i]] = za[i]+1
dg = dict()
for i in range(len(x)):
        dg[za[i]+1] = mo[i]
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
bit1 = BIT(len(x))
bit2 = BIT(len(x))
now = -1
def cheak(x,y):
  o = bit2.sum(x)
  if y >= o:
    return 0
  else:
    return 1
for i in range(q):
        nn = nnn[i]
        if int(nn[0]) == 1:
                _,a,b = map(int,nn.split())
                tei += b
                bit1.add(d[a],a)
                bit2.add(d[a],1)
                now += 1
        else:
                dai = len(x)
                syo = 1
                while True:
                        if dai-syo <= 1:
                                if cheak(syo,now//2) == 1:
                                        dai = syo
                                break
                        kon = (dai+syo)//2
                        c = cheak(kon,now//2)
                        if c == 1:
                                dai = kon
                        else:
                                syo = kon
                ans = 0
                ans -= bit1.sum(dai) - dg[dai]*bit2.sum(dai)
                ans += bit1.sum(len(x)) -bit1.sum(dai) -((bit2.sum(len(x))-bit2.sum(dai))*dg[dai])
                print(dg[dai],tei+ans)