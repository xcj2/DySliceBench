import copy
n = int(input())
c = input().split()
c = [[c[i][0], int(c[i][1])] for i in range(n)]
ba = copy.deepcopy(c)
sa = copy.deepcopy(c)

def bubble_sort(a, n):
    flag = 1
    i = 0
    while flag:
        flag = 0
        for j in reversed(range(i+1, n)):
            if a[j][1] < a[j-1][1]:
                a[j], a[j-1] = a[j-1], a[j]
                flag = 1
        i += 1
    return a

def selection_sort(a, n):
    for i in range(n-1):
        minj = i
        for j in range(i, n):
            if a[j][1] < a[minj][1]:
                minj = j
        a[i], a[minj] = a[minj], a[i]
    return a

ba = bubble_sort(ba, n)
sa = selection_sort(sa, n)

def is_stable(x, y):
    for i in range(n):
        if x[i][0] != y[i][0]:
            return False
    return True

fba = [i[0] + str(i[1]) for i in ba]
print(' '.join(fba))
print('Stable')
fsa = [i[0] + str(i[1]) for i in sa]
print(' '.join(fsa))
print('Stable' if is_stable(ba, sa) else 'Not stable')
