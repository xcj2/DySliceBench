from sys import stdin
from collections import defaultdict
readline = stdin.readline
read = stdin.buffer.read
def r_map(): return map(int, readline().rstrip().split())
def r_list(): return list(r_map())

MOD = 10 ** 9 + 7
# import numpy as np
# from numba import jit
# stdin = open('sample.txt')

def main():
    N = int(readline().rstrip())
    A = r_list()
    A.sort()
    ans = 0
    a_dic = defaultdict(lambda: 0)
    for j, a in enumerate(A[:0:-1]):
        i = N - 2 - j
        a_dic[i] += a
        if i > 0:
            a_dic[i - 1] = a_dic[i]
    for i, a in enumerate(A[:-1]):
        ans += a * a_dic[i]
    print(ans % MOD)

if __name__ == "__main__":
    main()
