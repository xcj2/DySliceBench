# -*- coding: utf-8 -*-

##
## B - Frog2
## https://atcoder.jp/contests/dp/tasks/dp_b
##

import sys

def solve(N, K, nums):
    assert N > 0
    if N == 1:
        return 0
    costs = []; add = costs.append
    add(0)
    add(abs(nums[1] - nums[0]))
    #for i in range(2, min(K, N)):
    #    c = min( costs[j] + abs(nums[i] - nums[j]) for j in range(0, i) )
    #    costs.append(c)
    #for i in range(K, N):
    #    c = min( costs[j] + abs(nums[i] - nums[j]) for j in range(i-K, i) )
    #    costs.append(c)
    for i in range(2, N):
        c = min( costs[j] + abs(nums[i] - nums[j])
                     for j in range(max(i-K, 0), i) )
        add(c)
    return costs[-1]

def load(input):
    line = input.readline()
    N, K = [ int(s) for s in line.split() ]
    nums = [ int(s) for s in input.read().split() ]
    return N, K, nums

def main():
    N, K, nums = load(sys.stdin)
    result = solve(N, K, nums)
    print(result)

main()
