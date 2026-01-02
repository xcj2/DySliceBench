import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

def main():
    H, W = mapint()
    ch, cw = mapint()
    dh, dw = mapint()
    maze = [list(input()) for _ in range(H)]
    
    dirc = ((-1, 0), (1, 0), (0, -1), (0, 1))
    magic = ((-2, -2), (-2, -1), (-2, 0), (-2, 1), (-2, 2), (-1, -2), (-1, -1), (-1, 1), (-1, 2), (0, -2), (0, 2), (1, -2), (1, -1), (1, 1), (1, 2), (2, -2), (2, -1), (2, 0), (2, 1), (2, 2))
    from collections import deque
    Q = deque([(ch-1, cw-1)])
    
    dist = [[10**18]*W for _ in range(H)]
    dist[ch-1][cw-1] = 0
    while Q:
        y, x = Q.popleft()
        for dy, dx in dirc:
            ny, nx = y+dy, x+dx
            if ny<0 or ny>=H or nx<0 or nx>=W:
                continue
            if maze[ny][nx]=='#':
                continue
            if dist[ny][nx]>dist[y][x]:
                dist[ny][nx] = dist[y][x]
                Q.appendleft((ny, nx))
        
        for dy, dx in magic:
            ny, nx = y+dy, x+dx
            if ny<0 or ny>=H or nx<0 or nx>=W:
                continue
            if maze[ny][nx]=='#':
                continue
            if dist[ny][nx]>dist[y][x]+1:
                dist[ny][nx] = dist[y][x]+1
                Q.append((ny, nx))
    if dist[dh-1][dw-1]>=10**17:
        print(-1)
    else:
        print(dist[dh-1][dw-1])
main()