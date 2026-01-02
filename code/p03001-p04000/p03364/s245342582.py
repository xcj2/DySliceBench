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
    S=[SI() for i in range(n)]
    ans=0
    if n==1:
        print(1)
        sys.exit()
    st=n*(n-1)//2
    for b in range(n):
        count=0
        for i in range(n-1):
            for j in range(i+1,n):
                #print(b,i,j)
                #print(i,(j+b)%n,j,(i+b)%n)
                if S[i][(j+b)%n]==S[j][(i+b)%n]:
                    count+=1
            if count==st:
                ans+=n
    print(ans)
        
        
                





if __name__=="__main__":
    main()
