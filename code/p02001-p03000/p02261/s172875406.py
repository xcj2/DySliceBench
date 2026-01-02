#! python3
# stable_sort.py

import copy

def num_from_card(card):
    return int(card[1:])

def bubble_sort(A, N):
    A_ = copy.copy(A)
    flag = True
    while flag:
        flag = False
        for i in range(N-1, 0, -1):
            if num_from_card(A_[i]) < num_from_card(A_[i-1]):
                A_[i-1], A_[i] = A_[i], A_[i-1]
                flag = True
    return A_

def selection_sort(A, N):
    A_ = copy.copy(A)
    for i in range(N-1):
        minj = i
        for j in range(i, N):
            if num_from_card(A_[j]) < num_from_card(A_[minj]):
                minj = j
        if i != minj:
            A_[i], A_[minj] = A_[minj], A_[i]
    return A_

def is_stable(A, sorted_A, N):
    A_nums = [int(x[1:]) for x in A]
    same_num = [x for x in set(A_nums) if A_nums.count(x) > 1]
    A_symbols, sorted_A_symbols = [], []
    flag = 'Stable'
    for num in same_num:
        if [card[0] for card in A if int(card[1:]) == num] != [card[0] for card in sorted_A if int(card[1:]) == num]:
            flag = 'Not stable'
            break
    return flag

N = int(input())
cards = [x for x in input().split(' ')]

bubble_sorted = bubble_sort(cards, N)
selection_sorted = selection_sort(cards, N)

print(' '.join(bubble_sorted))
print(is_stable(cards, bubble_sorted, N))
print(' '.join(selection_sorted))
print(is_stable(cards, selection_sorted, N))
