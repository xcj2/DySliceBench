import sys


def intervals(n):
    results = []
    g = 1
    while g <= n:
        results.append(g)
        g = g * 3 + 1
    return list(reversed(results))


def insertion_sort(a, g):
    n = len(a)
    count = 0
    for i in range(g, n):
        v = a[i]
        j = i - g
        while j >= 0 and a[j] > v:
            a[j + g] = a[j]
            j -= g
            count += 1
        a[j + g] = v
    return count


def shell_sort(a):
    n = len(a)
    count = 0
    gs = intervals(n)
    for g in gs:
        count += insertion_sort(a, g)
    print(len(gs))
    print(' '.join(map(str, gs)))
    print(count)
    for value in a:
        print(value)


n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(n)]
shell_sort(a)

