# encoding: "utf-8"

from collections import defaultdict
from functools import reduce
from itertools import groupby

class Stdin:
    @staticmethod
    def read_line(converter=str):
        return [converter(x) for x in input().split()]
    
    @staticmethod
    def read_lines(n, converter=str):
        result = list()
        for _ in range(n):
            result.append(Stdin.read_line(converter))
        return result
    
    @staticmethod
    def convert(data, converter):
        assert(len(data) == len(converter))
        return tuple(map(lambda x, f: f(x), data, converter))

    @staticmethod
    def convert_lines(datas, n, converter):
        return [converter(data, n, converter) for data in datas]


def main():
    _ = input()
    xs = Stdin.read_line(converter=int)
    # print(xs)
    ys = concat_map(xs, lambda x: [x, x+1, x-1])
    ys.sort()
    print(max(map(lambda x: count(x[1]), groupby(ys))))

def concat_map(xs, f):
    return reduce(lambda accum, x: extended(accum, x), map(f, xs))

def extended(xss, xs):
    xss.extend(xs)
    return xss

def count(iterator):
    cnt = 0
    for _ in iterator:
        cnt += 1
    return cnt

if __name__ == "__main__":
    main()