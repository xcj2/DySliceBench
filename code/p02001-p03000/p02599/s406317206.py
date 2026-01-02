import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

class BIT:
    """
    a[1]~a[n]の数列を想定
    """

    def __init__(self,n):
        self.size = n
        self.tree = [0]*(n+1)
 
    def add(self,index,x):
        """
        a[index]にxを加算
        """
        while index <= self.size:
            self.tree[index] += x
            index += index & (-index)
 
    def sum(self,index):
        """
        a[1]~a[index]の和
        """
        s = 0
        while index:
            s += self.tree[index]
            index -= index & (-index)
        return s
 
    def search(self,value):
        """
        sum(index) >= value を満たす最小のindex
        sum(n) < value のとき n+1 を返す
        """
        i = 0
        s = 0
        step = 1 << (self.size.bit_length() - 1)
        while step:
            if i+step <= self.size and s + self.tree[i+step] < value:
                i += step
                s += self.tree[i]
            step >>= 1
        return i + 1

N,Q = LI()
c = LI()
l,r = LIR(Q,2)

x = []
for i in range(Q):
    x.append((i,l[i],r[i]))
x.sort(key=lambda x: x[2])

bit = BIT(N)

ans = [0]*Q
last = [-1]*(N+1)
right = -1 # 確認し終わった右端
for i in range(Q):
    for j in range(right+1,x[i][2]):
        bit.add(j+1,1)
        if last[c[j]] != -1:
            bit.add(last[c[j]]+1,-1)
        last[c[j]] = j
    right = x[i][2]-1
    ans[x[i][0]] = bit.sum(x[i][2]) -  bit.sum(x[i][1]-1)

for a in ans:
    print(a)