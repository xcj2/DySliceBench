from collections import deque
from heapq import heappush, heappop
import sys
sys.setrecursionlimit(10**7)

def input():
    return sys.stdin.readline().strip()

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

def neighbors4(x, y):
  dxy = (0, 1, 0, -1, 0 )
  for i in range(4):
    yield(x + dxy[i], y + dxy[i+1])

def search(cost, sx, sy):
    # ある地点からジャンプ無しで行ける範囲を探索

    que = deque()
    que.append((sx,sy))

    reached = []

    while que:
        x,y = que.popleft()

        # 訪れた場所リスト
        reached.append((x,y))

        if cost_map[y][x] <= cost:
            continue
        cost_map[y][x] = cost

        for x2, y2 in neighbors4(x,y):
            if x2<0 or x2>=w or y2<0 or y2>=h:
                continue
            if grid_s[y2][x2] == ".":
                que.append((x2, y2))
    
    return reached

def jump(cost, x, y):
    if cost >= cost_map[y][x]:
        return
    reached = search(cost, x, y)
    
    # ゴールに到達したらおわり
    if cost_map[dh][dw] != INF:
        print(cost_map[dh][dw])
        exit()
    
    # 1回ジャンプする
    for x,y in reached:
        for y2 in range(max(0, y-2), min(h, y+3)):
            for x2 in range(max(0, x-2), min(w, x+3)):
                if abs(x-x2) + abs(y-y2) < 2:
                    continue
                if grid_s[y2][x2] == "." and cost_map[y2][x2] > cost+1:
                    heappush(jump_que, (cost+1, x2, y2))

def main():
    global h,w,dh,dw,grid_s,cost_map, jump_que,INF
    INF = 999999999999999999999999
    MOD = 10**9+7

    h,w = get_nums_l()
    ch,cw = get_nums_l()
    dh,dw = get_nums_l()

    # 0-originに変換
    ch -= 1
    cw -= 1
    dh -= 1
    dw -= 1

    grid_s = []
    for i in range(h):
        grid_s.append(input())
    
    cost_map = [[INF] * w for _ in range(h) ]

    jump_que = deque()
    jump_que.append((0, cw, ch))

    while jump_que:
        cost, x, y = jump_que.popleft()
        
        if cost >= cost_map[y][x]:
            continue
        reached = search(cost, x, y)
        
        # ゴールに到達したらおわり
        if cost_map[dh][dw] != INF:
            print(cost_map[dh][dw])
            exit()
        
        # 1回ジャンプする
        for x,y in reached:
            for y2 in range(max(0, y-2), min(h, y+3)):
                for x2 in range(max(0, x-2), min(w, x+3)):
                    if abs(x-x2) + abs(y-y2) < 2:
                        continue
                    if grid_s[y2][x2] == "." and cost_map[y2][x2] > cost+1:
                        jump_que.append((cost+1, x2, y2))
    
    print(-1)

main()