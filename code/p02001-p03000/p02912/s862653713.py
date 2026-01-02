def d_powerful_discount_tickets():
    import heapq
    N, M = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]

    # 参考: https://juppy.hatenablog.com/entry/2019/04/05/蟻本_Python_プライオリティキュー_2_heapq_競技プログラミン
    def _heappush_max(heap, item):
        heap.append(item)
        heapq._siftdown_max(heap, 0, len(heap) - 1)

    def _heappop_max(heap):
        """Maxheap version of a heappop."""
        lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
        if heap:
            returnitem = heap[0]
            heap[0] = lastelt
            heapq._siftup_max(heap, 0)
            return returnitem
        return lastelt

    heapq._heapify_max(A)
    for _ in range(M):
        _heappush_max(A, _heappop_max(A) // 2)
    return sum(A)

print(d_powerful_discount_tickets())