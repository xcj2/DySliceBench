def solve(inp):
    N = int(inp.readline().strip())
    A = list(map(int, inp.readline().strip().split(' ')))
    B = list(map(int, inp.readline().strip().split(' ')))
    C = list(map(int, inp.readline().strip().split(' ')))

    r = sum(B)
    for i in range(N - 1):
        if A[i] + 1 == A[i + 1]:
            r += C[A[i] - 1]
    return str(r)


def test(s):
    from io import StringIO
    print(solve(StringIO(s)))


def main():
    import sys
    result = solve(sys.stdin)
    if result:
        print(result)


if __name__ == '__main__':
    # test('')
    main()