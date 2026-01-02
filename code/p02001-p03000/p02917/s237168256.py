def solve(inp):
    N = int(inp.readline().strip())
    B = list(map(int, inp.readline().strip().split(' ')))

    A = [0 for i in range(N)]

    A[N - 1] = B[N - 2]
    for i in range(N - 2, 0, -1):
        A[i] = min(B[i - 1], B[i])
    A[0] = B[0]
    # print(A)

    return str(sum(A))


def test(s):
    from io import StringIO
    print(solve(StringIO(s)))


def main():
    import sys
    result = solve(sys.stdin)
    if result:
        print(result)


if __name__ == '__main__':
    # test('3\n2 5')
    # test('2\n3')
    # test('6\n0 153 10 10 23')
    main()
