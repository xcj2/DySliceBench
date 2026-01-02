import sys
sys.setrecursionlimit(10 ** 7)

N = int(input())
ABC = []
for _ in range(N):
    ABC.append([int(v) for v in sys.stdin.readline().strip().split(' ')])


def memoize(f):
    cache = {}
    def helper(x, y):
        if (x, y) not in cache:
            cache[(x, y)] = f(x, y)
        return cache[(x, y)]
    return helper

@memoize
def find(d, p):
    if d == -1:
        return 0
    else:
        if p == 0:
            return max(ABC[d][0] + find(d - 1, 1), ABC[d][0] + find(d - 1, 2))
        elif p == 1:
            return max(ABC[d][1] + find(d - 1, 0), ABC[d][1] + find(d - 1, 2))
        else:
            return max(ABC[d][2] + find(d - 1, 0), ABC[d][2] + find(d - 1, 1))

print(max(find(N - 1, 0), find(N - 1, 1), find(N - 1, 2)))
