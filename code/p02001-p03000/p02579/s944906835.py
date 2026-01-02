from collections import deque
h, w = map(int, input().split())
Ch, Cw = map(int, input().split())
Dh, Dw = map(int, input().split())
Ch -= 1
Cw -= 1
Dh -= 1
Dw -= 1

WALL = -100
INI = -1
PASSED = 0

S = [[0] * w for _ in range(h)]
for i in range(h):
    tmp = input()
    for j in range(w):
        if tmp[j] == '#':
            S[i][j] = WALL
        else:
            S[i][j] = INI

S[Ch][Cw] = 0
direction = [[0, -1], [-1, 0], [0, 1], [1, 0]]


def dfs(y, x, d):
    d.append((y, x))
    if y == Dh and x == Dw:
        print(S[y][x])
        exit()
    for dy, dx in direction:
        next_y = y + dy
        next_x = x + dx
        if next_y < 0 or next_y >= h or next_x < 0 or next_x >= w:
            continue
        if S[next_y][next_x] == INI:
            #print("y = ", y, "x = ", x, "next_y = ", next_y, "next_x = ", next_x)
            S[next_y][next_x] = S[y][x]
            dfs(next_y, next_x, d)

def bfs(y, x, d):
    for dy in range(-2, 3):
        for dx in range(-2, 3):
            next_y = y + dy
            next_x = x + dx
            if next_y < 0 or next_y >= h or next_x < 0 or next_x >= w:
                continue
            if S[next_y][next_x] == INI:
                d.append((next_y, next_x))
                #print("S[u][x] = ", S[y][x])
                S[next_y][next_x] = S[y][x] + 1
    return False

def show(S):
    for y in range(h):
        for x in range(w):
            if S[y][x] == WALL:
                print("#", end="")
            elif S[y][x] == INI:
                print(".", end="")
            else:
                print(S[y][x], end="")
        print()

d = deque()
d.append((Ch, Cw))
d2 = deque()
while len(d):
    while(len(d)):
        y, x = d.popleft()
        dfs(y, x, d2)

    while len(d2):
        y2, x2 = d2.popleft()
        #print("y2 = ", y2, "x2 = ", x2)
        #show(S)
        bfs(y2, x2, d)

print(-1)