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
    N, amount = get_next_ints()

    made_amount = 0
    donuts = []
    min_donut = float('inf')
    for _ in range(N):
        donut = get_next_int()
        donuts.append(donut)
        min_donut = min(min_donut, donut)

    remain = amount - sum(donuts)
    made_amount += N
    made_amount += int(remain / min_donut)
    print(made_amount)





solve()