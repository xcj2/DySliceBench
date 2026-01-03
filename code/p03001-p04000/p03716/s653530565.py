from heapq import heapify, heappop, heappush, heappushpop


class PriorityQueue:
    def __init__(self, heap):
        self.heap = heap
        heapify(self.heap)

    def push(self, item):
        heappush(self.heap, item)

    def pop(self):
        return heappop(self.heap)

    def pushpop(self, item):
        return heappushpop(self.heap, item)

    def __call__(self):
        return self.heap

    def __len__(self):
        return len(self.heap)


def main():
    N = int(input())
    a = list(map(int, input().split()))

    first_half = PriorityQueue(a[:N])
    second_half = PriorityQueue(list(map(lambda x: -x, a[2 * N:])))
    f_max, s_min = [0] * (N + 1), [0] * (N + 1)
    f_max[0], s_min[-1] = sum(a[:N]), sum(a[2 * N:])

    for k in range(N):
        first_half.push(a[k + N])
        f_max[k + 1] = f_max[k] + a[k + N] - first_half.pop()
        second_half.push(-a[-N - 1 - k])
        s_min[N - 1 - k] = s_min[N - k] + a[-N - 1 - k] + second_half.pop()

    ans = -float('inf')
    for k in range(N + 1):
        if ans < f_max[k] - s_min[k]:
            ans = f_max[k] - s_min[k]
    print(ans)


if __name__ == '__main__':
    main()
