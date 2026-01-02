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
    
    '''w,h=MI()
    lis=[LI() for i in range(h)]
    step=[[0,-1],[-1,0],[-1,1],[0,-1],[1,0],[0,1]]
    print(lis)
    for i in range(h):
        for j in range(w):
            if lis[i][j]==0:
                count=0
                for x,y in step:
                    if 0<=i+x<h and 0<=j+y<w and lis[i+x][j+y]==1:
                        count+=1
            if count==6:
                lis[i][j]=1
    ans=0
    for i in range(h):
        for j in range(w):
            if lis[i][j]==1:
                for x,y in step:
                    if not (0<=i+x<h and 0<=j+y<w):
                        ans+=1
                    elif lis[i+x][j+y]==0:
                        ans+=1
            print(ans)
    print(ans)
                        
    print(lis)'''
    n=I()
    if n%2==0:
        print(n//2-1)
    else:
        print((n-1)//2)
if __name__=="__main__":
    main()
