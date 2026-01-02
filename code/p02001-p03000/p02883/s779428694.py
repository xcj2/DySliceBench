import sys
import numpy as np

readline = sys.stdin.buffer.readline

N, K = map(int, readline().split())
A = np.array(list(map(int, readline().split())))
F = np.array(list(map(int, readline().split())))

A = np.sort(A)[::-1]
F = np.sort(F)


def binary_search(min_n, max_n):

    while max_n - min_n != 1:
        tn = (min_n + max_n) // 2
        if judge(tn):
            max_n = tn
        else:
            min_n = tn

    return max_n


def judge(tn):

    k = 0
    if np.maximum(0, A - tn // F).sum() <= K:
        return True
    else:
        return False


def solve():

    ans = binary_search(-1, 10**12)
    print(ans)


if __name__ == '__main__':
    solve()
