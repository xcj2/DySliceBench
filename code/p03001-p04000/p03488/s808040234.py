def parse(s):
    first_val = None
    verticals, horizontals = list(), list()
    seq = 0
    is_horizontal = True
    is_first = True
    for c in s:
        if c == 'T':
            if is_first:
                first_val = seq
                is_first = False
            elif is_horizontal:
                horizontals.append(seq)
            else:
                verticals.append(seq)
            is_horizontal = not is_horizontal
            seq = 0
        else:
            seq += 1
    if seq > 0:
        if is_first:
            first_val = seq
        elif is_horizontal:
            horizontals.append(seq)
        else:
            verticals.append(seq)
    return first_val, verticals, horizontals


def check(vals, target):
    val_set = {0}
    for v in vals:
        tmp_set = set()
        for sv in val_set:
            tmp_set.add(sv + v)
            tmp_set.add(sv - v)
        val_set = tmp_set
    return target in val_set


def main():
    S = input()
    X, Y = list(map(int, input().split(' ')))
    fv, vs, hs = parse(S)
    if check(hs, X - fv) and check(vs, Y):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
