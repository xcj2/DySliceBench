def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil,pi,factorial,sqrt
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
    s=SI()
    n=len(s)
    ans=inf
    c=Counter(list(s))
    #print(c)
    for strs in c.keys():
        mx=0
        key=0
        for i in range(n):
            if s[i]==strs:
                mx=max(mx,key)
                key=0
            else:
                key+=1
        mx=max(mx,key)
        #print(mx)
        ans=min(ans,mx)
    print(ans)
        
            
                
                
        
    
if __name__=="__main__":
    main()

