import heapq
import sys
input = sys.stdin.readline


def _heappush_max(heap, item):
    heap.append(item)
    heapq._siftdown_max(heap, 0, len(heap)-1)


def _heappop_max(heap):
    """Maxheap version of a heappop."""
    lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        heapq._siftup_max(heap, 0)
        return returnitem
    return lastelt


def main():
    n, m = map(int, input().split())

    if n == 1:
        a = int(input())
        for i in range(m):
            a //= 2
        print(a)
        exit()

    a = (list(map(int, input().split())))
    heapq._heapify_max(a)

    for i in range(m):
        tmp = _heappop_max(a) // 2
        _heappush_max(a, tmp)

    print(sum(a))


if __name__ == '__main__':
    main()
