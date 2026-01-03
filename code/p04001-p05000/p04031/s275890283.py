import re
import doctest
import functools

class IO_for_Contest(object):
    @staticmethod
    def my_input():
        #return raw_input()
        return input()

    @staticmethod
    def read_from_input():
        n = IO_for_Contest.read_int()
        return IO_for_Contest.read_n_int(n)

    @staticmethod
    def read_line():
        return IO_for_Contest.my_input().strip()

    @staticmethod
    def read_int():
        return int(IO_for_Contest.my_input().strip())

    @staticmethod
    def read_n_int(n):
        return list(map( \
                int, \
                re.split('\s+', IO_for_Contest.my_input().strip())))[ : n]
def solve():
    a = IO_for_Contest.read_from_input()
    print(think_min_cost_for(a))

def think_min_cost_for(arr):
    """
    >>> think_min_cost_for([4, 8])
    8
    """
    ceil = 100
    floor = -100
    cost = []
    for to in range(floor, ceil + 1):
        cost.append(think_min_cost_about(arr, to))
    return min(cost)

def think_min_cost_about(arr, to):
    diff = list(map(lambda x: x - to, arr))
    diff_2 = list(map(lambda x: x ** 2, diff))
    return sum(diff_2)

if __name__ == '__main__':
    #doctest.testmod()
    solve()