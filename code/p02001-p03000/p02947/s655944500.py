import sys
from math import factorial

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    string_type = {}
    for s in inputs:
        count = {}
        s_list = list(s)
        s_list.sort()
        for c in s_list:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        key = ""
        for k in count.keys():
            key += "{}{}".format(k, count[k])
        if key in string_type:
            string_type[key] += 1
        else:
            string_type[key] = 1

    comb_count = 0
    for v in string_type.values():
        if v != 1:
            if v == 2:
                comb_count += 1
            else:
                comb_count += factorial(v) // factorial(v-2) // factorial(2)
    return comb_count


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    N = int(input())
    ret = solve(inputs(N))
    print(ret)
