def bubble_sort(a, n):
    for i in range(n):
        for j in range(n - 1, i, -1):
            if a[j]['value'] < a[j - 1]['value']:
                tmp = a[j]
                a[j] = a[j - 1]
                a[j - 1] = tmp


def selection_sort(a, n):
    is_stable = True

    for i in range(n):
        minj = i
        samei = n
        for j in range(i+1, n, 1):
            if a[j]['value'] == a[i]['value']:
                samei = j
            if a[j]['value'] < a[minj]['value']:
                minj = j
                if samei < minj:
                    is_stable = False
        tmp = a[i]
        a[i] = a[minj]
        a[minj] = tmp

    return is_stable

def print_list_split_whitespace(a):
    for x in a[:-1]:
        print(x['design'] + str(x['value']), end=' ')
    print(a[-1]['design'] + str(a[-1]['value']))


n = int(input())

a = input().split()
for i in range(n):
    s = a[i]
    a[i] = {'design': s[0], 'value': int(s[1])}
b = a.copy()
c = a.copy()

bubble_sort(a, n)
print_list_split_whitespace(a)

print("Stable")

is_stable = selection_sort(b, n)
print_list_split_whitespace(b)

if is_stable:
    print("Stable")
else:
    print("Not stable")
