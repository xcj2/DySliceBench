import sys

YES = "Yes"
NO = "No"


def solve(N: int, H: "List[int]"):
    hmax = H[0]
    for h in H:
        if h <= hmax - 2:
            return NO
        hmax = max(hmax, h)
    return YES


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    H = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    ans = solve(N, H)
    if ans is not None:
        print(ans)


if __name__ == '__main__':
    main()
