n = int(input())
cards = input().split()


def print_stable(original_list, sorted_list):
    for n in range(1, 10):
        original_list_n = filter(lambda card: int(card[1]) == n, original_list)
        sorted_list_n = filter(lambda card: int(card[1]) == n, sorted_list)
        is_same = all(map(lambda c: c[0] == c[1], zip(original_list_n, sorted_list_n)))
        if not is_same:
            print('Not stable')
            return
    print('Stable')


def print_list(l):
    print(' '.join(map(str, l)))


def bubble_sort(l):
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1, 0, -1):
            if l[i][1] < l[i - 1][1]:
                l[i], l[i - 1] = l[i - 1], l[i]
                swapped = True
    return l


def selection_sort(l):
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if l[j][1] < l[min_index][1]:
                min_index = j
        l[i], l[min_index] = l[min_index], l[i]
    return l


bubble_list = bubble_sort(cards[:])
print_list(bubble_list)
print_stable(cards, bubble_list)

selection_list = selection_sort(cards[:])
print_list(selection_list)
print_stable(cards, selection_list)

