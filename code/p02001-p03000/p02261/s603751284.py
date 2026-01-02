def bubble_sort(A):
    cnt = 0
    for i in range(0, len(A) - 1):
        for j in range(len(A) - 1, i, -1):
            if A[j][1] < A[j - 1][1]:
                A[j - 1], A[j] = A[j], A[j - 1]
                cnt += 1


def selection_sort(A):
    for i in range(0, len(A)):
        min = i
        for j in range(i + 1, len(A)):
            if A[min][1] > A[j][1]:
                min = j
        A[i], A[min] = A[min], A[i]


def isStable(before, after):
    for i in range(0, len((before))):
        for j in range(i + 1, len(before)):
            for a in range(0, len(after)):
                for b in range(a + 1, len(after)):
                    if before[i][1] == before[j][1]:
                        if before[i] == after[b] and before[j] == after[a]:
                            return False
    return True


if __name__ == '__main__':
    n = int(input())
    l = input().split()
    m = l.copy()
    n = l.copy()
    bubble_sort(m)
    selection_sort(n)
    print(' '.join(m))
    print('Stable' if isStable(l, m) else 'Not stable')
    print(' '.join(n))
    print('Stable' if isStable(l, n) else 'Not stable')

