import sys
import math
from collections import defaultdict, deque
from copy import deepcopy
    
input = sys.stdin.readline
def RD(): return input().rstrip()
def F(): return float(input().rstrip())
def I(): return int(input().rstrip())
def MI(): return map(int, input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float,input().split()))
def Init(H, W, num): return [[num for i in range(W)] for j in range(H)]
    
    
def main():
    H, W = MI()
    d = Init(H, W, -1)
    mylist = [input().rstrip() for i in range(H)]
    move = [[1,0],[0,1],[-1,0],[0,-1]]
    dq = deque()
    dq.append([0,0])
    goal = [H-1,W-1]
    d[0][0] = 0
    while dq:
        ht, wt = dq.popleft()
        for h, w in move:
            h += ht
            w += wt
            if h >= 0 and h < H and w >= 0 and w < W and d[h][w] == -1 and mylist[h][w] != "#":
                d[h][w] = d[ht][wt]+1
                dq.append([h,w])
                
    goal_dist = d[goal[0]][goal[1]]
    if goal_dist == -1:
        print(-1)
    else:
        white = 0
        for i in mylist:
            white += i.count('.')
        print(white-goal_dist-1)


        
    
if __name__ == "__main__":
    main()