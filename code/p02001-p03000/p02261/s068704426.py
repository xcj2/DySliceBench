class Card:
    def __init__(self, s):
        self.suit = s[0]
        self.value = int(s[1])

    def __lt__(self, another_card):
        return self.value < another_card.value

    def __repr__(self):
        return self.suit + str(self.value)


def bubble_sort(A):
    n = len(A)
    A = A[:]
    for i in range(n):
        for j in reversed(range(i + 1, n)):
            if A[j] < A[j - 1]:
                A[j - 1], A[j] = A[j], A[j - 1]
    return A


def selection_sort(A):
    n = len(A)
    A = A[:]
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if A[j] < A[min_idx]:
                min_idx = j
        A[min_idx], A[i] = A[i], A[min_idx]
    return A


N = int(input())
A = [Card(s) for s in input().split()]
A_sorted_by_bsort = bubble_sort(A)
A_sorted_by_ssort = selection_sort(A)
print(*A_sorted_by_bsort)
print("Stable")
print(*A_sorted_by_ssort)
print("Stable" if A_sorted_by_ssort == A_sorted_by_bsort else "Not stable")

