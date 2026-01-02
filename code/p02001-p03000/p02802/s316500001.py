def get_next_ints(delim=" "):
    return tuple([int(float(x)) for x in input().split(delim)])


def get_next_by_types(*value_types, delim=" "):
    return tuple(
        [t(x) for t, x in zip(value_types, input().rstrip("\n").split(delim))])


def main():
    n, m = get_next_ints()
    ac_count = 0
    wa_count = 0

    from collections import defaultdict
    ac_cache = defaultdict(int)
    wa_cache = defaultdict(int)
    ac_count = 0
    wa_count = 0
    wa = 0
    for i in range(m):

        p, result = get_next_by_types(int, str)

        if ac_cache[p] == 0:
            if result == 'AC':

                ac_cache[p] = 1
                ac_count += 1
                wa_count += wa_cache[p]
                wa = 0
            else:
                wa_cache[p] += 1
    print(ac_count, wa_count)


if __name__ == '__main__':
    main()
if __name__ == '__jupyter__':
    import doctest
    print(doctest.testmod())