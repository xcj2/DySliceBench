def bubble_sort(card, n):
    flag = 1
    while flag:
        flag = 0
        for i in range(n-1, 0, -1):
            if card[i][1] < card[i-1][1]:
                card[i], card[i-1] = card[i-1], card[i]
                flag = 1
    print(' '.join(map(str, card)))
    return card

def selection_sort(card, n):
    for i in range(n):
        minj = i
        for j in range(i, n):
            if card[j][1] <  card[minj][1]:
                minj=j
        if i != minj:              
            card[i], card[minj] = card[minj], card[i]

    print(' '.join(map(str, card)))
    return card

def isStable(stable_sorted, target):
    for i in range(len(stable_sorted)):
        if stable_sorted[i] != target[i]:
            return "Not stable"
    return "Stable"

def main():
    n = int(input())
    card = input().split()

    bubble_sorted_card = bubble_sort(card.copy(), n)
    print(isStable(bubble_sorted_card, bubble_sorted_card))

    selection_sorted_card = selection_sort(card.copy(), n)
    print(isStable(bubble_sorted_card, selection_sorted_card))

if __name__ == "__main__":
    main()
