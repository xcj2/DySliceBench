def getN():
    return int(input())

def getMN():
    a = input().split()
    b = [int(i) for i in a]
    return b[0],b[1]

def getlist():
    a = input().split()
    b = [int(i) for i in a]
    return b

from collections import defaultdict

n, t = getMN()
nums = getlist()
ans = defaultdict(int)
cur = nums[0]
upper = cur
profits = defaultdict(int)
n_low = 1
n_up = 1

for num in nums[1:]:
    if cur > num:
        profits[upper-cur] += min(n_low, n_up)
        cur = num
        n_low = 1
        n_up = 1
        upper = cur
    elif cur == num:
        n_low += 1
    elif num == upper:
        n_up += 1
    elif num > upper:
        upper = num
        n_up = 1
profits[upper-cur] += min(n_low, n_up)

maxkey = max(profits.keys())
print(profits[maxkey])