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
    A = [SS() for _ in range(H)]

    d = ((1, 0), (0, 1), (-1, 0), (0, -1))

    dist = [[INF] * W for i in range(H)]
    que = collections.deque()

    for i, j in itertools.product(range(H), range(W)):
        if A[i][j] == '#':
            que.append((i, j))
            dist[i][j] = 0

    while que:
        cy, cx = que.popleft()
        for dy, dx in d:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < H and 0 <= nx < W and dist[cy][cx] + 1 < dist[ny][nx]:
                dist[ny][nx] = dist[cy][cx] + 1
                que.append((ny, nx))

    # for i in dist:
    #     print(i)

    ans = max([max(i) for i in dist])
    print(ans)

if __name__ == '__main__':
    resolve()
