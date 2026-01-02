def main():
    """
    Range:
        (x,y)
        X: x-K+1 〜 x+K-1
        Y: y-K+1 〜 y+K-1

    rangeをすべて試す: 無理
        1つの希望を満たすように範囲指定:
            模様は確定する
                (0,0)-(K,K) * 2(W or B)
                K^2 * N -> 10^3^2 * 10^5
            他の希望は満たされるか判定
    """
    N, K = map(int, input().split())
    xy = []
    for _ in range(N):
        x, y, c = input().split()
        a = K if c == "B" else 0
        xy.append((int(x), int(y) + a))

    AC(K, xy)
    # TLE(K, xy)


def fix(x, K2):
    return min(max(0, x), K2)


def boundary(x, y, K):
    K2 = K * 2
    s = set()
    for i in range(-2, 2):
        for j in range(-2, 2):
            if (i + j) % 2 == 1:
                continue

            x1 = fix(x + i * K, K2)
            y1 = fix(y + j * K, K2)
            x2 = fix(x + (i + 1) * K, K2)
            y2 = fix(y + (j + 1) * K, K2)

            if x1 == x2 or y1 == y2:
                continue

            s.add(((x1, y1), (x2, y2)))

    return s

def AC(K, xy):
    K2 = K * 2
    w = [
        [0] * (K2 + 1)
        for _ in range(K2 + 1)
    ]

    for x, y in xy:
        x = x % K2
        y = y % K2
        for (x1, y1), (x2, y2) in boundary(x, y, K):
            w[y1][x1] += 1
            w[y1][x2] -= 1
            w[y2][x1] -= 1
            w[y2][x2] += 1

    ans = max_cumsum(w)
    print(ans)


def max_cumsum(w):
    # error in atcoder pypy3
    #import numpy as np
    #return np.array(w).cumsum(axis=1).cumsum(axis=0).max()

    import copy
    w = copy.deepcopy(w)
    l = len(w)
    for i in range(1, l):
        for j in range(l):
            w[j][i] += w[j][i-1]

    for i in range(l):
        for j in range(1, l):
            w[j][i] += w[j-1][i]

    return max(map(max, w))


def TLE(K, xy):
    ans = 0
    for i in range(2 * K):
        for j in range(2 * K):
            tmp_ans = 0
            for x, y in xy:
                x = (x + i) % (2 * K)
                y = (y + j) % (2 * K)

                w1 = x < K and y < K
                w2 = x >= K and y >= K
                if w1 or w2:
                    tmp_ans += 1

            ans = max(ans, tmp_ans)

    print(ans)

if __name__ == '__main__':
    main()
