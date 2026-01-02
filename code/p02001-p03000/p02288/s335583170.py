
def parent(i):
    return i // 2


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def max_heapify(i):
    global A

    l = left(i)
    r = right(i)

    if l <= H and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r <= H and A[r] > A[largest]:
        largest = r

    if largest != i:  # iが子供に降るときは、
        A[i], A[largest] = A[largest], A[i]
        max_heapify(largest)  # ここでいうlargestは、元々はiの子ノード。戦いに敗れたA[i]が格納されている。


H = int(input())
A = [None] * (H + 1)

_ = list(map(int, input().split()))
A[1:] = _

for i in range(H//2, 0, -1):
    # print(i)
    max_heapify(i)

print(' ' + ' '.join(map(str, A[1:])))

