def partition(A, p, r):
    x = A[r][1]
    i = p - 1
    for j in range(p, r):
        if A[j][1] <= x:
            i += 1
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
    tmp = A[i + 1]
    A[i + 1] = A[r]
    A[r] = tmp
    return i + 1


def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)


def resolve():
    from collections import defaultdict, deque
    n = int(input())
    A = []
    chk = defaultdict(deque)
    for _ in range(n):
        a, b = input().split()
        b = int(b)
        A.append([a, b])
        chk[b].append(a)
    quickSort(A, 0, len(A) - 1)
    for a, b in A:
        if chk[b].popleft() != a:
            print("Not stable")
            break
    else:
        print("Stable")
    for a in A:
        print(*a)


resolve()

