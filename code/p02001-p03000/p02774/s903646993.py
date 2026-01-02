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
    n,k=MI()
    lis=LI()
    p,z,m=0,0,0
    plus=[]
    minus=[]
    for i in range(n):
        if lis[i]>0:
            p+=1
            plus.append(lis[i])
        elif lis[i]==0:
            z+=1
        else:
            m+=1
            minus.append(lis[i])
    plus.sort()
    minus.sort()
    #print(plus)
    #print(minus)
    #plus,minus,sort
    resm=p*m
    resz=z*p+z*m+p*m+z*(z-1)//2
    if k<=resm:
        left=-10**18-1
        right=-1
        while left+1<right:
            x=(left+right)//2
            i=0
            ans=0
            j=0
            while i<p:
                while j<m:
                    if plus[i]*minus[j]<=x:
                        if j==m-1:
                            ans+=m
                            i+=1
                            break
                        j+=1
                    else:
                        i+=1
                        ans+=j
                        break
            #print(left,right,x,ans)
            if ans>=k:
                right=x
            else:
                left=x
        print(right)
    
    elif k<=resz:
        print(0)
        sys.exit()
    else:
        k=k-resz
        #print(k)
        left=0
        right=10**18
        square=[]
        for i in range(p):
            square.append(plus[i]**2)
        for i in range(m):
            minus[i]*=(-1)
            square.append(minus[i]**2)
        square.sort()
        plus.sort()
        minus.sort()
        plus2=sorted(plus,reverse=True)  
        minus2=sorted(minus,reverse=True)
        while left+1<right:
            x=(left+right)//2
            i=0
            ans=0
            j=0
            zure=bisect_right(square,x)-1
            while i<p:
                while j<p:
                    if plus2[i]*plus[j]<=x:
                        if j==p-1:
                            ans+=p
                            i+=1
                            break
                        j+=1
                    else:
                        i+=1
                        ans+=j
                        break
            i=0
            j=0
            while i<m:
                while j<m:
                    if minus2[i]*minus[j]<=x:
                        if j==m-1:
                            ans+=m
                            i+=1
                            break
                        j+=1
                    else:
                        i+=1
                        ans+=j
                        break
            #print(left,right,x,ans,zure,(ans-zure)//2)
            if (ans-zure)//2>=k:
                right=x
            else:
                left=x
        print(right)
            
if __name__=="__main__":
    main()
