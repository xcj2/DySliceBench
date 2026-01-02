from collections import namedtuple

Task = namedtuple('Task', 'name time')

class Queue:
    def __init__(self, n):
        self.n = n
        self._l = [None for _ in range(self.n + 1)]
        self._head = 0
        self._tail = 0

    def enqueue(self, x):
        self._l[self._tail] = x
        self._tail += 1
        if self._tail > self.n:
            self._tail -= self.n

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("pop from empty queue")
        else:
            e = self._l[self._head]
            self._l[self._head] = None
            self._head += 1
            if self._head > self.n:
                self._head -= self.n
            return e

    def isEmpty(self):
        return self._head == self._tail

    def isFull(self):
        return self._tail == self.n

if __name__ == '__main__':
    n, q = map(int, input().split())
    queue = Queue(n+1)
    for _ in range(n):
        name, time = input().split()
        time = int(time)
        queue.enqueue(Task(name=name, time=time))

    now = 0
    while not queue.isEmpty():
        task = queue.dequeue()
        t = task.time
        if t <= q:
            now += t
            print(task.name, now)
        else:
            now += q
            queue.enqueue(Task(task.name, t - q))

