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
    n,k=MI()
    height=LI()
    ans=inf
    for x in product([0,1],repeat=n):
        if sum(list(x))<k:
            continue
        mx=0
        res=0
        for i in range(n):
            if x[i]==1:
                if height[i]<=mx:
                    res+=mx-height[i]+1
                    #print(mx-height[i]+1)
                    mx+=1
                else:
                    res+=0
                    mx=max(mx,height[i])
            else:
                mx=max(mx,height[i])
        #print(res)
        ans=min(ans,res)
    print(ans)            
                
                
    
        
        
        
        




if __name__=="__main__":
    main()
