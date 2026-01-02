import sys
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    N_STR = inputs[0]
    N = int(N_STR)

    if len(N_STR) <= 2:
        return 0

    def check_over(string):
        if int(string) > N:
            return False
        return True

    def check_all_appered(string):
        does_appered = {
            '3': False,
            '5': False,
            '7': False
        }

        for s in string:
            if s in does_appered:
                does_appered[s] = True
        are_all_true = True
        for d in does_appered.values():
            are_all_true = are_all_true and d
        return are_all_true

    def create_s(origin, until_len):
        if len(origin) == until_len:
            return [origin]

        ret = []
        ret += create_s(origin+'3', until_len)
        ret += create_s(origin+'5', until_len)
        ret += create_s(origin+'7', until_len)

        pop_items = []
        for i in range(0, len(ret)):
            if ret[i] is None \
                    or not check_all_appered(ret[i]) \
                    or not check_over(ret[i]):
                pop_items.append(i)
        for p in reversed(pop_items):
            ret.pop(p)

        return ret

    ret = []
    for i in range(3, len(N_STR)+1):
        ret += create_s('', i)
    return len(ret)


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
