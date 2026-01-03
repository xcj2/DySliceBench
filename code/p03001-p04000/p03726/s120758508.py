def examA():
    A, B, C = LI()
    S = A+B+C
    cur = 0
    for i in range(32):
        if A%2==1 or B%2==1 or C%2==1:
            break
        A = (S-A)//2
        B = (S-B)//2
        C = (S-C)//2
        cur +=1
    if cur==32:
        ans = -1
    else:
        ans = cur
    print(ans)
    return

def examB():
    N, M = LI()
    cur = [0]*N
    for i in range(M):
        a, b = LI()
        cur[a-1] +=1
        cur[b-1] +=1
    ans = "YES"
    for j in cur:
        if j%2==1:
            ans = "NO"
            break
    print(ans)
    return


def clear_maze(h,w,s,maze):
#    debug_print(maze)
    distance = [[inf]*w for _ in range(h)]
    def bfs():
        queue = deque()
        queue.append(s)
        distance[s[0]][s[1]] = 0
        while len(queue):
            y, x = queue.popleft()
            for i in range(4):
                nx, ny = x + [1, 0, -1, 0][i], y + [0, 1, 0, -1][i]
                if (0<= nx <w and 0<= ny <h and maze[ny][nx] != '#'):
                    if distance[ny][nx]<=distance[y][x]+1:
                        continue
                    queue.append((ny, nx))
                    distance[ny][nx] = distance[y][x] + 1
        return distance
    return bfs()
def examC():
    H, W, K = LI()
    A = [SI() for _ in range(H)]
    sx = W-1; sy = H-1
    for i in range(H):
        for j in range(W):
            if A[i][j]=="S":
                sy = i; sx = j
                break
        if sy!=H-1 or sx!=W-1:
            break
    D = clear_maze(H,W,[sy,sx],A)
#    for v in D:
#        print(v)
    ans = inf
    for i in range(H):
        for j in range(W):
            if D[i][j]>K:
                continue
            cur = min((i+K-1)//K,(j+K-1)//K,(H+K-i-2)//K,(W+K-j-2)//K)
            ans = min(ans,cur+1)
    print(ans)
    return

def examD():
    def dfs(v, edges, n, visited, matched):
        for u in edges[v]:
            if u in visited:
                continue
            visited.add(u)
            if matched[u] == -1 or dfs(matched[u], edges, n, visited, matched):
                matched[u] = v
                return True
        return False
    N = I()
    V = [set()for _ in range(N)]
    for _ in range(N-1):
        a, b = LI()
        a -= 1; b -= 1
        V[a].add(b)
        V[b].add(a)
    cnt = 0
    matched = [-1] * N
    for s in range(N):
        cnt += dfs(s, V, N, set(), matched)
    #print(cnt)
    if cnt<N:
        print("First")
    else:
        print("Second")
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,inf
mod = 10**9 + 7
inf = 10**18

if __name__ == '__main__':
    examD()
