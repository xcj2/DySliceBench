import re


class IO_for_Contest(object):
    @staticmethod
    def my_input():
        # return raw_input()
        return input()

    @staticmethod
    def read_from_input():
        n, k = IO_for_Contest.read_n_int(2)
        return n, IO_for_Contest.read_n_int(k)

    @staticmethod
    def read_line():
        return IO_for_Contest.my_input().strip()

    @staticmethod
    def read_int():
        return int(IO_for_Contest.my_input().strip())

    @staticmethod
    def read_n_int(n):
        return list(map(
            int,
            re.split('\s+', IO_for_Contest.my_input().strip())))[: n]


def solve():
    n, d = IO_for_Contest.read_from_input()
    print(min_value_can_pay(n, d))


def min_value_can_pay(n, d):
    ints_can_be_used = think_ints_can_be_used(d)
    queue = []
    for i in ints_can_be_used:
        queue.append(i)
    while len(queue) > 0:
        j = queue.pop(0)
        if j >= n:
            return j
        if j == 0:
            continue
        for i in ints_can_be_used:
            queue.append(j * 10 + i)


def think_ints_can_be_used(d):
    ints = list(range(10))
    for i in d:
        ints.remove(i)
    return ints

if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    solve()