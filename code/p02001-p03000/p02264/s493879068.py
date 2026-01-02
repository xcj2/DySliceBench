class Queue():
    def __init__(self):
        self.queue = [None] * 100000
        self.head = 0
        self.tail = 0
        self.max_queue = len(self.queue)

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return self.head == (self.tail + 1) % self.max_queue

    def enqueue(self, x):
        if self.is_full():
            raise ValueError("Error: Full!")

        self.queue[self.tail] = x

        if self.tail + 1 == self.max_queue:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Error: Empty!")

        x = self.queue[self.head]

        if self.head + 1 == self.max_queue:
            self.head = 0
        else:
            self.head += 1
        return x


process_name = Queue()
process_cost = Queue()

n, q = map(int, input().split())

for i in range(n):
    name, time = input().split()
    time = int(time)

    process_name.enqueue(name)
    process_cost.enqueue(time)

at_time = 0
while not process_name.is_empty():
    name = process_name.dequeue()
    cost = process_cost.dequeue()
    if cost > q:
        process_name.enqueue(name)
        process_cost.enqueue(cost - q)
        at_time += q
    else:
        at_time += cost
        print(f"{name} {at_time}")
        pass

    pass





