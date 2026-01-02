from collections import defaultdict


def key(pair):
    _, n = pair
    return n


def partitionize(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if key(A[j]) <= key(x):
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quick_sort(A, p, r):
    if p < r:
        q = partitionize(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


def is_stable(ordered, original):
    scanned_ordered = defaultdict(list)
    scanned_original = defaultdict(list)
    for a, b in zip(ordered, original):
        s, n = a
        scanned_ordered[n].append(s)
        t, m = b
        scanned_original[m].append(t)
    for k in scanned_ordered:
        if scanned_ordered.get(k, "__NaN_1__") != scanned_original.get(k, "__NaN_2__"):
            return False
    return True


N = int(input())
A = []
for _ in range(N):
    s, n = input().split()
    A.append((s, int(n)))
sorted_A = A.copy()
quick_sort(sorted_A, 0, N - 1)
print("Stable" if is_stable(sorted_A, A) else "Not stable")
for s, n in sorted_A:
    print(s, n)

