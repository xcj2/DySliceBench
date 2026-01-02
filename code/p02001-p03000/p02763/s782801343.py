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
    #from math import gcd

    #inf = 10**17
    #mod = 10**9 + 7

    def segfunc(x, y):
        return x | y

    def init(arr):
        for i in range(n):
            seg[i+num-1] = {arr[i]}
        for i in range(num-2,-1,-1) :
            seg[i] = segfunc(seg[2*i+1],seg[2*i+2]) 
        
    def update(k,x):
        k += num-1
        seg[k].clear()
        seg[k] = {x}
        while k:
            k = (k-1)//2
            seg[k].clear()
            seg[k] = segfunc(seg[k*2+1],seg[k*2+2])
        
    def query(p,q):
        if q<=p:
            return ide_ele
        p += num-1
        q += num-2
        res=ide_ele
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
    s = list(input().rstrip())
    for i in range(n):
        s[i] = ord(s[i]) - 97

    ide_ele = set()

    num =2**((n-1).bit_length())

    # セグ木初期化
    seg=[ide_ele]*2*num
    init(s)

    q = int(input())
    for _ in range(q):
        a,b,c = input().rstrip().split()
        if a == '1':
            b = int(b)
            c = ord(c) - 97
            update(b-1, c)
        else:
            b = int(b)
            c = int(c)
            print(len(query(b-1, c)))

if __name__ == '__main__':
    main()