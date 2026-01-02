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
    N = get_next_int()
    X = get_next_ints()

    x_sorted = sorted(X)
    med_index = int((N-1)/2)
    # print(med_index, x_sorted)
    for num in X:
        index = bisect.bisect(x_sorted, num)-1
        if index > med_index:
            print(x_sorted[med_index])
        else:
            print(x_sorted[med_index+1])



solve()