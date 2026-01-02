import bisect


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
    N, M, X = get_next_ints()
    costs = get_next_ints()
    costs = sorted(costs)
    x_index = bisect.bisect(costs, X)
    left_cost = len(costs[0:x_index])
    right_cost = len(costs[x_index:])
    if left_cost < right_cost:
        print(left_cost)
    else:
        print(right_cost)
solve()