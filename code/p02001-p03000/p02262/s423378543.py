import math
def print_list(a):
    out = ''
    for ai in a:
        out += str(ai) + ' '
    else:
        out = out[:-1]
    print(out)

def insertion_sort(a, n, g):
    cnt = 0
    for i in range(g, n):
        v = a[i]
        j = i - g
        while j >= 0 and a[j] > v:
            a[j + g] = a[j]
            j = j - g
            cnt += 1
        a[j + g] = v
    return cnt

def shell_sort(a, n):
    cnt = 0
    m = 0
    g = []
    h = 1
    while True:
        if h > n:
            break
        m += 1
        g.append(h)
        h = 3 * h + 1
    g.reverse()

    for i in range(m):
        cnt += insertion_sort(a, n, g[i])
    print(m)
    print_list(g)
    print(cnt)
    for i in a:
        print(i)

n = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())

shell_sort(a, n)

