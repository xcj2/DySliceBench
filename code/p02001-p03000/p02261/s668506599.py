def bubble_sort(c, n):
    c = c.copy()
    for i in range(n):
        for j in range(0, n - 1):
            if c[j][1] > c[j + 1][1]:
                c[j], c[j + 1] = c[j + 1], c[j]
    return c


def selection_sort(a, n):
    a = a.copy()
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if a[j][1] < a[min_index][1]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    return a


def print_list(a):
    print(" ".join([s + v for s, v in a]))


def is_stable(l1, l2):
    def get_original_index(v):
        for i, e in enumerate(l1):
            if v == e:
                return i
        return Exception("bug")

    before = l2[0]
    for e in l2[1:]:
        if before[1] == e[1]:
            # print(before, e)
            bi = get_original_index(before)
            ei = get_original_index(e)
            # print(bi, ei)
            if bi > ei:
                return False
        before = e

    return True


n = int(input())
tmp = input().split()
a = []
for v in tmp:
    a.append((v[0], v[1]))

bs_result = bubble_sort(a, n)
ss_result = selection_sort(a, n)

print_list(bs_result)
if is_stable(a, bs_result):
    print("Stable")
else:
    print("Not stable")

print_list(ss_result)
if is_stable(a, ss_result):
    print("Stable")
else:
    print("Not stable")

