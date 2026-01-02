class Queue():
    def __init__(self, size=10):
        self.queue = [None] * size
        self.head = self.tail = 0
        self.MAX = size
        self.num_items = 0

    def is_empty(self):
        return self.num_items == 0

    def is_full(self):
        return self.num_items == self.MAX

    def enqueue(self, x):
        if self.is_full():
            raise IndexError

        self.queue[self.tail] = x
        self.num_items += 1
        if self.tail+1 == self.MAX:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError

        x = self.queue[self.head]
        self.num_items -= 1
        if self.head+1 == self.MAX:
            self.head = 0
        else:
            self.head += 1

        return x


class Process:
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def print_time(self):
        return self.time

    def print_name(self):
        return self.name


def main():
    n, q = map(int, input().split())
    qq = Queue(n)

    t = 0
    for i in range(n):
        name, time = input().split()
        p = Process(name, int(time))
        qq.enqueue(p)

    while not qq.is_empty():
        p = qq.dequeue()

        if p.time - q <= 0:
            t += p.time
            print("{} {}".format(p.name, t))
        else:
            p.time -= q
            t += q
            qq.enqueue(p)


if __name__ == '__main__':
    main()

