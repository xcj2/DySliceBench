#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, s: str):

    for SW in [[1, 1], [0, 1], [0, 0], [1, 0]]:
        for c in s[1:]:
            if SW[-1] == 1:
                if c == 'o':
                    SW.append(SW[-2])
                else:
                    SW.append(1-SW[-2])
            else:
                if c == 'o':
                    SW.append(1-SW[-2])
                else:
                    SW.append(SW[-2])
        if SW[0] == SW[-1]:
            if ((SW[0] == 1) and (s[0] == 'o') and (SW[-2] == SW[1]))\
               or ((SW[0] == 1) and (s[0] == 'x') and (SW[-2] != SW[1]))\
               or ((SW[0] == 0) and (s[0] == 'o') and (SW[-2] != SW[1]))\
               or ((SW[0] == 0) and (s[0] == 'x') and (SW[-2] == SW[1])):
                print("".join("WS"[sw] for sw in SW[:-1]))
                return

    print(-1)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    s = next(tokens)  # type: str
    solve(N, s)


if __name__ == '__main__':
    main()
