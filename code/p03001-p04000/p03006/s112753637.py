def getN():
    return int(input())

def getMN():
    return list(map(int, input().split()))

def getlist():
    return list(map(int, input().split()))

def valid(steps):
    for i , x in enumerate(sorted(steps)):
        if i != x:
            return i - 1

    return len(steps) - 1
#
n = getN()
za = []
for i in range(n):
    za.append(getlist())
ans = 0
from collections import defaultdict
kumi = defaultdict(int)

for i, pa in enumerate(za):
    for j, pb in enumerate(za):
        xa, ya = pa
        xb, yb = pb
        dfx = xa - xb
        dfy = ya - yb

        diff = str(dfx) + str(dfy)
        kumi[diff] += 1

if n == 1:
    print(1)
    import sys;sys.exit()
del kumi["00"]
print(n - max(list(kumi.values())))

# for p1 in za:
#     for p2 in za:
#         steps = []
#         if p1 == p2:
#             continue
#         xa, ya = p1
#         xb, yb = p2
#         dfx = xb - xa
#         dfy = yb - ya
#         if not (dfx or dfy):
#             continue
#         for p3 in za:
#             xc, yc = p3
#             if dfx:
#                 if (xc - xa) % dfx == 0:
#                     step = (xc - xa) // dfx
#                     if yc - ya == dfy * step:
#                         steps.append(step)
#
#             else:
#                 if xc == xa:
#                     if (yc - ya) % dfy == 0:
#                         steps.append((yc - ya) // dfy)
#         tmp = valid(steps)
#         print(p1, p2, tmp, steps)
#         if tmp > ans:
#             ans = tmp
#             if tmp == 3:
#                 print(p1, p2)
#
# print(n-ans)
