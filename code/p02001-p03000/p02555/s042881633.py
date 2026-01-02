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
    n=I()
    dp=[1 for i in range(n)]
    dp[0]=0
    if n==1:
        print(0)
        sys.exit()
    dp[1]=0
    for i in range(3,n):
        for j in range(i-2):
            dp[i]=(dp[i]+dp[j])%mod
    #print(dp)
    print(dp[-1]%mod)
    

        
        
        
        
    
if __name__=="__main__":
    main()

