def max_heapify(a, i):
    heap_size = len(a)
    left = (i + 1) * 2 - 1
    right = left + 1
    if left < heap_size and a[left] > a[i]:
        largest = left
    else:
        largest = i
    if right < heap_size and a[right] > a[largest]:
        largest = right
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, largest)


def build_max_heap(a):
    heap_size = len(a)
    for i in reversed(range(0, heap_size // 2)):
        max_heapify(a, i)


def main():
    _ = int(input())
    a = list(map(int, input().split()))
    build_max_heap(a)
    for it in a:
        print(' {}'.format(it), end='')
    print()


if __name__ == '__main__':
    main()

