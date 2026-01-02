import collections
import math
import operator as op
from functools import reduce
from collections import Counter
import numpy as np
import math
import bisect
import heapq


MOD = 1000000007


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def get_inputs(cast_func=None):
    if cast_func is None:
        return input().split()
    else:
        return list(map(cast_func, input().split()))


def get_input(cast_func=None):
    if cast_func is None:
        return input()
    else:
        return cast_func(input())


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def main():
    K = get_input(int)

    Lun = [None for _ in range(10)]
    for n in range(10):
        Lun[n] = [[] for _ in range(11)]
    for n in range(10):
        Lun[n][1].append(n)
    # print(Lun)

    for d in range(2, 11):
        for n in range(10):
            o = n*10**(d-1) 
            for i in [n-1, n, n+1]:
                if i >= 0 and i <= 9:
                    Lun[n][d].extend([l + o for l in Lun[i][d-1]])

    flag = True
    cnt = K
    for d in range(1, 11):
        for n in range(1, 10):
            if cnt - len(Lun[n][d]) <= 0:
                flag = False
                break
            else:
                cnt -= len(Lun[n][d])
        if not flag:
            break
    # print(n, d, cnt)
    # print(Lun[n][d])
    print(Lun[n][d][cnt-1])


    # Lun = np.zeros((10, 11), dtype=np.int64)
    # Lun[:, 1] = 1
    # for d in range(2, 11):
    #     for n in range(10):
    #         for i in [n-1, n, n+1]:
    #             if i >= 0 and i <= 9:
    #                 Lun[n, d] += Lun[i, d-1]





    # flag = True
    # cnt = K
    # for d in range(1, 11):
    #     for n in range(1, 10):
    #         if cnt - Lun[n, d] <= 0:
    #             flag = False
    #             break
    #         else:
    #             cnt -= Lun[n, d]
    #     if not flag:
    #         break
    # print(n, d, cnt)

    # ans = ""
    # cnt = K
    # flag = True
    # for d in range(1, 11):
    #     for n in range(1, 10):
    #         if cnt - Lun[n, d] <= 0:
    #             flag = False
    #             break
    #         else:
    #             cnt -= Lun[n, d]
    #     if not flag:
    #         break
    
    # ans = [None for _ in range(d)]
    # ans[0] = n

    # for _d in range(d-1, 0, -1):
    #     for n in range(1, 10):
    #         if 
    #         if cnt - Lun[n, d] <= 0:
    #             flag = False
    #             break
    #         else:
    #             cnt -= Lun[n, d]
    #     if not flag:
    #         break
 


if __name__ == '__main__':
    main()
