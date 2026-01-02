#関数リスト
import sys
input = sys.stdin.readline
from collections import defaultdict, deque

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    h, w, k = MI()
    x1, y1, x2, y2 = MI()
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1

    mylist = [0] * h

    #tableの読み込み
    for i in range(h):
        temp = input().rstrip()
        temp = [temp[j] for j in range(w)]
        mylist[i] = temp
    #初期化
    distance = [[-1 for i in range(w)] for j in range(h)]
    distance[x1][y1] = 0
    d = deque()
    start = (x1, y1)
    goal = [x2, y2]
    d.append(start)
    move = ([-1,0],[1,0],[0,1],[0,-1])

    while d:
        pos = d.popleft()
        x = pos[0]
        y = pos[1]
        if x == x2 and y == y2:
            print(distance[x2][y2])
            exit()
        dist = distance[x][y]
        for i in move:
            #tempxの初期化
            tempx = x
            tempy = y
            for l in range(k):
                tempx += i[0]
                tempy += i[1]
                if not ((tempx >= 0 and tempx <= h-1) and (tempy >= 0 and tempy <= w - 1)):
                    break
                elif mylist[tempx][tempy] == "." and distance[tempx][tempy] == -1:
                    distance[tempx][tempy] = dist + 1
                    d.append((tempx, tempy))
                elif dist + 1 <= distance[tempx][tempy] and mylist[tempx][tempy] == ".":
                    distance[tempx][tempy] = dist + 1
                else:
                    break
    print(-1)            
        
main()
