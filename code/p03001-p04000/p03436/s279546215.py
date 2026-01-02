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
        print(cnt - (dp[h - 1][w - 1] + 1))
# verified on 2019/06/13
# Pypy3:233ms https://atcoder.jp/contests/abc088/submissions/5898207
# https://atcoder.jp/contests/abc088/tasks/abc088_d

if __name__ == '__main__':
    ABC088_D()