def examA():
    N = I()
    ans = 0
    print(ans)
    return

def examB():
    ans = 0
    print(ans)
    return

def examC():
    ans = 0
    print(ans)
    return

def examD():
    ans = 0
    print(ans)
    return

def examE():
    ans = 0
    print(ans)
    return

def examF():
    # 0は絶対に入れない!!
    class Bit():
        def __init__(self, n):
            self.size = n
            self.tree = [0] * (n + 1)
            return

        def sum(self, i):
            i += 1
            s = 0
            while i > 0:
                s += self.tree[i]
                i -= i & -i
            return s

        def add(self, i, x=1):
            # i==0 はだめ => 全部+1するとか
            i += 1
            while i <= self.size:
                self.tree[i] += x
                i += i & -i
            return

        def search(self, x):
            # 二分探索。和がx以上となる最小のインデックス(>= 1)を返す
            # maspyさんの参考　よくわかってない
            i = 0
            s = 0
            step = 1 << ((self.size).bit_length() - 1)
            while step:
                if i + step <= self.size and s + self.tree[i + step] < x:
                    i += step
                    s += self.tree[i]
                step >>= 1
            return i

        def debug(self, k):
            return [self.sum(i) for i in range(k)]
    def compress(list1):
        list2 = sorted(set(list1))
        memo = {value: index for index, value in enumerate(list2)}
        for i in range(len(list1)):
            list1[i] = memo[list1[i]]
        return memo, len(list2)
    n = I()
    Q = [LI()for _ in range(n)]
    A = []
    for q in Q:
        if q[0]==2:
            continue
        a, b = q[1:]
        A.append(a)
    memo,N = compress(A)
    #print(memo)
    #print(N)
    bit = Bit(N+1)
    bit_a = Bit(N+1)
    location = defaultdict(int)
    num = 0
    B = 0
    ans = []
    for q in Q:
        if q[0]==2:
            x = bit.search((num+1)//2)
            #print(x,bit_a.sum(x),location[x])
            l = location[x]
            rep = l*bit.sum(x)-bit_a.sum(x)+B
            rep += bit_a.sum(N) - bit_a.sum(x) - l*(bit.sum(N) - bit.sum(x))
            ans.append((location[x],rep))
            continue
        a, b = q[1:]
        B += b
        bit.add(memo[a])
        bit_a.add(memo[a],a)
        location[memo[a]] = a
        num += 1

    for v in ans:
        print(" ".join(map(str,v)))
    return

def test():
    i = I()
    li = LI()
    lsi = LSI()
    si = LS()
    print(i)
    print(li)
    print(lsi)
    print(si)
    return

import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(readline())
def LI(): return list(map(int,readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examF()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""