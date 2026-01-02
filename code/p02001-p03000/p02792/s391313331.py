import sys


def solve(inp):
    N = int(inp.readline().strip())

    nums = [[0 for i in range(11)] for i in range(11)]

    for s in range(1, 10):
        for e in range(0, 10):
            n = 0
            # print('--- {} {}'.format(s, e))
            if s == e and s <= N:
                # 1けた
                n += 1
            for d in (10, 100, 1000, 10000, 100000, 1000000):
                start = end = s * d + e
                if start > 200000:
                    continue
                d2 = int(d / 10)
                while d2 >= 10:
                    end += 9 * d2
                    d2 = int(d2 / 10)
                end = min(end, 200000)
                # print('{} {}'.format(start, end))
                if end <= N:
                    n += int(d / 10)
                else:
                    j = start
                    while j <= N:
                        n += 1
                        j += 10
            # print('  --> {}'.format(n))
            # print()
            nums[s][e] = n

    r = 0
    for s in range(1, N + 1):
        if s % 10 != 0:
            r += nums[s % 10][int(str(s)[0])]

    return str(r)


def solve1(inp):
    N = int(inp.readline().strip())

    r = 0
    for i in range(1, N + 1):
        first = int(str(i)[0])
        last = i % 10
        for j in range(1, N + 1):
            if int(str(j)[0]) == last and j % 10 == first:
                r += 1

    return str(r)


def main():
    result = solve(sys.stdin)
    if result:
        print(result)


if __name__ == '__main__':
    main()
