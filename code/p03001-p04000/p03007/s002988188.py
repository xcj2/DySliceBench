def getN():
    return int(input())

def getMN():
    return list(map(int, input().split()))

def getlist():
    return list(map(int, input().split()))
import sys

n = getN()
nums = getlist()
nums.sort()

from bisect import bisect_left
insert = bisect_left(nums, 0)


if insert == 0:
    print(sum(nums) - 2 * nums[0])
    tmp = nums[0]
    for num in nums[1:-1]:
        print(tmp, num)
        tmp = tmp - num
    print(nums[-1], tmp)
    sys.exit()

if insert == len(nums):
    nums.sort(reverse=True)
    print(abs(sum(nums)) + 2 * nums[0])
    tmp = nums[0]
    for num in nums[1:]:
        print(tmp, num)
        tmp = tmp - num
    sys.exit()

neg = nums[:insert]
pos = nums[insert:]
neg_end = neg[0]
pos_end = pos[-1]
print(abs(sum(neg)) + sum(pos))
for ne in neg[1:]:
    print(pos_end, ne)
    pos_end -= ne

for po in pos[:-1]:
    print(neg_end, po)
    neg_end -= po

print(pos_end, neg_end)




"""
5
8 9 -2 -3 10
"""
