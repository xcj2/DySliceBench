class Queue:
    _items = []
    _capacity = 0
    _head = 0
    _tail = 0

    def __init__(self, cap):
        self._capacity = cap + 1
        for i in range(self._capacity):
            self._items.append(None)

    def enqueue(self, val):
        index = (self._tail + 1)%self._capacity
        if index == self._head:
            raise Exception('Queue is full')
        self._items[self._tail] = val
        self._tail = index

    def dequeue(self):
        if self._head == self._tail:
            raise Exception('Queue is empty')
        val = self._items[self._head]
        self._items[self._head] = None
        self._head = (self._head + 1)%self._capacity
        return val

    def is_empty(self):
        return  self._head == self._tail
        


class Task:
    name = ''
    time = 0

    def __init__(self, name, time):
        self.name = name
        self.time = time

    def __str__(self):
        return '%s %d'%(self.name, self.time)

if __name__ == '__main__':
    N, p = map(int, input().split())

    tasks = Queue(N)
    finished_tasks = []
    total_time = 0  

    for i in range(N):
        n, t = input().split()
        tasks.enqueue(Task(n, int(t)))

    while not tasks.is_empty():
        cur = tasks.dequeue()
        if cur.time <= p:
            total_time += cur.time
            cur.time = total_time
            finished_tasks.append(cur)
        else:
            total_time += p
            cur.time -=p
            tasks.enqueue(cur)

    for i in finished_tasks:
        print(i)
