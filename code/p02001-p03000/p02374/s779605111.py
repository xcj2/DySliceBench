import sys

sys.setrecursionlimit(int(1e6))


class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)

    def get_sum(self, i):
        ret = 0
        while i > 0:
            ret += self.data[i]
            i -= (i & -i)
        return ret

    def add(self, i, w):
        if i == 0:
            return
        while i <= self.n:
            self.data[i] += w
            i += (i & -i)


def dfs(u, cnt):
    cnt += 1
    l[u] = cnt
    for c in tree[u]:
        cnt = dfs(c, cnt)
    cnt += 1
    r[u] = cnt
    return cnt


n = int(input())
l, r = [0] * n, [0] * n
tree = [set(map(int, input().split()[1:])) for _ in range(n)]

bit = BIT(dfs(0, 1))

q = int(input())
for _ in range(q):
    line = list(map(int, input().split()))
    if line[0]:
        print(bit.get_sum(r[line[1]] - 1))
    else:
        bit.add(l[line[1]], line[2])
        bit.add(r[line[1]], -line[2])

