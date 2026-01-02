H = int(input())
A = [0]
# A = [int(i) for i in input().split()]
s = input().split()
for si in s:
    A.append(int(si))


def parent(i):
    return i // 2


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def max_heapify(a, i):
    l = left(i)
    r = right(i)
    if l <= H and a[l] > a[i]:
        largest = l
    else:
        largest = i

    if r <= H and a[r] > a[largest]:
        largest = r

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, largest)


def build_max_heap(a):
    for i in range(H // 2, 0, -1):
        max_heapify(a, i)


build_max_heap(A)
print("", " ".join([str(i) for i in A[1:]]))

