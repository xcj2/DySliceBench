def is_stable(A, B, n):
    for i in range(n):
        for j in range(i+1, n):
            if A[i]['value'] == A[j]['value']:
                for a in range(n):
                    for b in range(a+1, n):
                        if A[i] == B[b] and A[j] == B[a]:
                            return False
    return True


def show(Card, n):
    for i in range(n):
        if i != n-1:
            print(Card[i]['suit'] + str(Card[i]['value']), end=' ')
        else:
            print(Card[i]['suit'] + str(Card[i]['value']))


def bubble_sort(A, n):
    Card = A.copy()
    flag = 1
    while flag:
        flag = 0
        for i in range(n-1):
            if Card[i]['value'] > Card[i+1]['value']:
                Card[i], Card[i+1] = Card[i+1], Card[i]
                flag = 1
    show(Card, n)
    return Card


def selection_sort(A, n):
    Card = A.copy()
    for i in range(n-1):
        min_j = i
        for j in range(i+1, n):
            if Card[min_j]['value'] > Card[j]['value']:
                min_j = j
        if min_j != i:
            Card[i], Card[min_j] = Card[min_j], Card[i]
    show(Card, n)
    return Card


def main():
    n = int(input())
    A = list(input().split())
    Card = [
        {'value': int(a[1]), 'suit': a[0]}
        for a in A
    ]
    Card_bubble = bubble_sort(Card, n)
    if is_stable(Card, Card_bubble, n):
        print('Stable')
    else:
        print('Not stable')
    Card_selection = selection_sort(Card, n)
    if is_stable(Card, Card_selection, n):
        print('Stable')
    else:
        print('Not stable')


if __name__ == "__main__":
    main()

