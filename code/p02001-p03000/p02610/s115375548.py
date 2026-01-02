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

class OrderedSet:
    def __init__(self,n):
        self.c = {}
        self.r = {}
        #self.a_sort = sorted(list(set(a)))
        self.a_sort = list(range(n))
        for i,a in enumerate(self.a_sort):
            self.c[a] = i+1
            self.r[i+1] = a
        self.size = len(self.c)
        self.tree = [0]*(self.size + 1)
        self.num = [0]*self.size
        self.all_count = 0  # 全要素数

    # BITのsum関数
    def _sum(self,index):
        s = 0
        while index:
            s += self.tree[index]
            index -= index & (-index)
        return s

    # xをk個挿入する
    def insert(self,x,k=1):
        index = self.c[x]
        self.num[index-1] += k
        while index <= self.size:
            self.tree[index] += k
            index += index & (-index)
        self.all_count += k
    
    # xをk個削除する
    def erase(self,x,k=1):
        self.insert(x,k=-k)

    # 格納しているxの数を返す
    def count(self,x):
        return self.num[self.c[x]-1]

    # 下から数えてk番目の要素を返す（要素がk個未満のときNoneを返す）
    def get_kth_bottom(self,k):
        if k <= 0:
            return None
        elif self.all_count < k:
            return None
        else:
            i = 0
            s = 0
            step = 1 << (self.size.bit_length() - 1)
            while step:
                if i+step <= self.size and s+self.tree[i+step] < k:
                    i += step
                    s += self.tree[i]
                step >>= 1
            return self.r[i+1]
    
    # 上から数えてk番目の要素を返す（要素がk個未満のときNoneを返す）
    def get_kth_top(self,k):
        return self.get_kth_bottom(self.all_count-k+1)
    
    # x以上の最小要素を返す
    def lower_bound(self,x):
        if x in self.c.keys():
            p = self.c[x]-1
        else:
            p = bisect_left(self.a_sort,x)
        if p == 0:
            k = 1
        else:
            k = self._sum(p) + 1
        return self.get_kth_bottom(k)
    
    # x以下の最大要素を返す
    def upper_bound(self,x):
        if x in self.c.keys():
            p = self.c[x]
        else:
            p = bisect_right(self.a_sort,x)
        if p == 0:
            return None
        else:
            k = self._sum(p)
            return self.get_kth_bottom(k)

T = I()

ans = []
for _ in range(T):
    N = I()
    K,L,R = LIR(N,3)
    
    left = []    # 左側に入れたい要素
    right = []   # 右側に入れたい要素
    for i in range(N):
        large = max(L[i],R[i])
        small = min(L[i],R[i])
        gap = large-small
        if L[i] >= R[i]:
            left.append((gap,K[i]-1,large,small))
        else:
            right.append((gap,K[i],large,small))

    left.sort(key=lambda x:x[0], reverse=True)
    right.sort(key=lambda x:x[0], reverse=True)

    ordset = OrderedSet(N)
    ans_t = 0

    # まだ空いている場所をordsetに入れておく
    for i in range(N):
        ordset.insert(i)

    for i in range(len(left)):
        p = ordset.upper_bound(left[i][1])
        if p is None:
            p2 = ordset.upper_bound(len(left)-1)
            ordset.erase(p2)
            ans_t += left[i][3]
        elif p >= len(left):
            p2 = ordset.upper_bound(len(left)-1)
            ordset.erase(p2)
            ans_t += left[i][2]            
        else:
            ordset.erase(p)
            ans_t += left[i][2]

    for i in range(len(right)):
        p = ordset.lower_bound(right[i][1])
        if p is None:
            p2 = ordset.lower_bound(len(left))
            ordset.erase(p2)
            ans_t += right[i][3]
        else:
            ordset.erase(p)
            ans_t += right[i][2]
    
    ans.append(ans_t)

for ans_t in ans:
    print(ans_t)