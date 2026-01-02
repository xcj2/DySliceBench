# encoding: "utf-8"

from collections import defaultdict

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


def count_and_del(xs):
    cnt = 0
    fst = xs[-1]
    for x in reversed(xs):
        if x != fst:
            break
        cnt += 1
    del xs[-cnt:]
    return cnt   


def main():
    _ = input()
    xs = Stdin.read_line(converter=int)
    xs.sort(reverse=True)
    ys = defaultdict(int)
    while xs:
        key = xs[-1]
        cnt = count_and_del(xs)
        ys[key] += cnt
        ys[key-1] += cnt
        ys[key+1] += cnt

    print(max(ys.values()))


if __name__ == "__main__":
    main()