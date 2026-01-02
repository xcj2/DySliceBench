def main():
    n = int(input())
    cards = list(map(str, input().split()))
    bubbleSortedCards = cards[:]
    selectionSortedCards = cards[:]


    bubbleSort(bubbleSortedCards, n)
    print(' '.join(map(str, bubbleSortedCards)))
    print('Stable')

    selectionSort(selectionSortedCards, n)
    print(' '.join(map(str, selectionSortedCards)))
    print(isStable(bubbleSortedCards, selectionSortedCards, n))


def bubbleSort(numbers, n):
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if int(numbers[j][1]) > int(numbers[j + 1][1]):
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

def selectionSort(numbers, n):
    minj = 0

    for i in range(n):
        minj = i
        for j in range(i, n, 1):
            if int(numbers[j][1]) < int(numbers[minj][1]):
                minj = j

        if i != minj:
            numbers[i], numbers[minj] = numbers[minj], numbers[i]

def isStable(bubbleSortedCards, selectionSortedCards, n):
    for i in range(n):
        if bubbleSortedCards[i] != selectionSortedCards[i]:
            return 'Not stable'

    return 'Stable'

if __name__ == '__main__':
    main()

