def main():
    n = int(input())
    *v, = map(int, input().split())

    v0 = assemble(v[::2])
    v1 = assemble(v[1::2])

    if len(v0) == 1 and len(v1) == 1:
        if v0[0][0] == v1[0][0]:
            print(n // 2)
        else:
            print(0)
        return
    elif len(v0) == 1:
        if v0[0][0] == v1[0][0]:
            print(sum_v(v1, 1))
        else:
            print(sum_v(v1, 0))
        return
    elif len(v1) == 1:
        if v0[0][0] == v1[0][0]:
            print(sum_v(v0, 1))
        else:
            print(sum_v(v0, 0))
        return

    score = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            score[i][j] = sum_v(v0, i) + sum_v(v1, j)
            if v0[i][0] == v1[j][0]:
                score[i][j] = 10 ** 9
    print(min([min(s) for s in score]))


def assemble(v):
    dct = {}
    for vel in v:
        if vel in dct:
            dct[vel] += 1
        else:
            dct[vel] = 1
    return sorted(list(dct.items()), key=lambda x: x[1], reverse=True)


def sum_v(v, ii):
    return sum([vv[1] for i, vv in enumerate(v) if i != ii])


main()
