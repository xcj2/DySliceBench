def make_card(i, card):
    suit, value = card.split()
    return (int(value), i, card)


def partition_stable(a, p, r):
    x, i = a[r], p - 1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    i += 1
    a[i], a[r] = a[r], a[i]
    return i


def partition_not_stable(a, p, r):
    x, i = a[r][0], p - 1
    for j in range(p, r):
        if a[j][0] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    i += 1
    a[i], a[r] = a[r], a[i]
    return i


def quick_sort(a, p, r, func):
    if p < r:
        q = func(a, p, r)
        quick_sort(a, p, q - 1, func)
        quick_sort(a, q + 1, r, func)


n = int(input())
a = list(make_card(i, input()) for i in range(n))
b = a[:]

quick_sort(a, 0, n - 1, partition_not_stable)
quick_sort(b, 0, n - 1, partition_stable)
print(('S' if a == b else 'Not s') + 'table')
print('\n'.join(card[2] for card in a))

