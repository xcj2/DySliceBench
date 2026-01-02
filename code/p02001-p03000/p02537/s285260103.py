import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)

def input():
    return sys.stdin.readline().strip()

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

class SegmentTree2:
    # 初期化処理
    # f : SegmentTreeにのせるモノイド
    # default : fに対する単位元
    def __init__(self, size, f=lambda x,y : x+y, default=0):
        self.size = 2**(size-1).bit_length() # 簡単のため要素数Nを2冪にする
        self.default = default
        self.dat = [default]*(self.size*2) # 要素を単位元で初期化
        self.f = f

    def update(self, i, x):
        i += self.size
        self.dat[i] = x
        while i > 0:
            i >>= 1
            self.dat[i] = self.f(self.dat[i*2], self.dat[i*2+1])

    def query(self, l, r):
        l += self.size
        r += self.size
        lres, rres = self.default, self.default
        while l < r:
            if l & 1:
                lres = self.f(lres, self.dat[l])
                l += 1

            if r & 1:
                r -= 1
                rres = self.f(self.dat[r], rres) # モノイドでは可換律は保証されていないので演算の方向に注意
            l >>= 1
            r >>= 1
        res = self.f(lres, rres)
        return res

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
        """
        [q_left, q_right] (閉区間) の値を集計して返します。
        """

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

def main():
    INF = 999999999999999999999999
    MOD = 10**9+7

    n,k = get_nums_l()
    A = list(map(int, [input() for _ in range(n)]))


    # ある数字を末尾に取るときの最長列帳
    sg = SegmentTree2(300001, max, 0)

    for i in range(0, n):
        a = A[i]
        l = max(0, a-k)
        r = min(300000, a+k)
        v = sg.query(l, r+1)
        sg.update(a, v+1)

    print(sg.query(0, 300001))

main()
