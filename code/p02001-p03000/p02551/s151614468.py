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
    mod = 10**9+7
#main code here!
    n,q=MI()
    ans=(n-2)**2
    
    x=n
    y=n
    xlist=[n for i in range(n-2)]
    ylist=[n for i in range(n-2)]
    for i in range(q):
        a,b=MI()
        if a==1:
            if b<x:
                ans-=y-2
                for i in range(b,x):
                    ylist[i-2]=y
                x=b
            else:
                ans-=ylist[b-2]-2
        else:
            if b<y:
                ans-=x-2
                for i in range(b,y):
                    xlist[i-2]=x
                y=b
            else:
                ans-=xlist[b-2]-2
        #print(ans)
        #print(xlist)
        #print(ylist)
        #print(x,y)
        #print()
    print(ans)
    
            

            
            
            

    
        
        
        
        
    
        
                    
            
        



        
        
        
        
        
    
if __name__=="__main__":
    main()

