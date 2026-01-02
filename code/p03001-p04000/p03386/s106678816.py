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
    A, B, K = get_next_ints()
    if K > B - A:
        for i in range(A, B + 1):
            print(i)
    else:
        ans = list(range(A, A + K))

        ans_b = list(range(B - K + 1, B + 1))
        for i in ans:
            print(i)
        for j in ans_b:
            if not j in (ans):
                print(j)
solve()