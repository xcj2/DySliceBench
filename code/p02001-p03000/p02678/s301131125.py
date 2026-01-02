import sys
from collections import defaultdict
from queue import deque
readline = sys.stdin.buffer.readline
#sys.setrecursionlimit(10**8)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    N, M = geta(int)
    g = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = geta(int)
        g[a].append(b)
        g[b].append(a)

    g[0].append(1)

    ans = [-1] * (N + 1)
    que = deque()
    que.appendleft(0)

    while len(que) > 0:
        parent = que.pop()
        for child in g[parent]:
            if ans[child] == -1:
                ans[child] = parent
                que.appendleft(child)

    print("Yes", *ans[2:], sep="\n")


if __name__ == "__main__":
    main()