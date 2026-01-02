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
    ans = 0
    for i in range(N):
        l, r = get_next_ints()
        ans += r-l+1
    print(ans)
solve()