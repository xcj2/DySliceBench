import sys, math
import heapq
class Heapq:
    def __init__(self, arr, desc=False):
        if desc:
            arr = [-a for a in arr]
        self.sign = -1 if desc else 1
        self.hq = arr
        heapq.heapify(self.hq)

    def pop(self):
        return heapq.heappop(self.hq) * self.sign

    def push(self, a):
        heapq.heappush(self.hq, a * self.sign)

    def top(self):
        return self.hq[0] * self.sign

def main():
    def input():
        return sys.stdin.readline()[:-1]
    N, M = map(int,input().split())
    A = sorted(list(map(int,input().split())))[::-1]
    Q = Heapq(A, True)
    for k in range(M):
        now = Q.pop()
        Q.push(now//2)
    ans = 0
    for k in range(N):
        ans += Q.pop()
    print(ans)
if __name__ == '__main__':
    main()
