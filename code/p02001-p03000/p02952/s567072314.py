import sys


def solve(N: int):
    if 1 <= N <= 9:
        return N
    if 10 <= N <= 99:
        return 9
    if 100 <= N <= 999:
        return 9 + N - 99
    if 1000 <= N <= 9999:
        return 9 + 900
    if 10000 <= N <= 99999:
        return 9 + 900 + N - 9999
    else:
        return 9 + 900 + 90000



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    ans = solve(N)
    if ans is not None:
        print(ans)


if __name__ == '__main__':
    main()
