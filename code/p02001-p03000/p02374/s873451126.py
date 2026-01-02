import sys

sys.setrecursionlimit(200000)


class BIT(object):
    def __init__(self, n: int) -> None:
        self.n = n
        self.data = [0] * (n + 1)

    def get_sum(self, i: int) -> int:
        ret = 0
        while i > 0:
            ret += self.data[i]
            i -= (i & -i)
        return ret

    def add(self, i: int, w: int) -> None:
        if i == 0:
            return
        while i <= self.n:
            self.data[i] += w
            i += (i & -i)


def dfs(u: int, cnt: int) -> int:
    global left, right
    cnt += 1
    left[u] = cnt
    for c in tree[u]:
        cnt = dfs(c, cnt)
    cnt += 1
    right[u] = cnt
    return cnt


if __name__ == "__main__":
    n = int(input())
    left, right = [0] * n, [0] * n
    tree = []
    for _ in range(n):
        _, *children = map(lambda x: int(x), input().split())
        tree.append(set(children))

    bit = BIT(dfs(0, 1))

    q = int(input())
    for _ in range(q):
        query = list(map(lambda x: int(x), input().split()))
        if query[0]:
            print(bit.get_sum(right[query[1]] - 1))
        else:
            bit.add(left[query[1]], query[2])
            bit.add(right[query[1]], -query[2])

