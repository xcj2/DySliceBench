def is_stable(before_sort, after_sort):
    current_num = 0
    same_number_card = list()
    for num in after_sort:
        if current_num == int(num[1]):
            for same_card in same_number_card:
                if before_sort.index(same_card) > before_sort.index(num):
                    return False
            same_number_card.append(num)
        else:
            current_num = int(num[1])
            same_number_card = [num,]
    return True

def partition(A, p, r):
    x = A[r][1]
    i = p - 1
    for j in range(p, r):
        if A[j][1] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

if __name__ == '__main__':
    n = int(input())
    cards = list()
    for i in range(n):
        card = input().split()
        card[1] = int(card[1])
        cards.append(card)
    before_cards = list(cards)
    quicksort(cards, 0, n-1)
    print('Stable') if is_stable(before_cards, cards) else print('Not stable')
    for card in cards:
        print(*card)