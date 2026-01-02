import math


def print_list_split_whitespace(a):
    for x in a[:-1]:
        print(x, end=' ')
    print(a[-1])


def insertion_sort(a, n, g, cnt):
    for i in range(g, n, 1):
        v = a[i]
        j = i - g
        while j >= 0 and a[j] > v:
            a[j + g] = a[j]
            j -= g
            cnt += 1
        a[j+g] = v
    return cnt


def shell_sort(a, n):
    cnt = 0
    m = math.floor(math.log(2 * n + 1, 3))
    print(m)
    gs = [1]
    for i in range(1, m, 1):
        gs.append(gs[i - 1] * 3 + 1)
    gs.reverse()
    print_list_split_whitespace(gs)

    for i in range(m):
        cnt = insertion_sort(a, n, gs[i], cnt)
    print(cnt)


n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

shell_sort(a, n)

for x in a:
    print(x)
