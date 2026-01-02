def max_heapify(a, i):
    h = len(a)
    l = 2 * i
    r = 2 * i + 1
    if l <= h and a[l - 1] > a[i - 1]:
        largest = l
    else:
        largest = i
    if r <= h and a[r - 1] > a[largest - 1]:
        largest = r

    if largest != i:
        tmp = a[i - 1]
        a[i - 1] = a[largest - 1]
        a[largest - 1] = tmp
        max_heapify(a, largest)


def build_max_heap(a):
    h = len(a)
    for i in range(h // 2, 0, -1):
        max_heapify(a, i)


def print_list_split_whitespace(a):
    s = ""
    for x in a:
        s += " " + str(x)
    print(s)


h = int(input())
heap = [int(x) for x in input().split()]

build_max_heap(heap)

print_list_split_whitespace(heap)
