import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


def main():
    from collections import deque
    H, W = MI()
    C = LI()
    D = LI()
    C = [i - 1 for i in C]
    D = [i - 1 for i in D]
    S_ = []
    for i in range(H):
        s = S()
        S_.append(s)
    cost = [[10 ** 10] * W for _ in range(H)]
    cost[C[0]][C[1]] = 0
    queue = deque()
    queue.append(C)
    while len(queue) != 0:
        a = queue.popleft()
        a_cost = cost[a[0]][a[1]]
        for i in range(-2, 3):
            if a[0] + i < 0 or a[0] + i >= H:
                continue
            for j in range(-2, 3):
                if a[1] + j < 0 or a[1] + j >= W:
                    continue
                if i == j == 0:
                    continue
                b = [a[0] + i, a[1] + j]
                b_cost = cost[b[0]][b[1]]
                if S_[b[0]][b[1]] == '#':
                    continue
                if (abs(i) == 1 and j == 0) or (abs(j) == 1 and i == 0):
                    if a_cost < b_cost:
                        cost[b[0]][b[1]] = a_cost
                        queue.appendleft(b)
                else:
                    if a_cost + 1 < b_cost:
                        cost[b[0]][b[1]] = a_cost + 1
                        queue.append(b)
    ans = cost[D[0]][D[1]]
    if ans != 10 ** 10:
        print(ans)
    else:
        print(-1)

if __name__ == "__main__":
    main()
