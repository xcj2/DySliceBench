#  --*-coding:utf-8-*--

import bisect

def f(n, aVals, bVals, cVals):
    #     return len(ys)*len(xs) - sum(bisect.bisect_left(ys, x) for x in xs

    bVals = sorted(bVals)
    cVals = sorted(cVals)

    xs = [0]*(n+1)
    x = 0
    for i in range(n-1, -1, -1):
        x += n - bisect.bisect_right(cVals, bVals[i])
        xs[i] = x

    return sum(xs[bisect.bisect_right(bVals, a)]
               for a in aVals)


def test():
    assert f(2, [1, 5], [2, 4], [3, 6]) == 3
    assert f(3, [1, 1, 1], [2, 2, 2], [3, 3, 3]) == 27
    assert f(6, [3, 14, 159, 2, 6, 53],
             [58, 9, 79, 323, 84, 6],
             [2643, 383, 2, 79, 50, 288]) == 87


def main():
    n = int(input())
    aVals = list(map(int, input().split()))
    bVals = list(map(int, input().split()))
    cVals = list(map(int, input().split()))

    print(f(n, aVals, bVals, cVals))


if __name__ == '__main__':
    main()
