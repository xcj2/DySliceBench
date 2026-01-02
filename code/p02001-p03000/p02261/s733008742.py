_, cards = input(), input().split()

def bubble_sort(array):
    A = array[:]
    for i in range(len(A)):
        for j in range(1, len(A) - i):
            if int(A[j - 1][1]) > int(A[j][1]):
                A[j], A[j - 1] = A[j - 1], A[j]
    return A

def selection_sort(array):
    A = array[:]
    for i in range(len(A)):
        minn = i
        for j in range(i, len(A)):
            if int(A[j][1]) < int(A[minn][1]): minn = j
        A[i], A[minn] = A[minn], A[i]
    return A
def is_stable(org, sorted):

    def get_same_numbers(array):
        result = {}
        for i in range(1, 10):
            result[i] = []
            for j in range(len(array)):
                if int(array[j][1]) == i:
                    result[i].append(array[j])
        return [cards for _, cards in result.items() if len(cards) >= 2]

    return "Stable" if get_same_numbers(org) == get_same_numbers(sorted) else "Not stable"

a = bubble_sort(cards)
print(" ".join(a))
print(is_stable(cards, a))
b = selection_sort(cards)
print(" ".join(b))
print(is_stable(cards, b))
