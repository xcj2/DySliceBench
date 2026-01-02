#■標準入力ショートカット


def get_next_int():
    return int(float(input()))


def get_next_ints(delim=" "):
    return tuple([int(float(x)) for x in input().split(delim)])


def get_next_str():
    return input()


def get_next_strs(delim=" "):
    return tuple(input().split(delim))


def get_next_by_types(*value_types, delim=" "):
    return tuple([t(x) for t, x in zip(value_types, input().split(delim))])


def solve():
    N = get_next_int()
    positions = get_next_ints()

    diffs = [0 for i in range(N)]
    dist = 0
    prev_pos = 0
    for i, pos in enumerate(positions):
        dist += abs(pos - prev_pos)

        next_pos = positions[i + 1] if i + 1 < N else 0
        if prev_pos <= pos <= next_pos or prev_pos >= pos >= next_pos:
            diff = 0
        else:
            diff = min(abs(next_pos - pos), abs(prev_pos - pos)) * 2
        diffs[i] = diff
        prev_pos = pos
    dist += abs(prev_pos)
    # print(dist)
    # print(diffs)
    for diff in diffs:
        print(dist - diff)


solve()