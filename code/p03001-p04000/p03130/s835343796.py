import sys

sys.setrecursionlimit(200000)


def input():
    return sys.stdin.readline()[:-1]


def ii(t: type = int):
    return t(input())


def il(t: type = int):
    return list(map(t, input().split()))


def imi(N: int, t: type = int):
    return [ii(t) for _ in range(N)]


def iml(N: int, t: type = int):
    return [il(t) for _ in range(N)]


def solve():
    tree = [[] for _ in range(4)]
    for i in range(3):
        a, b = il()
        a -= 1
        b -= 1
        tree[a].append(b)
        tree[b].append(a)

    def dfs(prev, s, ans):
        for t in tree[s]:
            if t == prev:
                continue
            ans.append(s)
            _ = dfs(s, t, ans)
        return len(set(ans))

    return "YES" if dfs(-1, 0, []) == 3 else "NO"


if __name__ == "__main__":
    print(solve())
