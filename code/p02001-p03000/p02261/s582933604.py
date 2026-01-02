# -*- coding: utf-8 -*-


def bubble_sort(cards, num):
    flag = True
    while flag:
        flag = False
        for left in range(num-1, 0, -1):
            right = left - 1
            if cards[left][1] < cards[right][1]:
                cards[right], cards[left] = cards[left], cards[right]
                flag = True

    print(list_to_str(cards))


def selection_sort(cards, num):
    for head in range(num):
        min_i = head

        for target in range(head+1, num):
            if cards[target][1] < cards[min_i][1]:
                min_i = target
        cards[head], cards[min_i] = cards[min_i], cards[head]

    print(list_to_str(cards))


def is_stable(before, after, num):
    for i in range(num):
        for j in range(i+1, num):
            for a in range(num):
                for b in range(a+1, num):
                    if before[i][1] == before[j][1]\
                    and before[i] == after[b]\
                    and before[j] == after[a]:
                        return 'Not stable'
    return 'Stable'


def list_to_str(l, delimiter=' '):
    # The default delimiter is one space.
    return delimiter.join([str(v) for v in l])


if __name__ == '__main__':
    num = int(input())
    cards = input().split()
    cards_for_bubble = cards.copy()
    cards_for_selection = cards.copy()

    bubble_sort(cards_for_bubble, num)
    print(is_stable(cards, cards_for_bubble, num))

    selection_sort(cards_for_selection, num)
    print(is_stable(cards, cards_for_selection, num))