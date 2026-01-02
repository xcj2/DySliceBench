from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

def dfs(x,y):
    global st
    global visited
    global ans

    if MAP[y][x] == '#':
        ans |= 0
        return
    elif MAP[y][x] == 'B':
        ans |= 1
        return
    elif MAP[y][x] == 'W':
        ans |= 2
        return
    else:
        visited[y][x] = True
        st.add((x,y))
        if not visited[y][x+1]:
            dfs(x+1,y)
        if not visited[y][x-1]:
            dfs(x-1,y)
        if not visited[y+1][x]:
            dfs(x,y+1)
        if not visited[y-1][x]:
            dfs(x,y-1)
        return

while True:
    W,H = inpl()
    if W == 0:
        break
    else:
        MAP = []
        MAP.append(['#']*(W+2))
        for _ in range(H):
            MAP.append(['#']+list(input())+['#'])
        MAP.append(['#']*(W+2))

        visited = [[False]*(W+2) for _ in range(H+2)]
        dp = [[-1]*(W+2) for _ in range(H+2)]
        ansb = answ = 0
        for y0 in range(1,H+1):
            for x0 in range(1,W+1):
                if not visited[y0][x0]:
                    st = set([])
                    ans = 0
                    dfs(x0,y0)
                    for x,y in st:
                        dp[y][x] = ans

        #for d in dp:
        #    print(' '.join([str(k).rjust(2) for k in d]))

        answ = ansb = 0
        for d in dp:
            answ += d.count(2)
            ansb += d.count(1)

        print(ansb,answ)

