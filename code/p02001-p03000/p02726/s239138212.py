import sys
# sys.setrecursionlimit(100000)
from collections import deque
from collections import defaultdict


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    # 各ノードで幅優先探索を行う
    # 計算量(O(n^2))
    n, x, y = input_int_list()
    g = defaultdict(list)
    g[x].append(y)
    g[y].append(x)
    for i in range(1, n):
        g[i].append(i + 1)
        g[i + 1].append(i)
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        # 幅優先探索
        seen = set()
        dq = deque()
        dq.append((i, 0))  # node,depth
        while dq:
            p, d = dq.popleft()
            if p > i:  # 整数の組(i,j) (1 <= i <= j <= N)
                ans[d] += 1
            for q in g[p]:
                if q not in seen:
                    dq.append((q, d + 1))
                    seen.add(q)

    for i in range(1, n):
        print(ans[i])

    return


if __name__ == "__main__":
    main()
