n = int(input())
a = []
for i in range(n):
    suit, num = input().split()
    a.append([suit, int(num), int(i)])

b = a[:]

def partition(a, p, r):
    x = a[r][1]
    i = p - 1
    for j in range(p,r):
        if a[j][1] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1

def quickSort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quickSort(a, p, q - 1)
        quickSort(a, q + 1, r)

def checkStable(a):
    for i in range(len(a) - 1):
        if a[i][1] == a[i + 1][1] and a[i][2] > a[i + 1][2]:
            return "Not stable"
    return "Stable"

quickSort(a, 0, n - 1)

print(checkStable(a))
for a_i in a:
    print(a_i[0],a_i[1])