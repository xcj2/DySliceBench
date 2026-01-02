#!python3
import sys
sys.setrecursionlimit(1000000)

from heapq import heappush, heappop, heapify

iim = lambda: map(int, input().rstrip().split())

def resolve():
    H, N = iim()
    AB = [tuple(iim()) for i in range(N)]
    inf = float("inf")
    AB.sort(key=lambda a: (a[0]/a[1], -a[0]), reverse=True)

    def memo(f):
        cache = {}
        def wrapper(*a):
            if a in cache:
                return cache[a]
            b = f(*a)
            cache[a] = b

            return b

        return wrapper

    @memo
    def calc(h):
        if h <= 0: return 0

        bi = inf
        for a, b in AB:
            bj = b + calc(h - a)
            if bi > bj:
                bi = bj
            else:
                break
        return bi

    print(calc(H))



if __name__ == "__main__":
    resolve()

