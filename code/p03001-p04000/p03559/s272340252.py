from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt
from collections import deque
from bisect import bisect, bisect_left, bisect_right
INF = float("inf")

from bisect import bisect, bisect_left, bisect_right



# Find rightmost value less than x
def find_lt(a, x):
    i = bisect_left(a, x)
    if i:
        return i
    return 0


# Find leftmost value greater than x'
def find_gt(a, x):
    i = bisect_right(a, x)
    if i != len(a):
        return i
    return len(a)


def main():
    N = int(input())
    A = list(sorted(list(map(int, input().split()))))
    B = list(sorted(list(map(int, input().split()))))
    C = list(sorted(list(map(int, input().split()))))

    ans = 0
    for b in B:
        a = find_lt(A, b)
        b = N - find_gt(C, b)
        ans += a * b
    print(ans)


if __name__ == '__main__':
    main()
