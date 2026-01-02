# coding: utf-8
# Your code here!

import sys
readline = sys.stdin.readline
read = sys.stdin.read

#n,*a = [int(i) for i in read().split()]
#a = [int(i) for i in readline().split()]
#n = int(input())

def solve():
    from bisect import bisect_right, bisect_left
    
    n,k,*a = map(int,read().split())
    a.sort()
    
    #v = [a[i]*a[j] for i in range(n) for j in range(i+1,n)]
    #v.sort()
    #print(v)
    #print(v[k-1])
    
    l = bisect_left(a,0)
    r = bisect_right(a,0,lo = l)
    
    a_neg = [-i for i in a[:l][::-1]]
    a_pos = a[r:]
    
    if k <= l*(n-r): # negative
        def check(x): #x 以上は k 個以上あるか？
            res = (n-r)*l
            L = n-r
            v = 0
            for i in a_neg[::-1]:
                V = (x+i-1)//i
                while v < L and a_pos[v] < V:
                    v += 1
                res -= v
            return res >= k
    
        ok = 0
        ng = 10**18
        while ng-ok > 1:
            mid = (ok+ng)//2
            if check(mid): ok = mid
            else: ng = mid
    
        print(-ok)
    
    elif k <= n*(n-1)//2 - l*(l-1)//2 - (n-r)*(n-r-1)//2:
        print(0)
    
    else:
        k -= n*(n-1)//2 - l*(l-1)//2 - (n-r)*(n-r-1)//2
    
        def check(x): #x 以下は k 個以上あるか？
            res = 0
            vn = l-1
            for i,ai in enumerate(a_neg):
                X = x//ai
                while vn and a_neg[vn] > X:
                    vn -= 1            
                #vn = bisect_right(a_neg,x//ai,hi=vn)
                if vn+1 > i+1: res += vn+1-i-1

            vp = n-r-1
            for i,ai in enumerate(a_pos):
                X = x//ai
                while vp and a_pos[vp] > X:
                    vp -= 1            
                #vp = bisect_right(a_pos,x//ai,hi=vp)
                if vp+1 > i+1: res += vp+1-i-1
            return res >= k
        
        ng = 0
        ok = 10**18
        while ok-ng > 1:
            mid = (ok+ng)//2
            if check(mid): ok = mid
            else: ng = mid
    
        print(ok)


solve()



