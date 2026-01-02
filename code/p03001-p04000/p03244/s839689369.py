import collections


def main():
    n = int(input())
    *v, = map(int, input().split())

    v0 = count(v[::2])
    v1 = count(v[1::2])

    if len(v0) == 1 and len(v1) == 1:
        if v0[0][0] == v1[0][0]:
            print(n // 2)
        else:
            print(0)
        return

    l0 = min(2, len(v0))
    l1 = min(2, len(v1))

    INF = 10 ** 9
    score = [[0] * l1 for _ in range(l0)]
    for i in range(l0):
        for j in range(l1):
            score[i][j] = sum_v(v0, i) + sum_v(v1, j)
            if i >= l0 or j >= l1 or v0[i][0] == v1[j][0]:
                score[i][j] = INF
    print(min([min(s) for s in score]))


def count(v):
    return collections.Counter(v).most_common()


def sum_v(v, ii):
    return sum([vv[1] for i, vv in enumerate(v) if i != ii])


main()
