import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

def main():
    N, X, Y = map(int, input().split())

    ans = [0] * N
    for i in range(1, N+1):
        dist = [-1] * (N+1)
        dist[i] = 0
        q = deque()
        q.append(i)
        def push(l, m):
            if dist[l] > -1:
                return
            q.append(l)
            dist[l] = dist[m] + 1
            ans[dist[l]] += 1

        while q:
            j = q.popleft()
            if j < N: push(j+1, j)
            if j > 1: push(j-1, j)
            if j == X: push(Y, j)
            if j == Y: push(X, j)
    print(*[i // 2for i in ans[1:]], sep='\n')

if __name__ == '__main__':
    main()
