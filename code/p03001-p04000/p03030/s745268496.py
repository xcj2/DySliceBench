import sys


def solve(N: int, S: "List[str]", P: "List[int]"):
    data = list(zip(S, map(lambda x: -x, P), range(1, N + 1)))
    data.sort()
    return "\n".join(str(t[2]) for t in data)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [str()] * (N)  # type: "List[str]"
    P = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        S[i] = next(tokens)
        P[i] = int(next(tokens))
    ans = solve(N, S, P)
    if ans is not None:
        print(ans)

if __name__ == "__main__":
    main()
