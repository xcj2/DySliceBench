import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def dfs(G, i):
    seen = set([i])
    stack = [i]
    cnt = 0
    while stack:
        node = stack.pop()
        cnt += 1
        for _n in G[node]:
            if _n not in seen:
                seen.add(_n)
                stack.append(_n)
    return cnt


def main():
    from collections import defaultdict
    G = defaultdict(set)
    edge = []
    n, m = input_int_list()

    for _ in range(m):
        a, b = input_int_list()
        G[a].add(b)
        G[b].add(a)
        edge.append((a, b))

    ans = 0
    # すべての辺を取り除いたときに、dfsで全ノードを辿れるか調べる
    # O(n*m)
    for a, b in edge:
        G[a].remove(b)
        G[b].remove(a)
        cnt = dfs(G, 1)
        if cnt < n:
            ans += 1
        G[a].add(b)
        G[b].add(a)

    print(ans)

    return


if __name__ == "__main__":
    main()
