class Process:

    def __init__(self, name, time):
        self.name = name
        self.time = time

    def execute(self, q):
        if self.time == 0:
            raise RuntimeError
        execution_time = min(self.time, q)
        self.time -= execution_time
        return execution_time

    def is_ended(self):
        return self.time == 0


class Queue:

    def __init__(self):
        self.head = 0
        self.tail = 0
        self.queue = [0] * 100005

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return self.head == (self.tail + 1) % len(self.queue)

    def enqueue(self, x):
        self.queue[self.tail] = x
        if self.tail + 1 == len(self.queue):
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError
        x = self.queue[self.head]
        if self.head + 1 == len(self.queue):
            self.head = 0
        else:
            self.head += 1
        return x


def main():
    # input
    n, q = list(map(int, input().split(' ')))
    processes = []
    for _ in range(n):
        name, time = input().split(' ')
        processes.append(Process(name, int(time)))
    Q = Queue()
    for process in processes:
        Q.enqueue(process)

    # execute
    elapsed_time = 0
    while not Q.is_empty():
        process = Q.dequeue()
        elapsed_time += process.execute(q)
        if process.is_ended():
            print(process.name, elapsed_time)
        else:
            Q.enqueue(process)


if __name__ == "__main__":
    main()

