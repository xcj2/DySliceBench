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
    A, B, C = get_next_ints()
    parity = (A % 2 + B % 2 + C % 2)
    ans = 0
    if parity == 1:
        A += 1 if A % 2 == 0 else 0
        B += 1 if B % 2 == 0 else 0
        C += 1 if C % 2 == 0 else 0
        ans += 1
    if parity == 2:
        A += 1 if A % 2 != 0 else 0
        B += 1 if B % 2 != 0 else 0
        C += 1 if C % 2 != 0 else 0
        ans += 1
    max_val = max(A, B, C)
    ans += int((max_val - A) / 2 + (max_val - B) / 2 + (max_val - C) / 2)
    print(ans)

solve()