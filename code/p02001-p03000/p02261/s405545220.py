def bubble_sort_index(n, number_from_cards):
    flag = True
    index_lists = list(range(n))
    while flag:
        flag = False
        for i in range(n - 1, 0, -1):
            if number_from_cards[i] < number_from_cards[i - 1]:
                number_from_cards[i], number_from_cards[i - 1] = number_from_cards[i - 1], number_from_cards[i]
                index_lists[i], index_lists[i - 1] = index_lists[i - 1], index_lists[i]
                flag = True
    return index_lists


def selection_sort_index(n, number_from_cards):
    index_list = list(range(n))
    for i in range(n):
        min_j = i
        for j in range(i, n):
            if number_from_cards[min_j] > number_from_cards[j]:
                min_j = j
        if min_j == i:
            continue
        number_from_cards[i], number_from_cards[min_j] = number_from_cards[min_j], number_from_cards[i]
        index_list[i], index_list[min_j] = index_list[min_j], index_list[i]
    return index_list


def main():
    N = int(input())
    true_cards = input().split(' ')
    number_from_cards = [int(c[-1]) for c in true_cards]
    sorted_index_lists_for_bubble = bubble_sort_index(N, number_from_cards.copy())
    sorted_bubble = [true_cards[index] for index in sorted_index_lists_for_bubble]

    sorted_index_lists_for_selection = selection_sort_index(N, number_from_cards.copy())
    sorted_selection = [true_cards[index] for index in sorted_index_lists_for_selection]

    print(' '.join(sorted_bubble))
    print('Stable')
    print(' '.join(sorted_selection))
    if sorted_bubble == sorted_selection:
        print('Stable')
    else:
        print('Not stable')


if __name__ == '__main__':
    main()

