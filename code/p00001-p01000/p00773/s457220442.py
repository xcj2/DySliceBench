import sys


from inspect import currentframe


def debug_print(s):
    # print(s)
    return 


def debug_key(*args):
    names = {id(v): k for k, v in currentframe().f_back.f_locals.items()}
    debug_print(', '.join(names.get(id(arg), '???')+' = '+repr(arg) for arg in args))


def solve(x, y, s):
    debug_print("\n-----solve-----")
    ans = 0
    for first in range(1, s // 2 + 1):
        second = s - first
        first_nuki = (first + 1) / (x + 100) * 100
        second_nuki = (second + 1) / (x + 100) * 100

        if first_nuki.is_integer():
            first_nuki -= 1
        else:
            first_nuki = int(first_nuki)

        if second_nuki.is_integer():
            second_nuki -= 1
        else:
            second_nuki = int(second_nuki)

        if (int((first_nuki * (100 + x)) / 100) + int((second_nuki * (100 + x)) / 100)) != s:

            continue

        sum_y = int((first_nuki * (100 + y)) / 100) + int((second_nuki * (100 + y)) / 100)
        ans = max(ans, sum_y)

        # debug_key(sum_y)
        # debug_key(first_nuki)
        # debug_key(second_nuki)
        # debug_key((first_nuki * (100 + y)) // 100)
        # debug_key((second_nuki * (100 + y)) // 100)
        # debug((first_nuki * (100 + y)) // 100 + (second_nuki * (100 + y)) // 100)

    print(ans)
    return


if __name__ == '__main__':

    # a = [int(input()) for _ in range(244)]
    # b = [int(input()) for _ in range(244)]
    #
    # if a == b:
    #     debug("ok")
    # else:
    #     debug("(●・▽・●)")

    while True:
        x_input, y_input, s_input = map(int, input().split())
        # a += 1
        if x_input == y_input == s_input == 0:
            break

        solve(x_input, y_input, s_input)


