import sys


def solve(K: int, X: int):
    s = X - (K - 1)
    e = X + (K - 1)
    ans = []
    for i in range(2000001):
        x = i - 1000000
        if s <= x <= e:
            ans.append(str(x))
    return " ".join(ans)
        


# -----------------------------------------------------------------------------
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()

    K = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int

    ans = solve(K, X)
    if ans is not None:
        print(ans)


if __name__ == '__main__':
    main()
