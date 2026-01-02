n = int(input())
a = list(map(str, input().split()))
b = a.copy()


def bubble_sort():
    for i in range(n):
        for j in reversed(range(i+1, n)):
            num = int(a[j][1])
            num_ = int(a[j-1][1])
            if num < num_:
                a[j], a[j-1] = a[j-1], a[j]
    return a


def selection_sort():
    for i in range(n):
        minv = int(b[i][1])
        mink = i
        for j in range(i, n):
            if int(b[j][1]) < minv:
                minv = int(b[j][1])
                mink = j
        if int(b[i][1]) != minv:
            b[i], b[mink] = b[mink], b[i]
    return b


bubble = bubble_sort()
selection = selection_sort()


def check_stable():
    if selection == bubble:
        return 'Stable'
    else:
        return 'Not stable'


check_selection = check_stable()


print(*bubble)
print('Stable')
print(*selection)
print(check_selection)
