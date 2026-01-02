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

N = I()
A = LI()

sumA = sum(A)

bit = BIT(N)
for i in range(N):
    bit.add(i+1,A[i])

ans = float('inf')

# 2本目の区切りを i/i+1 の境目とする
# 左右2つの区間は，それぞれ差が最小になるように区切ると最適
for i in range(1,N-2):
    l_sum = bit.sum(i+1)
    r_sum = sumA-l_sum
    p = bit.search(l_sum+r_sum/2)
    if p == i+2:
        r_max = bit.sum(p)-bit.sum(i+1)
        r_min = r_sum-r_max
    elif p == N:
        r_min = bit.sum(p-1)-bit.sum(i+1)
        r_max = r_sum-r_min
    else:
        max1 = bit.sum(p)-bit.sum(i+1)
        min1 = r_sum-max1
        max2 = min1+A[p-1]
        min2 = max1-A[p-1]
        if max1-min1 < max2-min2:
            r_max = max1
            r_min = min1
        else:
            r_max = max2
            r_min = min2

    p = bit.search(l_sum/2)
    if p == 1:
        l_max = bit.sum(p)
        l_min = l_sum-l_max
    elif p == i+1:
        l_min = bit.sum(p-1)
        l_max = l_sum-l_min
    else:
        max1 = bit.sum(p)
        min1 = l_sum-max1
        max2 = min1+A[p-1]
        min2 = max1-A[p-1]
        if max1-min1 < max2-min2:
            l_max = max1
            l_min = min1
        else:
            l_max = max2
            l_min = min2

    now = max(l_max,r_max) - min(l_min,r_min)
    if now < ans:
        ans = now

print(ans)