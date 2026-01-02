def check_stable(before_sort_list, after_sort_list):
    N = len(before_sort_list)
    for i in range(0, N, 1):
        for j in range(i+1, N, 1):
            for a in range(0, N, 1):
                for b in range(a+1, N, 1):
                    if before_sort_list[i][1] == before_sort_list[j][1] and before_sort_list[i] == after_sort_list[b] and before_sort_list[j] == after_sort_list[a]:
                        return False
    return True

def bubble_sort(cards_list, N):
    for i in range(0, N, 1):
        for j in range(N-1, i, -1):
            if cards_list[j][1] < cards_list[j-1][1]:
                cards_list[j], cards_list[j-1] = (cards_list[j-1], cards_list[j])
    return cards_list


def selection_sort(cards_list, N):
    for i in range(0, N, 1):
        minj = i
        for j in range(i, N, 1):
            if cards_list[j][1] < cards_list[minj][1]:
                minj = j
        cards_list[i], cards_list[minj] = (cards_list[minj], cards_list[i])
    return cards_list


num_cards = int(input())
cards = input().split(' ')

sorted_cards1 = bubble_sort(cards.copy(), num_cards)
sorted_cards2 = selection_sort(cards.copy(), num_cards)

print(' '.join(sorted_cards1))
print('Stable' if check_stable(cards, sorted_cards1) else 'Not stable')
print(' '.join(sorted_cards2))
print('Stable' if check_stable(cards, sorted_cards2) else 'Not stable')
