from collections import defaultdict


def read_input():
    l, r = map(int, input().split())
    return l, r


def candidates():
    cand = defaultdict(list)
    for i in range(1, 2019):
        for j in range(i + 1, 2019):
            cand[(i*j) % 2019].append((i, j))

    return cand


def check_in_range(l, r, x):
    if r - l > 2019:
        return True

    base = (l // 2019) * 2019

    test = base + x
    while base <= r:
        if l <= test <= r:
            return True
        base += 2019
        test = base + x

    return False


def submit():
    l, r = read_input()

    cands = candidates()
    for i in range(2019):
        cand = cands[i]

        for c in cand:
            if check_in_range(l, r, c[0]) and check_in_range(l, r, c[1]):
                print(i)
                return







if __name__ == '__main__':
    submit()
