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
    A, B, C, X, Y = get_next_ints()

    proper = (A * X) + B * Y
    if X > Y:
        smaller = Y
        remainder = X - Y
        value = A
    else:
        smaller = X
        remainder = Y - X
        value = B
    mixed = C * smaller * 2 + min(remainder * value, remainder * C * 2)

    print(min(proper, mixed))


solve()