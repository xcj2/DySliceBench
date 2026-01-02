def bubbleSort(cards):
    n = len(cards)
    for i in range(n):
        for j in range(n-1, i, -1):
            if cards[j][1] < cards[j-1][1]:
                cards[j], cards[j-1] = cards[j-1], cards[j]
    
    return cards


def selectionSort(cards):
    n = len(cards)
    for i in range(n):
        minj = i
        for j in range(i, n):
            if cards[j][1] < cards[minj][1]:
                minj = j
        cards[i], cards[minj] = cards[minj], cards[i]
    
    return cards


def isStableSort(initialArray, resultArray):
    n = len(initialArray)
    for i in range(n):
        for j in range(i+1, n):
            for a in range(n):
                for b in range(a+1, n):
                    if initialArray[i][1] == initialArray[j][1]:
                        if initialArray[i] == resultArray[b]:
                            if initialArray[j] == resultArray[a]:
                                return False
    
    return True


n = int(input())
array = [x for x in input().split()]
cards = [[a[0], a[1]] for a in array]
cardsForBubble = cards[:]
cardsForSelection = cards[:]

bSort = bubbleSort(cardsForBubble)
sSort = selectionSort(cardsForSelection)

resultForBubble = []
resultForSelection = []

for b in bSort:
    resultForBubble.append(''.join(b))
for s in sSort:
    resultForSelection.append(''.join(s))

print(*resultForBubble)
if isStableSort(array, resultForBubble):
    print("Stable")
else:
    print("Not stable")

print(*resultForSelection)
if isStableSort(array, resultForSelection):
    print("Stable")
else:
    print("Not stable")
