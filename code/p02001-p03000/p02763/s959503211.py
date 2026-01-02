import sys
import math
from collections import defaultdict

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

#Binary Indexed Tree（１点加算）
#1-indexed
class BIT:
    """
    a[1]~a[n]の数列を想定
    """

    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def add(self, index, x):
        """
        a[index]にxを加算
        """
        while index <= self.size:
            self.tree[index] += x
            index += index & (-index)
 
    def sum(self, index):
        """
        a[1]~a[index]の和
        """
        s = 0
        while index:
            s += self.tree[index]
            index -= index & (-index)
        return s
 
    def search(self, value):
        """
        sum(index) >= value を満たす最小のindex
        sum(n) < value のとき n+1 を返す
        """
        i = 0
        s = 0
        step = 1 << (self.size.bit_length() - 1)
        while step:
            if i + step <= self.size and s + self.tree[i + step] < value:
                i += step
                s += self.tree[i]
            step >>= 1
        return i + 1

N = I()
S = list(str(input()))
Q = I()

def calc(c):
    return ord(c)-ord('a')

bit = [BIT(N) for _ in range(26)]
for i in range(N):
    bit[calc(S[i])].add(i+1,1)

for i in range(Q):
    now = list(input().split())
    if now[0]=='1':
        iq = int(now[1])
        cq = str(now[2])
        bit[calc(S[iq-1])].add(iq,-1)
        bit[calc(cq)].add(iq,1)
        S[iq-1] = cq
    else:
        lq = int(now[1])
        rq = int(now[2])
        ans = 0
        for j in range(26):
            if lq == 1:
                if bit[j].sum(rq) >= 1:
                    ans += 1
            else:
                if bit[j].sum(rq) != bit[j].sum(lq-1):
                    ans += 1
        print(ans)