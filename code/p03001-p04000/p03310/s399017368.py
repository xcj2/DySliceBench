#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, A: "List[int]"):
    s = sum(A)
    cums = [0]
    for v in A:
        cums.append(cums[-1] + v)

    ret = float('inf')
    i, j, k = 1, 2, 3
    while j < N - 1:
        lm = cums[j]
        while i < j - 1 and cums[i] < lm // 2:
            i += 1
        if i > 2 and abs(lm - 2 * cums[i]) > abs(lm - 2 * cums[i - 1]):
            i -= 1

        rm = cums[N] - cums[j]
        while k < N - 1 and cums[k] - cums[j] < rm // 2:
            k += 1
        if k > j + 1 and abs(rm - 2 * (cums[k] - cums[j])) > abs(rm - 2 * (cums[k - 1] - cums[j])):
            k -= 1

        a, b, c, d = cums[i], cums[j] - cums[i], cums[k] - cums[j], cums[N] - cums[k]
        tmp = max(a, b, c, d) - min(a, b, c, d)
        #print(tmp, i, j, k, ':', a, b, c, d, '\n')
        ret = min(ret, tmp)
        j += 1
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
