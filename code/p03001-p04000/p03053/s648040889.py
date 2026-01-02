import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    from collections import deque

    h, w = input_int_list()
    grid = []
    visited = []
    grid.append(["@"] * (w + 2))
    visited.append([True] * (w + 2))
    for _ in range(h):
        grid.append(["@"] + list(input()) + ["@"])
        visited.append([True] + [False] * w + [True])
    grid.append(["@"] * (w + 2))
    visited.append([True] * (w + 2))

    # 幅優先探索で すべてを"#"に変える。
    # かかった手数分が答え
    direction = ((0, 1), (1, 0), (-1, 0), (0, -1))
    dq = deque()
    # すべての"#"をdequeに入れる
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if grid[i][j] == "#":
                dq.append((i, j, 0))
                visited[i][j] = True
    ans = 0
    # 幅優先探索
    while dq:
        i, j, d = dq.popleft()
        for di, dj in direction:
            if grid[i + di][j + dj] == "." and not visited[i + di][j + dj]:
                dq.append((i + di, j + dj, d + 1))
                visited[i + di][j + dj] = True
                ans = max(ans, d + 1)

    print(ans)
    return


if __name__ == "__main__":
    main()
