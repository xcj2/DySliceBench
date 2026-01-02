import sys
import math
from collections import defaultdict, deque
    
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
    N = I()
    mylist = [[] for i in range(N)]
    for i in range(N):
        temp = LI()
        temp2 = temp[1]
        for j in range(temp2):
            mylist[temp[0]-1].append(temp[2+j]-1)
    #初期化,距離、訪れたか。
    d = [-1] * N
    d[0] = 0
    dq = deque()
    dq.append(0)
    while dq:
        now = dq.popleft()
        for next_p in mylist[now]:
            if d[next_p] == -1:
                d[next_p] = d[now]+1
                dq.append(next_p)
    for index, num in enumerate(d):
            print(index+1, num)
            
        
    
if __name__ == "__main__":
    main()
