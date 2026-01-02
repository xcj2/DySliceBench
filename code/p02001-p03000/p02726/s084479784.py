import sys
sys.setrecursionlimit(1000000000)
from collections import Counter
def key(x, y):
    return str(x)+str(y)
def main2():
    # TLE
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1

    M = {}
    for i in range(N):
        for j in range(i, N):
            M[key(i, j)] = j - i
    
    def helper(x, y, from_cost):
        if 0 <= x <= N-1 and 0 <= y <= N-1:
            if M[key(x,y)] > from_cost+1:
                M[key(x,y)] = from_cost + 1
                cost = from_cost + 1

                helper(x-1,y, cost)
                helper(x+1,y, cost)
                helper(x,y-1, cost)
                helper(x,y+1, cost)
        
    helper(X, Y, 0)

    cost_list = Counter(list(M.values()))
    for k in range(N-1):
        print(cost_list[k+1])

from collections import deque
INF = 1e10


def main3():
    # official TLE
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    ans = [0 for _ in range(N)]
    for sv in range(N):
        dist = [INF for _ in range(N)]
        q = deque([])

        def push(v, d):
            if dist[v] != INF: return
            dist[v] = d
            q.append(v)

        push(sv, 0)

        while q:
            sv = q.popleft()
            d = dist[sv]
            if sv > 0:
                push(sv-1, d+1)
            if sv < N-1:
                push(sv+1, d+1)
            if sv == X:
                push(Y, d+1)
            if sv == Y:
                push(X, d+1)

        for d in dist:
            ans[d] += 1
    
    for k in range(1, N):
        print(ans[k] // 2)

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    dist = [0 for _ in range(N)]
    for i in range(N-1):
        for j in range(i+1, N):
            d = min(abs(X-i)+1+abs(j-Y), abs(i-j), abs(Y-i)+1+abs(j-Y))
            dist[d] += 1
    
    for k in range(1, N):
        print(dist[k])
 

main()