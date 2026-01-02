def partition(a, p, r):
    x = a[r][1]
    i = p - 1
    for j in range(p, r):
        if a[j][1] <= x:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


def quicksort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quicksort(a, p, q - 1)
        quicksort(a, q + 1, r)


def checkstable(a):
    for i in range(1, len(a)):
        if a[i - 1][1] == a[i][1]:
            if a[i - 1][2] > a[i][2]:
                return "Not stable"
    return "Stable"


import sys
n = int(input())
a = []
for i in range(n):
    suit, num = sys.stdin.readline().split()
    a += [[suit, int(num), i]]

quicksort(a, 0, len(a) - 1)
print(checkstable(a))

for line in a:
    print(line[0], line[1])