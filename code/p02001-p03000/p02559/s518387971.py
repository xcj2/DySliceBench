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
    mod = 10**9 + 7
#main code here!
    n,q=MI()
    #ソース　https://juppy.hatenablog.com/entry/2018/11/17/蟻本_python_Binary_Indexed_Tree_競技プログラミング
    #A1 ... AnのBIT(1-indexed)
    BIT = [0]*(n+1)
    #idxの一番下のbit
    #A1 ~ Aiまでの和 O(logN)
    def BIT_query(idx):
        res_sum = 0
        while idx > 0:
            res_sum += BIT[idx]
            idx -= idx&(-idx)
        return res_sum
    
    #Ai += x O(logN)
    def BIT_update(idx,x):
        while idx <= n:
            BIT[idx] += x
            idx += idx&(-idx)
        return
    lis=LI()
    for i in range(n):
        BIT_update(i+1,lis[i])
    for i in range(q):
        a,b,c=MI()
        if a==0:
            BIT_update(b+1,c)
        else:
            ans=BIT_query(c)-BIT_query(b)
            print(ans)



        
        
        
        
        
    
if __name__=="__main__":
    main()

