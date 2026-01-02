#!/usr/bin/env python
import copy

def bubble_sort(card, N):
    for i in range(0, N):
        for j in range(N-1, i, -1):
            if value(card[j]) < value(card[j-1]):
                card[j], card[j-1] = card[j-1], card[j]
    return " ".join(map(str, card))


def selection_sort(card, N):
    for i in range(0, N):
        minj = i
        for j in range(i, N):
            if value(card[j]) < value(card[minj]):
                minj = j
        card[i], card[minj] = card[minj], card[i]
    return " ".join(map(str, card))


# check method
# insertion sort is a stable sort.
def insertion_sort(card, N):
    for i in range(1, N):
        v = card[i]
        j = i - 1
        while j >= 0 and value(card[j]) > value(v):
            card[j+1] = card[j]
            j -= 1
        card[j+1] = v
    return " ".join(map(str, card))


def value(elem):
    return elem[1]


def main():
    size = int(input())
    line = input().split()
    gold_standard = insertion_sort(copy.deepcopy(line), copy.deepcopy(size))

    bubble_ans = bubble_sort(copy.deepcopy(line), copy.deepcopy(size))
    print(bubble_ans)
    if bubble_ans == gold_standard:
        print('Stable')
    else:
        print('Not stable')

    selection_ans = selection_sort(copy.deepcopy(line), copy.deepcopy(size))
    print(selection_ans)
    if selection_ans == gold_standard:
        print('Stable')
    else:
        print('Not stable')


if __name__ == '__main__':
    main()