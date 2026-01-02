def bubble_sort(c, n):
    is_swapped = True
    i = 0
    while is_swapped:
        is_swapped = False
        for j in range(n-1, i, -1):
            if c[j][1] < c[j-1][1]:
                tmp = c[j]
                c[j] = c[j-1]
                c[j-1] = tmp
                is_swapped = True
        i += 1


def selection_sort(c, n):
    for i in range(n):
        minj = i
        for j in range(i, n):
            if c[j][1] < c[minj][1]:
                minj = j
        if i != minj:
            tmp = c[i]
            c[i] = c[minj]
            c[minj] = tmp


def make_dict(l):
    result = {}
    for v in l:
        num = v[1]
        if num in result:
            result[num].append(v)
        else:
            result[num] = [v]
    result = {k: v for k, v in result.items() if len(v) >= 2}

    return result


def print_is_stable(before, after):
    is_stable = True
    before_dict = make_dict(before)
    after_dict = make_dict(after)
    for k in before_dict:
        if before_dict[k] != after_dict[k]:
            is_stable = False
            break

    if is_stable:
        print('Stable')
    else:
        print('Not stable')


n = int(input())
a = [i for i in input().split()]
c = a[:]

bubble_sort(c, n)
print(' '.join([str(i) for i in c]))
print_is_stable(a, c)

c = a[:]
selection_sort(c, n)
print(' '.join([str(i) for i in c]))
print_is_stable(a, c)
