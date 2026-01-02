import sys
from collections import Counter


def solve(N: int, s: "List[str]"):
    c = Counter()
    for x in s:
        c["".join(sorted(x))] += 1
    ans = 0
    for i in c.values():
        ans += i * (i - 1) // 2
    return ans


# -----------------------------------------------------------------------------
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()

    N = int(next(tokens))  # type: int
    s = [next(tokens) for _ in range(N)]  # type: "List[str]"

    ans = solve(N, s)
    if ans is not None:
        print(ans)


if __name__ == '__main__':
    main()
