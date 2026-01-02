import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
#sys.setrecursionlimit(10**8)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


from queue import PriorityQueue


def main():
    n = gete(int)
    que = PriorityQueue()

    for _ in range(n):
        x, l = geta(int)
        que.put((x + l, x - l))

    ans = 0
    max_r = -10**9

    while not que.empty():
        r, l = que.get()

        if max_r <= l:
            max_r = r
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()