import sys
from itertools import accumulate
import math
import bisect


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if not arr:
        arr.append([n, 1])

    return arr


def solve(n):
    if n == 1:
        return 0
    ans = 0
    acc = list(accumulate(list(range(int(math.log2(n) + 2)))))
    arr = factorization(n)
    for e in arr:
        ans += bisect.bisect_right(acc, e[1]) - 1
    return ans


def main():
    input = sys.stdin.buffer.readline
    n = int(input())

    print(solve(n))


if __name__ == '__main__':
    main()
