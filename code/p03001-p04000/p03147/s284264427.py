def mizuyari2(row):
    cnt = 0
    _min = min(row)
    cnt += _min
    row2 = [i - _min for i in row]

    res = [[]]
    for e in row2:
        if e != 0:
            res[-1].append(e)
        else:
            res.append([])

    return cnt, res


def mizuyari(ll):
    cnt = 0

    for l in ll:
        if l:
            cnt2, hs = mizuyari2(l)
            # print(cnt2, hs)
            cnt += cnt2
            cnt += mizuyari(hs)
    return cnt


def main2():
    n = int(input())
    hs = [int(i) for i in input().split()]
    hs = [hs]
    cnt = mizuyari(hs)
    print(cnt)


if __name__ == '__main__':
    main2()
