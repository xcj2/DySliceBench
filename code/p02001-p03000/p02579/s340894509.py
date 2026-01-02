import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    H, W = LI()
    Ch, Cw = LI_()
    Dh, Dw = LI_()
    S = [SS() for _ in range(H)]

    d = ((1, 0), (0, 1), (-1, 0), (0, -1)) 
    dist = [[INF] * W for _ in range(H)]
    que = collections.deque()
    que.append((Ch, Cw, 0))
    dist[Ch][Cw] = 0
    while que:
        cy, cx, cost = que.popleft()
        for dy, dx in d:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < H and 0 <= nx < W and S[ny][nx] == '.' and cost < dist[ny][nx] :
                dist[ny][nx] = cost
                que.appendleft((ny, nx, cost))
        for dy, dx in itertools.product(range(-2, 3), repeat=2):
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < H and 0 <= nx < W and S[ny][nx] == '.' and cost + 1 < dist[ny][nx] :
                dist[ny][nx] = cost + 1
                que.append((ny, nx, cost + 1))

    if dist[Dh][Dw] == INF:
        print(-1)
    else:
        print(dist[Dh][Dw])

if __name__ == '__main__':
    resolve()
