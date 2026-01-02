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
    lis=LI2()
    ind=[i for i in range(n)]
    if lis[0]!=0:
        print(-1)
        sys.exit()
    for i in range(1,n):
        if lis[i]==0:
            ind[i]=0
        else:
            ind[i]=ind[i-1]+1
    for i in range(n):
        if lis[i]>ind[i]:
            print(-1)
            sys.exit()
    ans=0
    for i in range(n-1):
        x=lis[i]
        if lis[i+1]==lis[i]+1:
            continue
        elif lis[i+1]>lis[i]+1:
            print(-1)
            sys.exit()
        else:
            ans+=x
    if n!=1 and lis[-1]==lis[-2]+1:
        ans+=lis[-1]
    else:
        ans+=lis[-1]
    
    print(ans)
            
            
            
            
        
    
    
    
    



if __name__=="__main__":
    main()
