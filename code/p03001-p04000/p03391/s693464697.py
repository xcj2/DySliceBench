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
    A, B = [], []
    diff_progression = False
    min_B = float('INF')
    for i in range(N):
        a, b = get_next_ints()
        A.append(a)
        B.append(b)
        if a != b:
            diff_progression = True
        if a > b:
            min_B = min(min_B, b)
    if not diff_progression:
        print(0)
    else:
        ans = sum(A) - min_B
        print(ans)

solve()