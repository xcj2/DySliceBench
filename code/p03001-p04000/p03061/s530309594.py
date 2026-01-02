def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    import math

    #inf = 10**17
    #mod = 10**9 + 7

    def segfunc(a, b):
        if b == 0:
            return a
        else:
            return segfunc(b, a % b)

    def init(arr):
        # 0-index/上段の分ズラす
        for i in range(n):
            seg[i+num-1]=arr[i]
        # 上段の分を右から埋めていく
        for i in range(num-2,-1,-1) :
            seg[i]=segfunc(seg[2*i+1],seg[2*i+2]) 
        
    def update(k,x):
        # 元の配列のindex→seg木上のindex
        k += num-1
        seg[k] = x
        while k:
            k = (k-1)//2
            seg[k] = segfunc(seg[k*2+1],seg[k*2+2])
        
    def query(p,q):
        # 不当な区間
        if q<=p:
            return ide_ele
        p += num-1
        q += num-2
        res=ide_ele
        # 最下段から区間を見て更新していく
        # 見ている区間が覆う区間はその時点で見る必要はなく
        # 半分しか覆っていない区間は更新する
        # 上段に上がる際に区間外が混ざらないようにする
        while q-p>1:
            if p&1 == 0:
                res = segfunc(res,seg[p])
            if q&1 == 1:
                res = segfunc(res,seg[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        if p == q:
            res = segfunc(res,seg[p])
        else:
            res = segfunc(segfunc(res,seg[p]),seg[q])
        return res

    n = int(input())
    A = list(map(int, input().split()))

    # 単位元
    ide_ele = 0

    # num:n以上の最小の2のべき乗
    # n:5~8のときnum=8なので3が入ってほしいから-1
    num =2**((n-1).bit_length())

    # セグ木初期化
    seg=[ide_ele]*2*num
    init(A)

    res = 0
    for i in range(n):
        res = max(res, segfunc(query(0, i), query(i+1, n)))
    print(res)

if __name__ == '__main__':
    main()