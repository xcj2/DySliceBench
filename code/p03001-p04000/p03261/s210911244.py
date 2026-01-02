import math
import string


def readints():
    return list(map(int, input().split()))


def nCr(n, r):
    return math.factorial(n)//(math.factorial(n-r)*math.factorial(r))


def has_duplicates2(seq):  # りストに重複した要素があるか判定（要素にリストがある場合）
    seen = []
    for item in seq:
        if not(item in seen):
            seen.append(item)
    return len(seq) != len(seen)


n = int(input())
w = [None]*n
for i in range(n):
    w[i] = input()
# print(w)

if has_duplicates2(w):
    print('No')
    exit()

for i in range(n-1):
    #print(w[i][-1], w[i+1][0])
    if w[i][-1] != w[i+1][0]:
        print('No')
        exit()
print('Yes')
