import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
     

class SegmentTree():
    def __init__(self, arr):
        self.arr = arr
        self.size = self.calc_size(arr)
        self.n = (self.size+ 1) // 2 
        self.value = [2**31 - 1 for _ in range(self.size)]

    def calc_size(self, array):
        i = 1
        while i < len(array):
            i = i << 1
        return (i << 1) - 1

    def update(self, i, x):
        # 1 + 2 + ... + N/2 = N-1
        i += self.n - 1
        self.value[i] = x
        while i > 0:
            i = (i - 1)//2
            self.value[i] = min(self.value[2*i+1], self.value[2*i+2])

    def query(self, l, r):
        # find [l, r)
        def _query(l, r, node_i, node_l, node_r):
            # node_i: node = value[node_i]
            # node_l: node.leftChild is in charge of [node_l, m)
            # node_r: node.rightChild is in charge of [m, node_r)

            if node_r <= l or r <= node_l:
                return inf

            if l <= node_l and node_r <= r:
                return self.value[node_i]

            c1 = _query(l, r, 2 * node_i + 1, node_l, (node_l + node_r) // 2)
            c2 = _query(l, r, 2 * node_i + 2, (node_l + node_r) // 2, node_r)
            return min(c1, c2)

        return _query(l, r+1, 0, 0, self.n)

def main():
    n, q = LI()
    ans = []
    st = SegmentTree([2**31 - 1 for _ in range(n)])
    for _ in range(q):
        c, x, y = LI()
        if c == 0:
            st.update(x, y)
        if c == 1:
            ans.append(st.query(x, y))
    for a in ans:
        print(a)


main()


