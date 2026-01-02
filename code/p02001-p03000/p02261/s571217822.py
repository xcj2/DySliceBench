MARK = 0
NUMBER = 1


def bubble_sort(A):
    for i in range(len(A)-1):
        for j in reversed(range(i+1, len(A))):
            if A[j][NUMBER] < A[j - 1][NUMBER]:
                swap(A, j-1, j)


def selection_sort(A):
    for i in range(len(A)):
        mini = i
        for j in range(i, len(A)):
            if A[j][NUMBER] < A[mini][NUMBER]:
                mini = j
        if mini != i:
            swap(A, mini, i)


def swap(A, i, j):
    tmp = A[j]
    A[j] = A[i]
    A[i] = tmp


amount = int(input())
cards = input().split()  # list of cards (ex:[H2 S8])
isStable_selection = True

# make tuple of mark and number
for i in range(amount):
    cards[i] = tuple([cards[i][MARK], int(cards[i][NUMBER])])

cards_bubble = list(cards)
cards_selection = list(cards)

bubble_sort(cards_bubble)
selection_sort(cards_selection)

# judge stable or not (bubble sort is stable)
if cards_bubble == cards_selection:
    isStable_selection = True
else:
    isStable_selection = False

print(*[cards_bubble[i][MARK] + str(cards_bubble[i][NUMBER])
        for i in range(amount)])
print("Stable")

print(*[cards_selection[i][MARK] + str(cards_selection[i][NUMBER])
        for i in range(amount)])
if isStable_selection:
    print("Stable")
else:
    print("Not stable")