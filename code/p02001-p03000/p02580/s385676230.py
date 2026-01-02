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
    h,w,m=MI()
    lis1=[]
    lis2=[]
    for i in range(m):
        a,b=MI()
        lis1.append(a)
        lis2.append(b)
    c1=Counter(lis1)
    X=c1.most_common()
    #print(c1)
    c2=Counter(lis2)
    Y=c2.most_common()
    #print(c2)
    cand1=[]
    cand2=[]
    s=X[0][1]
    for a,b in X:
        if b==s:
            cand1.append(a)
        else:
            break
    #print(cand1)
    t=Y[0][1]
    for a,b in Y:
        if b==t:
            
            cand2.append(a)
        else:
            break
    #print(cand2)
    cand1.sort()
    cand2.sort()
    rest=len(cand1)*len(cand2)
    for i in range(m):
        x,y=lis1[i],lis2[i]
        if cand1[bisect_right(cand1,x)-1]==x and cand2[bisect_right(cand2,y)-1]==y:
            rest-=1
    if rest>0:
        print(s+t)
    else:
        print(s+t-1)
    
            
    

if __name__=="__main__":
    main()

