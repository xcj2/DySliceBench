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
    lis=LI()
    nums=[i for i in range(10**6+1)]
    spf=[-1 for i in range(10**6+1)]
    i=2
    while i<=10**3:
        if spf[i]>=0:
            i+=1
        for j in range(1,(10**6)//i+1):
            if spf[i*j]==-1:
                spf[i*j]=i
        i+=1
    #print(spf[10**5:10**5+100])
    for i in range(10**6+1):
        if spf[i]<0:
            spf[i]=i
    #print(spf[10**5:10**5+100])
    dic=defaultdict(lambda :0)
    for i in range(n):
        x=lis[i]
        key=set()
        while x>1:
            u=spf[x]
            x//=u
            key.add(u)
        for z in key:
            dic[z]+=1
    flag=True
    #print(dic)
    for z in dic.keys():
        if dic[z]==n:
            print("not coprime")
            sys.exit()
        if dic[z]>1:
            flag=False
        
    if flag==True:
        print("pairwise coprime")
        sys.exit()
    print("setwise coprime")
                
        
            
        
            
            

            
            
            

    
            
            
            
            
        
        
        
    
        
            
        
if __name__=="__main__":
    main()
