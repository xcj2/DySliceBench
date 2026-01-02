from sys import stdin
from itertools import permutations 


def get_time(nums):
    time = 0
    for i, n in enumerate(nums):
        time = time + n
        if i < len(nums) - 1 and time % 10 != 0:
            time = time + (10 - time % 10)
    return time


def solve(nums):
    min_time = 0
    for p in permutations(nums, len(nums)):
        t = get_time(p)
        if min_time > t or min_time == 0:
            min_time = t
    return min_time

def main():
    nums = [int(l) for l in stdin.readlines()]
    ans = solve(nums)
    print(ans)

if __name__ == '__main__':
    main()