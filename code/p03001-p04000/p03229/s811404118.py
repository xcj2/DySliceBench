# coding: utf-8
# hello worldと表示する
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
    lis.sort()
    ans=0
    if n%2==0:
        x=n//2
        for i in range(x-1):
            ans+=2*(lis[n-i-1]-lis[i])
        ans+=lis[n-x]-lis[x-1]
        print(ans)
    else:
        if n==1:
            print(0)
            sys.exit()
        x=n//2
        ans1=0  
        ans2=0
        for i in range(x):
            ans1+=2*lis[n-i-1]
            ans2-=2*lis[i]
        for i in range(x-1):
            ans1-=2*lis[i]
            ans2+=2*lis[n-i-1]
        ans1-=lis[x]+lis[x-1]
        ans2+=lis[x]+lis[x+1]
        #print(ans1,ans2)
        print(max(ans1,ans2))
if __name__=="__main__":
    main()
