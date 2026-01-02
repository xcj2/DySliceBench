n = int(input())
data = list(input().split() for _ in range(n))
c = 0

for k in range(n):
    data[k].append(str(k))


def exchange(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp
    return a


def partition(a, p, r):
    x = int(a[r][1])
    i = p-1
    for j in range(p, r):
        if int(a[j][1]) <= x:
            i += 1
            a = exchange(a, i, j)
    exchange(a, i+1, r)
    return i+1


def quicksort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quicksort(a, p, q-1)
        quicksort(a, q+1, r)


quicksort(data, 0, n-1)

for l in range(n-1):
    if int(data[l][1]) == int(data[l+1][1]):
        if int(data[l][2]) > int(data[l+1][2]):
            print('Not stable')
            c = 1
            break

if c == 0:
    print('Stable')

for l in range(n):
    print(data[l][0], data[l][1])

