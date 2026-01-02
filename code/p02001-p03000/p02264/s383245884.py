class Queue:
    def __init__(self, n):
        self.n = n + 1
        self.array = [0]*self.n
        self.head = 0
        self.tail = 0

    def enqueue(self, x):
        if not self.isfull():
            self.array[self.tail] = x
            self.tail += 1
            self.tail = self.tail % self.n
        else:
            raise ValueError

    def dequeue(self):
        if not self.isempty():
            val = self.array[self.head]
            self.head += 1
            self.head = self.head % self.n
            return val
        else:
            return False

    def isempty(self):
        return self.head == self.tail

    def isfull(self):
        return (self.tail+1) % self.n == self.head


def main():
    n, q = map(int, input().split())
    queue = Queue(n)
    time = 0

    for _ in range(n):
        query = input().split()
        queue.enqueue(query)

    task = True
    while not queue.isempty():
        task = queue.dequeue()
        if int(task[1]) > q:
            time += q
            tmp_time = int(task[1]) - q
            task = [task[0], tmp_time]
            queue.enqueue(task)
        else:
            time += int(task[1])
            print(task[0], time)


if __name__ == "__main__":
    main()

