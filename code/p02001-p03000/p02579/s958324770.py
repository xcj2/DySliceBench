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
    h,w=MI()
    sx,sy=MI()
    gx,gy=MI()
    sy-=1
    sx-=1
    gy-=1
    gx-=1
    mp=[[0]*h for i in range(w)]
    Q=deque([[sy,sx]])
    for i in range(h):
        s=SI()
        for j in range(w):
            if s[j]=="#":
                mp[j][i]=1
    #print(mp)
    turn=[[inf]*h for i in range(w)]
    turn[sy][sx]=0
    #print(turn)
    step=[[-1,0],[1,0],[0,1],[0,-1]]
    
    while Q:
        y,x=Q.popleft()
        z=turn[y][x]
        if y==gy and x==gx:
            print(turn[y][x])
            sys.exit()
        for j,i in step:
            if not (0<=y+j<w and 0<=x+i<h):
                continue
            elif mp[y+j][x+i]==1:
                continue
            else:
                if z<turn[y+j][x+i]:
                    turn[y+j][x+i]=z
                    Q.appendleft([y+j,x+i])
        #print(turn)
        for i in range(-2,3):
            for j in range(-2,3):
                if not (0<=y+j<w and 0<=x+i<h):
                    continue
                elif mp[y+j][x+i]==1:
                    continue
                else:
                    if z+1<turn[y+j][x+i]:
                        turn[y+j][x+i]=z+1
                        Q.append([y+j,x+i])
        #print(turn)
    #print(turn)
    print(-1)
        
                
                
        
        
        
        
            
            
    
if __name__=="__main__":
    main()

