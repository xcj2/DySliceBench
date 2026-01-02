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
    #全部異なるならbit全探索できそう
    #2つ以上同じものがあるとk以上同じものがある時　向きが逆だとして最小値候補に入れておく
    n=I()
    lis=LI()
    if 0 in lis:
        print(0)
        sys.exit()
    c=Counter(lis)
    ans=inf
    multi=[]
    for x in c.keys():
        #print(x)
        if c[x]>=3:
            print(0)
            sys.exit()
        elif c[x]>=2:
            ans=min(ans,x,24-2*x)
            multi.append(x)
    lis.append(0)
    lis=list(set(lis))
    u=len(lis)
    #print(lis)
    #ansは上限
    answers=[]
    #print(ans)
    for x in product([0,1],repeat=u):
        time=[]
        for i in range(u):
            if lis[i] in multi:
                time.append(lis[i])
                time.append(24-lis[i])
            elif x[i]==1:
                time.append(24-lis[i])
            else:
                time.append(lis[i])
        #print(time)
        z=ans
        for i in range(len(time)-1):
            for j in range(i+1,len(time)):
                z=min(z,24-abs(time[i]-time[j]),abs(time[i]-time[j]))   
        #print(z)
        answers.append(z)
        
    print(max(answers))
        
        
        
                
        
        
                
        
            
            
    
            
            
    


                
    
    
    
            
if __name__=="__main__":
    main()
