class Process():

    def __init__(self, data):
        self.name = data[0]
        self.time = int(data[1])
        self.endtime = 0

    def process(self, time):
        process_time = min(time, self.time)
        self.time -= process_time
        return process_time

    def is_done(self):
        return self.time <= 0


class MyQueue():

    def __init__(self, max):
        self.Q = [None for _ in range(max)]
        self.head = 0
        self.tail = 0
        self.max = max

    def enqueue(self, x):
        if self.is_full():
            raise ValueError
        self.Q[self.tail] = x
        self.tail += 1
        if self.tail == self.max:
            self.tail = 0

    def dequeue(self):
        if self.is_empty():
            raise IndexError
        ret = self.Q[self.head]
        self.head += 1
        if self.head == self.max:
            self.head = 0
        return ret

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return self.head == (self.tail + 1) % self.max

def main():
    n, q = map(int, input().split())
    queue = MyQueue(n + 1)
    current_time = 0
    done = []
    [queue.enqueue(Process(input().split())) for i in range(n)]

    while True:
        try:
            p: Process = queue.dequeue()
        except IndexError:
            break
        process_time = p.process(q)
        current_time += process_time
        if p.is_done():
            p.endtime = current_time
            done.append(p)
        else:
            queue.enqueue(p)

    [print(p.name, p.endtime, sep=" ") for p in done]

if __name__ == "__main__":
    main()

