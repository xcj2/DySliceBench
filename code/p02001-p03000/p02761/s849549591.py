import sys
INF = float("inf")


def solve(N: int, M: int, s: "List[int]", c: "List[int]"):

    for i in range(1000):
        A = str(i)
        if len(A) != N:
            continue
        flag = True
        for ss, cc in zip(s, c):
            if int(A[ss-1]) != cc:
                flag = False
                break

        if flag == True:
            print(A)
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
    M = int(next(tokens))  # type: int
    s = [int()] * (M)  # type: "List[int]"
    c = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        s[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(N, M, s, c)


if __name__ == '__main__':
    main()
