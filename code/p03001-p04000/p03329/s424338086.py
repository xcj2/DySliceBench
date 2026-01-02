import sys
sys.setrecursionlimit(10 ** 9)
from functools import lru_cache
def input(): return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    yen = [6 ** i for i in range(1, 7)]
    yen += [9 ** i for i in range(1, 6)]
    yen = [i for i in yen if i <= N]
    yen.sort(reverse=True)

    def MIN(a, b):
        if a > b:
            return b
        else:
            return a

    @lru_cache(maxsize=None)
    def dfs(x, n, m):
        n += 1
        for y in yen:
            if n >= m:
                return n
            if y > x:
                continue
            if x - y < 6:
                return n + x - y
            m = MIN(dfs(x - y, n, m), m)
        return m

    print(dfs(N, 0, N))

if __name__ == '__main__':
    main()
