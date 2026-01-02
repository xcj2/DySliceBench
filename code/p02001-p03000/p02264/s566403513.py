## import sys

class queue:
    def __init__(self, length):
        self.max = length + 2
        self.v = list(range(self.max))
        self.head = 0
        self.tail = 0
        
    def enqueue(self, x):
        self.v[self.tail] = x
        self.tail = (self.tail+1) % self.max
        
    def dequeue(self):
        a = self.v[self.head]
        self.head = (self.head+1) % self.max
        
        return a
    
    
    def isEmpty(self):
        return self.head == self.tail
    
    def isFull(self):
        return (self.tail - self.head) == self.length
    
    
def main():
    n, q = list(map(int,input().split()))
    que = queue(n)
    for _ in range(n):
        lis = input().split()
        lis[1] = int(lis[1])
        
        que.enqueue(lis)
    
    time = 0
    while n > 0:
        now = que.dequeue()
        if now[1] > q:
            now[1] -= q
            que.enqueue(now)
            time += q
            
        else:
            time += now[1]
            print(now[0], time)
            n -= 1
            
if __name__ == '__main__':
    main()
