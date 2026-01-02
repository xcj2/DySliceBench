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

    X, Y, A, B, C = map(int, input().split())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    r = list(map(int, input().split()))

    AB = sorted(p, reverse=True)[:X] + sorted(q, reverse=True)[:Y]
    ans = sum(AB)
    AB_q = PriorityQueue(AB)
    ab_now = AB_q.pop()

    for r_ in r:
        if r_ > ab_now:
            ans = ans - ab_now + r_
            AB_q.push(r_)
            ab_now = AB_q.pop()
    print(ans)


if __name__ == '__main__':
    main()
