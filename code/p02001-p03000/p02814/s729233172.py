# -*- coding: utf-8 -*-
import sys

N, M = map(int, input().split())
a_list = list(map(int, input().split()))

# lcm & gcd not math
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(x, y):
    return (x * y) // gcd(x, y)

from functools import reduce
def lcm_multi(num_list):
    return reduce(lcm, num_list, 1)

# number of being able to divide by 2 in all of list
def get_num_can_divide_two(num_list):
    bin_num_or = 0
    for now_num in num_list:
        bin_num_or |= now_num

    num_can_divide_two = 0
    while bin_num_or > 0:
        can_divede_two = bin_num_or & 1
        if can_divede_two:
            break
        bin_num_or >>= 1
        num_can_divide_two += 1

    return(num_can_divide_two)

num_can_divide_two = get_num_can_divide_two(a_list)

for i in range(N):
    if (a_list[i] // (2 ** num_can_divide_two)) % 2 == 0:
        print(0)
        sys.exit()
        

lcm_num =  lcm_multi(a_list)

print((M - lcm_num // 2) // lcm_num + 1)