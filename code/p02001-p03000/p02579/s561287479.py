from collections import deque
H, W = map(int, input().split())
cy, cx = map(int, input().split())
dy, dx = map(int, input().split())
maze = ['#'*(W+2)]
for hh in range(H):
    maze.append('#' + input() + '#')
maze.append('#'*(W+2))

stepx = [-1, 0, 1, 0]
stepy = [0, -1, 0, 1]
visited = [[0]*(W+2) for _ in range(H+2)]

deque2 = deque()
def floodfill(comp, src):
    count = 0
    while len(src) > 0:
        stak = []
        for (sy, sx) in src:
            #add to new component
            visited[sy][sx] = comp
            count += 1
            deque2.append((sy, sx))
            for i in range(4):
                ny, nx = sy + stepy[i], sx + stepx[i]
                if nx > 0 and nx <= W and ny > 0 and ny <= H\
                        and visited[ny][nx] == 0 and maze[ny][nx] == '.':
                    visited[ny][nx] = -1
                    stak.append((ny, nx))
        src = stak

    return count


def findnextz():
    nxt = []
    while len(deque2) > 0:
        (h, w) = deque2.popleft()
        for ii in range(-2, 3):
            nh = h + ii
            if nh > 0 and nh <= H:
                for jj in range(-2, 3):
                    nw = w + jj
                    if nw > 0 and nw <= W and visited[nh][nw] == 0 and maze[nh][nw] == '.':
                        visited[nh][nw] = -1
                        nxt.append((nh, nw))
    return nxt

def findnext(comp):
    count = 0
    nxt = []
    for h in range(1, H+1):
        for w in range(1, W+1):
            if visited[h][w] == comp:
                for ii in range(-2, 3):
                    nh = h + ii
                    if nh > 0 and nh <= H:
                        for jj in range(-2, 3):
                            nw = w + jj
                            if nw > 0 and nw <= W and visited[nh][nw] == 0 and maze[nh][nw] == '.':
                                visited[nh][nw] = -1
                                nxt.append((nh, nw))

    return nxt

ans = 0
total = 0
comp = 1

#floodfill source
if maze[cy][cx] == '.' and visited[cy][cx] == 0:
    count = floodfill(comp, [(cy, cx)])

# #floodfill dest
# if maze[dy][dx] == '.' and visited[dy][dx] == 0:
#     count = floodfill(comp, (dy, dx))
#     if count > 0:
#         total += count
#         comp += 1
#
#
while count > 0 and visited[dy][dx] <= 0:
    total += count
    #src = findnext(comp)
    src = findnextz()
    comp += 1
    if len(src) > 0:
        count = floodfill(comp, src)
    else: count = 0

print(visited[dy][dx] - 1)
