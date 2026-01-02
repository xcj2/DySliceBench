import sys
input = sys.stdin.readline
import heapq

def suc(s):
    return s + str(int(s[-1]) + 1)

def prev(s):
    return s + str(int(s[-1]) - 1)

def f(k):
    pq = list(range(1, 10))
    heapq.heapify(pq)
    i = 0
    while i < k:
        a = heapq.heappop(pq)
        yield a

        i += 1
        a_ = str(a)
        if a_[-1] < "9":
            down = int(suc(a_))
            heapq.heappush(pq, down)

        if a_[-1] > "0":
            up = int(prev(a_))
            heapq.heappush(pq, up)

        flat = int(a_ + a_[-1])
        heapq.heappush(pq, flat)

def main():
    k = int(input())
    ans = list(f(k))
    print(ans[-1])




main()