from itertools import product


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
    ans1 = fast_f(N, C, c, D)
    assert ans == ans1
    if N <= 30:
        ans2 = TLE(N, C, c, D)
        assert ans == ans2

    print(ans)


def WA(N, C, c, D):
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


def TLE(N, C, c, D):
    """
    3色に割り当てるので C^3
    """
    ans = float("inf")
    for i, j, k in product(range(C), repeat=3):
        if i == j or i == k or j == k:
            continue

        tmp = 0
        for x, y in product(range(N), repeat=2):
            rem = (x + y) % 3
            bef = c[x][y] - 1
            aft = [i, j, k][rem]
            tmp += D[bef][aft]

        ans = min(ans, tmp)

    return ans


def f(N, C, c, D):
    """
    """
    t = [[0] * C for _ in range(3)]
    ans = float("inf")
    for i in range(N):
        for j in range(N):
            # 余りのパターンごとに色の数を集計して圧縮
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
                # 余りのパターン[0,1,2]について、変更後の色の組合せを全列挙[i,j,k]
                # パターンが違うなら、色も異なるので同色にならないように考慮

                tmp = 0
                for bef in range(C):
                    for aft, rem in zip((i, j, k), range(3)):
                        # 違和感 × 対象個数
                        tmp += D[bef][aft] * t[rem][bef]

                ans = min(ans, tmp)

    return ans


def fast_f(N, C, c, D):
    t = [[0] * C for _ in range(3)]
    ans = float("inf")
    for i, j in product(range(N), repeat=2):
        for aft in range(C):
            rem = (i + j) % 3
            color = c[i][j]
            # 個数だけでなく、違和感も前処理に含める
            t[rem][aft] += D[color - 1][aft]

    for i, j, k in product(range(C), repeat=3):
        if i == j or i == k or j == k:
            continue

        tmp = 0
        for aft, rem in zip((i, j, k), range(3)):
            tmp += t[rem][aft]

        ans = min(ans, tmp)

    return ans


if __name__ == '__main__':
    main()
