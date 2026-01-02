import sys
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def li(): return list(input().rstrip())
# template

# BEGIN CUT HERE
from queue import Queue
def bfs(field, sy, sx, wall, dir):
    h = len(field)
    w = len(field[0])
    dp = [[-1 for _j in range(w)] for _i in range(h)]
    q = Queue()

    dp[sy][sx] = 0
    q.put((sy, sx))
    
    dy = [1, -1, 0, 0, 1, 1, -1, -1]
    dx = [0, 0, 1, -1, 1, -1, 1, -1]
    def isin(x,y): return 0 <= y and y < h and 0 <= x and x < w
    
    while not q.empty():
        y, x = q.get()
        for k in range(dir):
            ny,nx = y+dy[k],x+dx[k]
            if not isin(nx, ny) or field[ny][nx] == wall:
                continue
            elif dp[ny][nx] != -1:
                continue
            dp[ny][nx] = dp[y][x] + 1
            q.put((ny,nx))
        
    return dp
    
# END CUT HERE

def ABC088_D():
    h, w = mi()
    s = [['' for _j in range(w)] for _i in range(h)]
    for i in range(h):
        s[i] = li()
    dp = bfs(s, 0, 0, '#', 4)
    if dp[h - 1][w - 1] < 0:
        print(-1)
    else:
        cnt = 0
        for i in range(h):
            for j in range(w):
                cnt += s[i][j] == '.'
        print(cnt - (dp[h - 1][w - 1] + 1)) # 0-indexed
# verified on 2019/06/13
# Python3:29ms https://atcoder.jp/contests/abc088/submissions/5898220
# Pypy3:239ms https://atcoder.jp/contests/abc088/submissions/5898207
# https://atcoder.jp/contests/abc088/tasks/abc088_d

def ATC002_A():
    R, C = mi()
    sy, sx = mi()
    gy, gx = mi()
    s = [['' for _j in range(C)] for _i in range(R)]
    for i in range(R):
        s[i] = li()
    dp = bfs(s, sy-1, sx-1, '#', 4) # 0-indexed
    print(dp[gy-1][gx-1]) # 0-indexed

# グリッドでないbfs
def ABC126_D():
    N= ii()
    G = [[] for i in range(N)]
    for i in range(N-1):
        a, b, w = mi()
        a -= 1
        b -= 1
        G[a].append((b,w))
        G[b].append((a,w))
    dist = [-1 for _ in range(N)]
    que = Queue()
    for v in range(N):
        if dist[v] != -1:
            # v が探索済ならスルー
            continue
        dist[v] = 0
        que.put(v)
        while not que.empty():
            v = que.get()
            for nv,nw in G[v]:
                if dist[nv] == -1:
                    dist[nv] = dist[v] + nw
                    que.put(nv)
    for i in dist:
        if i % 2 == 0:
            print(0)
        else:
            print(1)
# verified on 2019/06/28
# Python3 https://atcoder.jp/contests/abc126/submissions/6141196


if __name__ == '__main__':
    # ABC088_D()
    # ATC002_A()
    ABC126_D()