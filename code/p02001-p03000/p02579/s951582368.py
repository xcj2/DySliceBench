import math


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    H, W = read_ints()
    Ch, Cw = read_ints()
    Ch -= 1
    Cw -= 1
    Dh, Dw = read_ints()
    Dh -= 1
    Dw -= 1
    table = []
    for _ in range(H):
        table.append(list(input()))
    costs = [
        [math.inf for _ in range(W)] for _ in range(H)
    ]

    def dfs(points, cost):
        Q = list(points)
        discovered = list(points)
        while Q:
            i, j = Q.pop()
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < H and 0 <= y < W and table[x][y] == '.' and costs[x][y] == math.inf:
                    costs[x][y] = cost
                    Q.append((x, y))
                    discovered.append((x, y))
        reachables = []
        for x, y in discovered:
            for dx in range(-2, 3):
                for dy in range(-2, 3):
                    new_x, new_y = x+dx, y+dy
                    if 0 <= new_x < H and 0 <= new_y < W and table[new_x][new_y] == '.' and costs[new_x][new_y] == math.inf:
                        costs[new_x][new_y] = cost+1
                        reachables.append((new_x, new_y))
        return reachables

    cost = 0
    Q = [(Ch, Cw)]
    costs[Ch][Cw] = 0
    while Q:
        Q = dfs(Q, cost)
        cost += 1
    if costs[Dh][Dw] == math.inf:
        return -1
    return costs[Dh][Dw]


if __name__ == '__main__':
    print(solve())
