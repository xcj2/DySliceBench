import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353

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

# 座圧（val→key）
def compress(A):
    sorted_A = sorted(set(A))
    Adict = {val:key for key,val in enumerate(sorted_A)}
    return Adict,len(sorted_A),sorted_A

# Binary Indexed Tree（１点加算）
## 1-indexed
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

Q = I()
query = []
for _ in range(Q):
    query.append(list(map(int,(input().split()))))

values = []
for i in range(Q):
    if query[i][0] == 1:
        values.append(query[i][1])

comp,n,values = compress(values)

# 位置の管理用
bit1 = BIT(n)

# 和の管理用
bit2 = BIT(n)

cumb = 0
num = 0
for i in range(Q):
    if query[i][0] == 1:
        cumb += query[i][2]
        val = query[i][1]
        num += 1
        p = comp[val]
        bit1.add(p+1,1)
        bit2.add(p+1,val)
    else:
        med = bit1.search((num+1)//2)
        sum_ = (bit2.sum(n)-bit2.sum(med)) - bit2.sum(med-1)
        minus_num = (bit1.sum(n)-bit1.sum(med)) - bit1.sum(med-1)
        print(values[med-1],sum_+cumb-minus_num*values[med-1])