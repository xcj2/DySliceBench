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
    turn=0
    q=I()
    ortop=[]
    orbot=[]
    for i in range(q):
        query=list(input().rstrip().split(" "))
        if query[0]=="1":
            turn=(turn+1)%2
        else:
            x=int(query[1])
            if (x+turn)%2==1:
                ortop.append(query[2])
            else:
                orbot.append(query[2])
    if turn%2==0:
        s1="".join(list(reversed(ortop)))
        s2="".join(orbot)
        print(s1+s+s2)
    else:
        s1="".join(list(reversed(orbot)))
        s2="".join(ortop)
        s="".join(list(reversed(s)))
        
        print(s1+s+s2)
        
        
            
            
            
    

        
    
            
        

        
if __name__=="__main__":
    main()
