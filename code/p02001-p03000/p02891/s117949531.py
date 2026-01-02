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
    s=SI()
    k=I()
    u=len(s)
    seq=0
    x=1
    for i in range(u-1):
        if s[i]==s[i+1]:
            x+=1
        else:
            seq+=x//2
            x=1
    seq+=x//2
    #print(seq)
            
    a=1
    for i in range(u-1):
        if s[0]==s[i+1]:
            a+=1
        else:
            break
    b=1
    for i in range(u-1):
        if s[-1]==s[u-1-(1+i)]:
            b+=1
        else:
            break
    #print(a,b)
    if x==u:
        ans=(u*k)//2
    else:
        if s[0]!=s[-1]:
            ans=(seq)*k
        else:
            ans=(seq)*k-(a//2+b//2-(a+b)//2)*(k-1)
    print(ans)
        





if __name__=="__main__":
    main()
