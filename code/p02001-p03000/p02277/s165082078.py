class Card:

    def __init__(self, data):
        self.mark = data[0]
        self.number = int(data[2:])

    def __str__(self):
        return f"{self.mark} {self.number}"

    def __eq__(self, other):
        return self.number == other.number

    def __ne__(self, other):
        return self.number != other.number

    def __le__(self, other):
        return self.number <= other.number

    def __lt__(self, other):
        return self.number < other.number

    def __ge__(self, other):
        return self.number >= other.number

    def __gt__(self, other):
        return self.number > other.number


def partition(p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quickSort(p, r):
    if p < r:
        q = partition(p, r)
        quickSort(p, q - 1)
        quickSort(q + 1, r)


def is_stable():
    count = 0
    for i, a in enumerate(A):
        if i == len(A) - 1:
            return True
        k = 0
        for o in Origin:
            if a.number == o.number:
                if count != k:
                    k += 1
                    continue
                if a.mark != o.mark:
                    return False
                else:
                    break
        if a.number != A[i + 1].number:
            count = 0
        else:
            count += 1

A = []
n = int(input())
for i in range(n):
    A.append(Card(input()))
Origin = A.copy()
quickSort(0, len(A) - 1)
print("Stable" if is_stable() else "Not stable")
print("\n".join(str(a) for a in A))

