import sys
import math
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

def check_t(num):
    t = math.log(num,2)
    return 2**(int(t)+1)



from collections import defaultdict
n = getN()
nums = getlist()
numhash = defaultdict(int)
for i in nums:
    numhash[i] += 1
ans = 0
for num in sorted(numhash.keys(), key=lambda x: -x):
    while(numhash[num] != 0):
        target = (check_t(num)) - num
        if numhash[target]:

            if target == num:
                if numhash[target] >= 2:
                    ans += 1
                    numhash[target] -= 2
                else:
                    numhash[num] = 0
            else:
                if numhash[target] >= 1:
                    ans += 1
                    numhash[target] -= 1
                    numhash[num] -= 1
                else:
                    numhash[num] = 0
        else:
            numhash[num] = 0


print(ans)
