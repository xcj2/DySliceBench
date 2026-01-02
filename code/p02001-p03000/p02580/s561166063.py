from collections import Counter
from itertools import groupby


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def ilen(ll):
    return sum(1 for _ in ll)


def solve():
    H, W, M = read_ints()
    hw = []
    for _ in range(M):
        hw.append(tuple(read_ints()))
    hw.sort()

    rows = set()
    max_count_row = 0
    for h, ws in groupby(hw, key=lambda pair: pair[0]):
        count = ilen(ws)
        if count == max_count_row:
            rows.add(h)
        elif count > max_count_row:
            rows = set([h])
            max_count_row = count

    hw.sort(key=lambda pair: pair[1])
    cols = set()
    max_count_col = 0
    for w, hs in groupby(hw, key=lambda pair: pair[1]):
        count = ilen(hs)
        if count == max_count_col:
            cols.add(w)
        elif count > max_count_col:
            cols = set([w])
            max_count_col = count

    hw = set(hw)
    for h in rows:
        for w in cols:
            if (h, w) not in hw:
                return max_count_row+max_count_col
    return max_count_row+max_count_col-1


if __name__ == '__main__':
    print(solve())
