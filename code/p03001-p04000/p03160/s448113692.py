# -*- coding: utf-8 -*-

##
## A - Frog1
## https://atcoder.jp/contests/dp/tasks/dp_a
##

import sys

def solve(N, nums):
    assert N > 0
    if N == 1:
        return 0
    cost_2 = 0
    cost_1 = abs(nums[1] - nums[0])
    for i in range(2, N):
        c1 = cost_1 + abs(nums[i] - nums[i-1])
        c2 = cost_2 + abs(nums[i] - nums[i-2])
        cost_i = min(c1, c2)
        cost_2 = cost_1
        cost_1 = cost_i
    return cost_1

def load(input):
    line = input.readline()
    N = int(line.strip())
    #buf = []; add = buf.append
    #size = 2**16
    #s = input.read(size)
    #while s:
    #    add(s)
    #    s = input.read(size)
    #return N, "".join(buf)
    return N, input.read()

def main():
    N, string = load(sys.stdin)
    nums = [ int(x) for x in string.split() ]
    result = solve(N, nums)
    print(result)

main()
