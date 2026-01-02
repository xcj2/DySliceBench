def main():
    """
    1 <= N <= 500
    3 <= C <= 30
    (i!=j): 1 <= D(i,j) <= 1000
    (i==j): 0  = D(i,j)
    1 <= c(i,j) <= C
    """
    N, C = map(int, input().split())
    D = [
        list(map(int, input().split()))
        for _ in range(C)
    ]
    c = [
        list(map(int, input().split()))
        for _ in range(N)
    ]
    ans = f(N, C, c, D)
    print(ans)


def TLE(N, C, c, D):
    for i in range(N):
        for j in range(N):
            for x in range(N):
                for y in range(N):
                    same_type = (i + j) % 3 == (x + y) % 3
                    c1 = c[i][j]
                    same_color = c1 == c[x][y]
                    if same_type != same_color:
                        D[c1-1]

    return


def f(N, C, c, D):
    """
    """
    t = [[0] * C for _ in range(3)]
    ans = float("inf")
    for i in range(N):
        for j in range(N):
            # 余りのパターンごとに色情報の集計
            rem = (i + j) % 3
            color = c[i][j]
            t[rem][color - 1] += 1

    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if i == k or j == k:
                    continue

                tmp = 0
                for bef in range(C):
                    for aft, rem in zip((i, j, k), range(3)):
                        tmp += D[bef][aft] * t[rem][bef]

                ans = min(ans, tmp)

    return ans


if __name__ == '__main__':
    main()
