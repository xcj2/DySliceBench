import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)
import bisect

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

class segtree:

    def __init__(self, n,operator,identity):
        nb = bin(n)[2:]
        bc = sum([int(digit) for digit in nb])
        if bc == 1:
            self.num_end_leaves = 2**(len(nb)-1)
        else:
            self.num_end_leaves = 2**(len(nb))

        self.array = [identity for i in range(self.num_end_leaves * 2)]
        self.identity = identity
        self.operator =operator

    def update(self,x,val):
        actual_x = x+self.num_end_leaves
        self.array[actual_x] = val
        while actual_x > 0 :
            actual_x = actual_x//2
            self.array[actual_x] = self.operator(self.array[actual_x*2],self.array[actual_x*2+1])

    def get(self,q_left,q_right,arr_ind=1,leaf_left=0,depth=0):
        width_of_floor = self.num_end_leaves//(2**depth)
        leaf_right = leaf_left+width_of_floor-1

        if leaf_left > q_right or leaf_right < q_left:
            return  self.identity

        elif leaf_left >= q_left and leaf_right <= q_right:
            return self.array[arr_ind]

        else:
            val_l = self.get(q_left,q_right,2*arr_ind,leaf_left,depth+1)
            val_r = self.get(q_left,q_right,2*arr_ind+1,leaf_left+width_of_floor//2,depth+1)
            return self.operator(val_l,val_r)

n = int(input())
s = [ c for c in input()]
q = int(input())
qqq = list(map(lambda s: s.strip().split(), sys.stdin.readlines()))

seg = segtree(n+1, lambda a,b:a|b, 0)

for i,c in enumerate(s):
    o = ord(c) - ord("a")
    seg.update(i, 2**o)
# log(chars)

for que in qqq:
    if que[0] == "1":
        target = int(que[1])-1
        o = ord(que[2]) - ord("a")
        seg.update(target, 2**o)

    else:
        left = int(que[1])-1
        right = int(que[2])-1

        x = seg.get(left, right)
        log("x", x)
        count = 0
        while x > 0:
            if x % 2 == 1:
                count += 1
            x = x//2
        print(count)
