# coding: utf-8


def array2d(dim1, dim2, init=None):
    return [[init for _ in range(dim2)] for _ in range(dim1)]

II = lambda: int(input())
MI = lambda: map(int, input().split())


def calc_scores(ad, D):
    def calc_score(i):
        x, y = ad[i]
        xp, yp = ad[i-D]
        return abs(x-xp) + abs(y-yp)
    scores = [0] * (D + 1)
    for i in range(D + 1, len(ad) + 1):
        scores.append(scores[i-D] + calc_score(i))
    return scores


def main():
    H, W, D = MI()
    ad = {}
    for i in range(H):
        for j, a in enumerate(MI()):
            ad[a] = (i, j)
    s = calc_scores(ad, D)
    for q in range(II()):
        L, R = MI()
        print(s[R] - s[L])


if __name__ == "__main__":
    main()
