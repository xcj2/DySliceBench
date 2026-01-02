def compare_cards(a, b):
    return a[1] < b[1]

def bubble_sort(A):
    for i in range(len(A)):
        for j in range(len(A)-1, i, -1):
            if compare_cards(A[j], A[j-1]):
                A[j], A[j-1] = A[j-1], A[j]

def selection_sort(A):
    for i in range(len(A)):
        mini = i
        for j in range(i, len(A)):
            if compare_cards(A[j], A[mini]):
                mini = j
        A[i], A[mini] = A[mini], A[i]

def check_stable(originA, sortedA):
    for i in range(len(originA)-1):
        if not compare_cards(sortedA[i], sortedA[i+1]):
            if originA.index(sortedA[i]) > originA.index(sortedA[i+1]):
                return "Not stable"
    return "Stable"

N = int(input())
A = input().split()

bubbleA = list(A)
selectionA = list(A)

bubble_sort(bubbleA)
selection_sort(selectionA)

print(*bubbleA)
print(check_stable(A, bubbleA))

print(*selectionA)
print(check_stable(A, selectionA))