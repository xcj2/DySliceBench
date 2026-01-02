def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil,pi,factorial
    from operator import itemgetter
    def I(): return int(input())
    def MI(): return map(int, input().split())
    def LI(): return list(map(int, input().split()))
    def LI2(): return [int(input()) for i in range(n)]
    def MXI(): return [[LI()]for i in range(n)]
    def SI(): return input().rstrip()
    def printns(x): print('\n'.join(x))
    def printni(x): print('\n'.join(list(map(str,x))))
    inf = 10**17
    mod = 998244353
#main code here!
    n,k=MI()
    area=[LI() for i in range(k)]
    #ソース　https://juppy.hatenablog.com/entry/2018/11/17/蟻本_python_Binary_Indexed_Tree_競技プログラミング
    #A1 ... AnのBIT(1-indexed)
    m=2*n
    BIT = [0]*(2*n+1)
    #idxの一番下のbit
    #A1 ~ Aiまでの和 O(logN)
    def BIT_query(idx):
        res_sum = 0
        while idx > 0:
            res_sum += BIT[idx]%mod
            idx -= idx&(-idx)
        return res_sum%mod
    
    #Ai += x O(logN)
    def BIT_update(idx,x):
        while idx <= m:
            BIT[idx] += x%mod
            idx += idx&(-idx)
        return
    BIT_update(n+1,1)
    #print(BIT)
    for i in range(n+2,2*n+1):
        ans=0
        for j in range(k):
            l,r=area[j]
            #print(l,r)
            #print(BIT_query(i-r-1),BIT_query(i-l))
            ans=(ans+BIT_query(i-l)-BIT_query(i-r-1))%mod
        #print(ans)
        BIT_update(i,ans%mod)
        #print(BIT)
    #print(BIT)
    print((BIT_query(2*n)-BIT_query(2*n-1))%mod)
            

    
        
        
        
        
    
        
                    
            
        



        
        
        
        
        
    
if __name__=="__main__":
    main()

