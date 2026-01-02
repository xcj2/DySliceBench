class Queue(object):
    def __init__(self, _max):
        if type(_max) != int:
            raise ValueError
        self._array = [None for i in range(0, _max)]
        self._head = 0
        self._tail = 0
        self._cnt = 0

    def enqueue(self, value):
        if self.is_full():
            raise IndexError
        self._array[self._head] = value
        self._cnt += 1
        if self._head + 1 >= len(self._array):
            self._head = 0
        else:
            self._head += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError
        value = self._array[self._tail]
        self._cnt -= 1
        if self._tail + 1 >= len(self._array):
            self._tail = 0
        else:
            self._tail += 1
        return value

    def is_empty(self):
        return self._cnt <= 0

    def is_full(self):
        return self._cnt >= len(self._array)


def round_robin(quantum, jobs):
    queue = Queue(100000)
    total = 0
    for job in jobs:
        queue.enqueue(job)

    while not queue.is_empty():
        name, time = queue.dequeue()
        if time > quantum:
            total += quantum
            queue.enqueue((name, time - quantum))
        else:
            total += time
            print("{0} {1}".format(name, total))


if __name__ == "__main__":
    n, quantum = input().split()
    jobs = [input().split() for i in range(0, int(n))]
    jobs = [(job[0], int(job[1])) for job in jobs]
    round_robin(int(quantum), jobs)