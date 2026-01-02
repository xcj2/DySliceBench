n = int(input())

A = list(input().split())

def insertion_sort(l):
    for i in range(0, len(l) - 1):
        x = i + 1
        while x != 0 and int(l[x][1]) < int(l[x - 1][1]):
            temp = l[x]
            l[x] = l[x - 1]
            l[x - 1] = temp
            x -= 1
    return l


def babble_sort(l):
    for i in range(0, len(l)):
        for j in reversed(range(i+1, len(l))):
            b = int(l[j][1])
            a = int(l[j - 1][1])
            if b < a:
                t = l[j]
                l[j] = l[j-1]
                l[j-1] = t
    return l

def is_stable(a, l):
    for i in range(0, len(a)):
        if a[i] != l[i]:
            return False
    return True

def print_with_space(l):
    print(' '.join(str(x) for x in l))

B = insertion_sort(A[:])

babbled = babble_sort(A[:])
print_with_space(babbled)

if is_stable(B, babbled):
    print('Stable')
else:
    print('Not stable')

def selection_sort(l):
    for i in range(0, len(l)):
        minj = i
        for j in range(i, len(l)):
            if int(l[j][1]) < int(l[minj][1]):
                minj = j
        t = l[i]
        l[i] = l[minj]
        l[minj] = t
    return l

selected = selection_sort(A[:])
print_with_space(selected)

if is_stable(B, selected):
    print('Stable')
else:
    print('Not stable')