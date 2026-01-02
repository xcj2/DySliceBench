#!/usr/bin/env python3
import sys


def solve(N: int, s: "List[str]"):

    result = 0
    str_dict = dict()
    for s_i in s:

        s_i = list(s_i)
        s_i.sort()
        s_i = "".join(s_i)

        if s_i in str_dict:
            result += str_dict[s_i]
            str_dict[s_i] += 1
        else:
            str_dict[s_i] = 1

    print(result)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    s = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, s)


if __name__ == "__main__":
    main()
