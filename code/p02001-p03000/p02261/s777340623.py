def show(array):
    for i in range(len(array)):
        if (i+1) >= len(array):
            print(array[i])
        else:
            print(array[i], end=' ')


def bubble_sort(c, n):
    for i in range(0, n):
        for j in range(n-1, i, -1):
            if c[j][1:] < c[j-1][1:]:
                c[j], c[j-1] = c[j-1], c[j]

    return c

def selection_sort(c, n):
    for i in range(0, n):
        
        minj = i
        for j in range(i+1, n):
            if c[j][1:] < c[minj][1:]:
                minj = j
        # if i != minj:
        c[i], c[minj] = c[minj], c[i]
    return c


def main():
    N = int(input())
    cards = list(input().split(' '))
    cards2 = cards.copy()

    # value_sorted = sorted(cards, key=lambda x: x[1:])
    bubble_result = bubble_sort(cards, N)
    selection_result = selection_sort(cards2, N)

    show(bubble_result)
    print('Stable')
    show(selection_result)
    if bubble_result == selection_result:
        print('Stable')
    else:
        print('Not stable')


main()
