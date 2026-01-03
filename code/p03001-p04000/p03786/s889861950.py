def search_sorted(x, xs):
    '''
    >>> search_sorted(3, range(10))
    3
    >>> search_sorted(3, [0, 1, 3, 3, 3, 5])
    4
    >>> search_sorted(3, [0, 1, 3, 3])
    3
    >>> search_sorted(1, [1, 1])
    1
    '''
    i = 0
    j = len(xs)
    while j - i > 1:
        m = (i + j) // 2
        if xs[m] <= x:
            i = m
        elif x < xs[m]:
            j = m
    return i

class FenwickTree:
    '''
    >>> tree = FenwickTree(5)
    >>> tree.add(0, 3)
    >>> tree.add(4, 2)
    >>> tree.add(2, 7)
    >>> tree.sum(5)
    12
    >>> tree.sum(3)
    10
    >>> tree.sum(2)
    3
    >>> tree.sum(1)
    3
    >>> tree.sum(0)
    0

    '''
    def __init__(self, n):
        self.array = [0] * n

    def add(self, i, x):
        while i < len(self.array):
            self.array[i] += x
            w = (i + 1) & -(i + 1)
            i += w

    def sum(self, i):
        i -= 1
        s = 0
        while i >= 0:
            s += self.array[i]
            w = (i + 1) & -(i + 1)
            i -= w
        return s


def solve():
    input()
    A = list(map(int, input().split())); A.sort()
    tree = FenwickTree(len(A))
    for i, a in enumerate(A):
        tree.add(i, a)

    answer = 0
    for i in range(len(A)):
        a = A[i]
        j = i
        while True:
            j = search_sorted(a * 2, A)
            a_ = tree.sum(j + 1)
            if a == a_:
                break
            else:
                a = a_
        if j + 1 == len(A):
            answer += 1
    print(answer)

solve()
