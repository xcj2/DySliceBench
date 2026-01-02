from copy import copy


class Card:

    def __init__(self, s):
        splited = s.split(' ')
        self.suit = splited[0]
        self.number = int(splited[1])

    def __gt__(self, other):
        return self.number > other.number

    def __ge__(self, other):
        return self.number >= other.number

    def __le__(self, other):
        return self.number <= other.number

    def __lt__(self, other):
        return self.number < other.number

    def __repr__(self):
        return '{} {}'.format(self.suit, self.number)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return self.suit == other.suit and self.number == other.number


s = 'A 0'
SENTINEL = Card(s)
SENTINEL.number = float('inf')


def main():
    n = int(input())
    cs_1 = [Card(input()) for _ in range(n)]
    cs_2 = copy(cs_1)
    merge_sort(cs_1, n, 0, n)
    quick_sort(cs_2, 0, n-1)
    if all([c1 == c2 for c1, c2 in zip(cs_1, cs_2)]):
        print('Stable')
    else:
        print('Not stable')
    print('\n'.join([str(c) for c in cs_2]))


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)


def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def merge_sort(A, n, left, right):
    if left+1 < right:
        mid = (left+right) // 2
        merge_sort(A, n, left, mid)
        merge_sort(A, n, mid, right)
        merge(A, n, left, mid, right)


def merge(A, n, left, mid, right):
    L = A[left:mid]
    R = A[mid:right]
    L.append(SENTINEL)
    R.append(SENTINEL)
    i = j = 0
    for k in range(left, right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


if __name__ == "__main__":
    main()


