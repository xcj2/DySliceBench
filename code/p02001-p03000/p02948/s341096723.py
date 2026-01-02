from heapq import heappush as hpush
from heapq import heappop as hpop

class Descending_HeapQueue:
    def __init__(self, hq=[]):
        self.hq = []
        for i in hq:
            self.push(i)
    def push(self, n):
        hpush(self.hq, -n)
    def pop(self):
        return -hpop(self.hq)
    def __len__(self):
        return len(self.hq)

def main():
    N, M = map(int, input().split())
    AB = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])
    ans = 0
    dhq = Descending_HeapQueue()
    pointer = 0
    for m in range(1, M+1):
        while (pointer < N) and (AB[pointer][0] <= m):
            dhq.push(AB[pointer][1])
            pointer += 1
        if len(dhq) > 0:
            ans += dhq.pop()
    print(ans)
main()