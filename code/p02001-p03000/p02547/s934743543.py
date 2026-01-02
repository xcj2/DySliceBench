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
    lis=[LI() for i in range(n)]
    for i in range(n-2):
        if lis[i][0]==lis[i][1] and lis[i+1][0]==lis[i+1][1] and lis[i+2][0]==lis[i+2][1]:
            print("Yes")
            exit()
    print("No")

        
        
        
        



        
        
        
        
        
    
if __name__=="__main__":
    main()

