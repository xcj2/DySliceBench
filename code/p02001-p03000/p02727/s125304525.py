import sys
class Heap:
    def __init__(self):
        self.heap = [None]*1000000
        self.root = 0
        self.size = 0
    
    def push(self, a:int):
        self.heap[self.size] = a
        b = self.size
        while b != 0 and self.heap[(b - 1) //2] < self.heap[b]:
            c = self.heap[(b - 1) //2]
            self.heap[(b - 1) //2] = self.heap[b]
            self.heap[b] = c
            b = (b - 1) //2
        self.size += 1
    
    def pop(self):
        a = self.heap[0]
        b = 0
        self.heap[b] = self.heap[self.size - 1]
        self.heap[self.size] = None
        self.size -= 1
        while (self.heap[b*2 + 1] is not None and self.heap[b] < self.heap[b*2 + 1]) or (self.heap[b*2 + 2] is not None and self.heap[b] < self.heap[b*2 + 2]):
            if self.heap[b*2 + 2] > self.heap[b*2 + 1]:
                c = self.heap[b]
                self.heap[b] = self.heap[b*2 + 2]
                self.heap[b*2 + 2] = c
                b = b*2 + 2
            else:
                c = self.heap[b]
                self.heap[b] = self.heap[b*2 + 1]
                self.heap[b*2 + 1] = c
                b = b*2 + 1
        return a
def main(): 
    x, y, A, B, C = map(int, input().split())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    r = list(map(int, input().split()))
    pq = Heap()
    p.sort()
    q.sort()
    for i in range(x):
        pq.push(p[len(p) - 1 - i])
    for i in range(y):
        pq.push(q[len(q) - 1 - i])
    for i in range(len(r)):
        pq.push(r[i])
    ans = 0
    for i in range(x + y):
        ans += pq.pop()
    print(ans)

main()
