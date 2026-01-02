# encoding: "utf-8"

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
    x, t = Stdin.read_line(converter=int)
    r = x - t
    if r < 0:
        r = 0
    print(r)

if __name__ == "__main__":
    main()