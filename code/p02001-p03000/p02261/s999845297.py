import copy

def bubble_sort(a):
    ba = copy.copy(a)
    flag = True
    for i in range(0, n):
        if not flag:
            break
        flag = False
        for j in range(n-1, 0, -1):
            if int(ba[j][1]) < int(ba[j-1][1]):
                ba[j], ba[j-1] = ba[j-1], ba[j]
                flag = True

    return ba

def selection_sort(a):
    sa = copy.copy(a)
    for i in range(n):
        flag = False
        minj = i
        for j in range(i, n):
            if int(sa[j][1]) < int(sa[minj][1]):
                minj = j
                flag = True
        if flag:
            sa[i], sa[minj] = sa[minj], sa[i]

    return sa

def is_stable(ba, sa):
    for b, s in zip(ba, sa):
        if b != s:
            return 'Not stable'
    return 'Stable'


n = int(input())
a = list(map(str, input().split()))

ba = bubble_sort(a)
print(' '.join(map(str, ba)))
print('Stable')

sa = selection_sort(a)
print(' '.join(map(str, sa)))
print(is_stable(ba, sa))

