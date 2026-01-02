MAX = 500000
H = None

def parent(i):
    return i//2


def left(i):
    return 2*i


def right(i):
    return 2*i+1


def max_heapify(A, i):
    l = left(i)
    r = right(i)

    if l <= H and A[l] > A[i]:
        largest = l
    else:
        largest = i
    
    if r <= H and A[r] > A[largest]:
        largest = r
    
    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        max_heapify(A, largest)


def build_max_heap(A):
    for i in range(H//2, 0, -1):
        max_heapify(A, i)


def main():
    global H
    H = int(input())
    A = [0] * (MAX+1)

    v_s = input().split(' ')

    for i in range(H):
        A[i+1] = int(v_s[i])

    build_max_heap(A)

    print(' ' + ' '.join(map(str, A[1:H+1])))


if __name__ == '__main__':
    main()

