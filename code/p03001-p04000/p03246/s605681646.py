from collections import defaultdict

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

n = getN()
nums = getlist()
lis1 = defaultdict(int)
lis2 = defaultdict(int)

for i,s in enumerate(nums):
    if i % 2 == 0:
        lis1[s] += 1
    else:
        lis2[s] += 1

maxk1 = []
maxv1 = 0
for k in lis1.keys():
    if lis1[k] == maxv1:
        maxk1.append(k)
    elif lis1[k] > maxv1:
        maxv1 = lis1[k]
        maxk1 = [k]

maxk2 = []
maxv2 = 0
for k in lis2.keys():
    if lis2[k] == maxv2:
        maxk2.append(k)
    elif lis2[k] > maxv2:
        maxv2 = lis2[k]
        maxk2 = [k]

v1 = list(lis1.values())
v1.sort(reverse=True)
v1 = v1 + [0]
v2 = list(lis2.values())
v2.sort(reverse=True)
v2 = v2 + [0]

if (len(maxk1) == 1) and (len(maxk2) == 1) and (maxk1[0] == maxk2[0]):
    rem = max(v1[0] + v2[1], v2[0] + v1[1])
    ans = n-rem

else:
    ans = n - maxv1 - maxv2
print(ans)


