# Queue

class MyQueue:
    def __init__(self):
        self.queue = [] # list
        self.top = 0
    
    def isEmpty(self):
        if self.top==0:
            return True
        return False
    
    def isFull(self):
        pass

    def enqueue(self, x):
        self.queue.append(x)
        self.top += 1
    
    def dequeue(self):
        if self.top>0:
            self.top -= 1            
            return self.queue.pop(0)
        else:
            print("there aren't enough values in Queue")

def main():
    n, q = map(int, input().split())
    A = [
        list(map(lambda x: int(x) if x.isdigit() else x, input().split()))
        for i in range(n)
    ]
    A = [{'name': name, 'time': time} for name, time in A]
    queue = MyQueue()
    for a in A:
        queue.enqueue(a)
    elapsed = 0
    while not queue.isEmpty():        
        job = queue.dequeue()        
        if job['time']>q:
            elapsed += q
            job['time'] = job['time'] - q
            queue.enqueue(job)
        else:
            elapsed += job['time']
            print(job['name']+ ' ' + str(elapsed))

main()
