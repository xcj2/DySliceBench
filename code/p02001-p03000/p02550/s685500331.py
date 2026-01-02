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
    n,x,m=MI()
    seq=[x]
    y=x
    for i in range(2*10**5+10):
        y=((y%m)**2)%m
        seq.append(y)
        #print(y)
    #print(seq)
    z=seq[m-1]
    repeat=[]
    for i in range(1,m+1):
        repeat.append(seq[i+m-1])
        if seq[i+m-1]==z:
            rep=i
            #print(i)
            break
    #print(len(repeat)==m)
    if n<=m:
        print(sum(seq[:n]))
    else:
        ans=sum(seq[:m])
        #print(repeat[:1])
        counts=(n-m)//rep
        S=sum(repeat)
        ans+=S*counts
        rest=(n-m)%rep
        last=m-1+counts*rep
        '''for i in range(last+1,n):
            ans+=repeat[(i-(m-1))%rep]'''
        for i in range(rest):
            ans+=repeat[i]
        print(ans)
    
        
        
        
        
    
        
                    
            
        



        
        
        
        
        
    
if __name__=="__main__":
    main()

