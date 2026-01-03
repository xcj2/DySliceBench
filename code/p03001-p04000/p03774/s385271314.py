def args():
    N, M = map(int, input().split())

    ST = []
    for _ in range(N):
        ST.append(tuple(map(int, input().split())))

    CP = []
    for _ in range(M):
        CP.append(tuple(map(int, input().split())))

    # print(N, M)
    # print(ST)
    # print(CP)

    return N, M, ST, CP


def solve(N, M, ST, CP):
    def get_dist(xy1, xy2):
        x1, y1 = xy1
        x2, y2 = xy2

        return abs(x1 - x2) + abs(y1 - y2)

    res = []
    for st in ST:
        min_cp, min_dist = 0, float("inf")
        for i, cp in enumerate(CP):
            dist = get_dist(st, cp)
            if dist < min_dist:
                min_dist = dist
                min_cp = i
        res.append(min_cp + 1)

    return res


if __name__ == '__main__':
    ans = solve(*args())
    for a in ans:
        print(a)
