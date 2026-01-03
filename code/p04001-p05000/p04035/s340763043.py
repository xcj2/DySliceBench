import re

class IO_for_Contest(object):
    @staticmethod
    def my_input():
        #return raw_input()
        return input()

    @staticmethod
    def read_from_input():
        n, l = IO_for_Contest.read_n_int(2)
        a = IO_for_Contest.read_n_int(n)
        return l, a

    @staticmethod
    def read_line():
        return IO_for_Contest.my_input().strip()

    @staticmethod
    def read_int():
        return int(IO_for_Contest.my_input().strip())

    @staticmethod
    def read_n_int(n):
        return list(map(int, re.split('\W+', IO_for_Contest.my_input().strip())))[ : n]


def solve():
    l, a = IO_for_Contest.read_from_input()
    result = find_way_how_to_split_ropes(l, a)
    if result is None:
        print('Impossible')
    else:
        print('Possible')
        for x in result:
            print(x)

def find_way_how_to_split_ropes(l, a):
    adjencent_sum = []
    for i in range(len(a) - 1):
        adjencent_sum.append(a[i] + a[i + 1])
    if max(adjencent_sum) < l:
        return None
    x = 0
    result = []
    for y in range(len(adjencent_sum)):
        if adjencent_sum[y] >= l:
            x = y + 1
            break
        result += [y + 1]
    for y in range(len(adjencent_sum) - 1, x - 1, -1):
        result += [y + 1]
    result += [x]
    return result

if __name__ == '__main__':
    solve()