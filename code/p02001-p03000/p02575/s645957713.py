'''
自宅用PCでの解答
'''
import math
#import numpy as np
import itertools
import queue
import bisect
from collections import deque,defaultdict
import heapq as hpq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)
mod = 10**9+7 #998244353
dir = [(-1,0),(0,-1),(1,0),(0,1)]
alp = "abcdefghijklmnopqrstuvwxyz"

class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

class Binary_Indexed_Tree:
    '''
    Binary_Indexed_Tree
    A1 ... AnのBIT(1-indexed)
    std_mapを使うときには一緒に貼る
    '''
    def __init__(self,n):
        self.N = n
        self.BIT = [0]*(n+1)
        self.l2 = 2**(len(format(n,'b'))-1)

    #A1 ~ Aiまでの和 O(logN)
    def get_sum(self,idx):
        res_sum = 0
        while idx > 0:
            res_sum += self.BIT[idx]
            idx -= idx&(-idx)
        return res_sum

    #Al ~ Arの和
    def query(self,l,r):
        return self.get_sum(r)-self.get_sum(l-1)

    #Ai += x O(logN)
    def add(self,idx,x):
        while idx <= self.N:
            self.BIT[idx] += x
            idx += idx&(-idx)
        return

    # 和がw以上になる最小のindex
    def lower_bound(self,w):
        if w <= 0:
            return 0
        x = 0
        k = self.l2
        while k > 0:
            if x+k <= self.N and self.BIT[x+k] < w:
                w -= self.BIT[x+k]
                x += k
            k //= 2
        return x+1

    # 和がwより大きくなる最小のindex
    def upper_bound(self,w):
        x = 0
        k = self.l2
        while k > 0:
            if x+k <= self.N and self.BIT[x+k] <= w:
                w -= self.BIT[x+k]
                x += k
            k //= 2
        return x+1

class std_map:
    '''
    c++のstd::map(平衡二分探索木)
    dictにおいてkeyの範囲が限定されてkeyに順序が組み込まれたもの
    念願のlower_boundとupper_boundができるようになった
    '''

    def __init__(self,n,init):
        self.size = n
        self.keys = set()
        self.bit = Binary_Indexed_Tree(n+1)
        self.dic = [init]*(n+1)

    def __contains__(self,key): # keyを持つか
        return key in self.keys

    def __getitem__(self,key): # keyに対するvalueを返す
        return self.dic[key]

    def __setitem__(self,key,value): # dic[key]をvalueで置き換える
        if not key in self.keys:
            self.bit.add(key,1)
            self.keys.add(key)
        self.dic[key] = value

    def remove(self,key): # keyをmapから取り除く
        self.keys.remove(key)
        self.bit.add(key,-1)

    def lower_bound(self,k): # k以上の最小のkeyを返す
        return self.bit.lower_bound(self.bit.get_sum(k))

    def upper_bound(self,k): # kより大きい最小のkeyを返す
        return self.bit.upper_bound(self.bit.get_sum(k))

    def kth_key(self,k): # k番目に小さいkeyを返す
        return self.bit.lower_bound(k)

    def kth_value(self,k): # k番目に小さいkeyに対するvalueを返す
        return self.dic[self.kth_key(k)]

    def prev_k(self,k): # kの一つ前のkeyを返す
        idx = self.bit.get_sum(k)
        if idx == 0:
            return -1
        return self.bit.lower_bound(idx-1)

    def prev_k(self,k): # kの一つ後のkeyを返す
        idx = self.bit.get_sum(k)
        if idx == self.size:
            return -1
        return self.bit.lower_bound(idx+1)

def main():
    h,w = map(int,ipt().split())
    st = SegTree([10**18]+[0]*w+[10**18],min,10**18)
    s = std_map(w+2,0)
    for i in range(1,w+2):
        s.bit.add(i,1)
    s.keys = set(range(1,w+2))


    for i in range(h):
        a,b = map(int,ipt().split())
        pl = s.bit.get_sum(a-1)+1
#        print(pl)
        pa = s.kth_key(pl)
        mv = 10**18
        while pa <= b:
#            print(pa)
            st.update(pa,10**18)
            mv = min(mv,s[pa]-pa)
            s.remove(pa)
            pa = s.kth_key(pl)

#        print(st.tree)

        mv += b+1
        if b != w:
            if (not b+1 in s) or s[b+1] > mv:
                st.update(b+1,mv)
                s[b+1] = mv

        mv = st.tree[1]
        if mv == 10**18:
            print(-1)
        else:
            print(mv+i+1)

    return None

if __name__ == '__main__':
    main()
