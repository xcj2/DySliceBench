def get_left_index(A, i):
    if len(A) > 2 * i:
        return 2 * i
    else:
        return None

def get_right_index(A, i):
    if len(A) > 2 * i + 1:
        return 2 * i + 1
    else:
        return None

def max_heapfy(A, i):
    left = get_left_index(A, i)
    right = get_right_index(A, i)
    largest = i
    if left and A[left] > A[i]:
        largest = left
    if right and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapfy(A, largest)

H = int(input())
A = [0]
for elem in map(int, input().split()):
    A.append(elem)


def build_max_heap(A):
    for i in range(H//2, 0, -1):
        max_heapfy(A, i)
build_max_heap(A)
print(' ', end='')        
print(*A[1:])
