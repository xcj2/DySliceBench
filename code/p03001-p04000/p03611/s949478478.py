# encoding: "utf-8"

from collections import defaultdict
from functools import reduce
from itertools import groupby, chain

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
    ys = chain.from_iterable([[x-1, x, x+1] for x in xs])
    ys = sorted(list(ys))
    m = max(map(len, group(ys)))
    print(m)

def group(xs):
    result = list()
    prev = xs[0]
    temp = list()
    for x in xs:
        if x == prev:
            temp.append(x)
        else:
            result.append(temp)
            prev = x
            temp = [x]
    return result

if __name__ == "__main__":
    main()