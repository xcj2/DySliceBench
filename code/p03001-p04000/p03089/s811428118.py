def getN():
    return int(input())

def getlist():
    return [(int(x), i) for i, x in enumerate(input().split())]

n = getN()
nums = getlist()
nums.reverse()

buffer = []
tmp = 0
used = {}

def insertcheck(n, k):
    if sum(mask[:k]) < n-1:
        return False

    return True

ans = []
mask = [0 for i in range(n)]
flag = 1


def search(nums):
    for num in nums:
        val, idx = num
        if mask[num[1]] == 0:
            if insertcheck(val, idx):
                ans.append((val,idx))
                used[num[0]] = num[1]
                mask[num[1]] = 1
                return 1

    return 0

while(flag):
    flag = search(nums)

if len(ans) != n:
    ans = [(-1, -1)]

for an in ans:
    print(an[0])


"""
9
1 1 1 2 2 1 2 4 2
"""