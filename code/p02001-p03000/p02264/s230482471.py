class My_Queue:

    def __init__(self, S):
        self.S = S
        self.q = [0 for i in range(S)]
        self.head = 0
        self.tail = 0

    def enqueue(self, x):
        if self.isFull():
            print('overflow')
            raise
        else:
            self.q[self.tail] = x

            if self.tail + 1 == self.S:
                self.tail = 0
            else:
                self.tail += 1

    def dequeue(self):
        if self.isEmpty():
            print('underflow')
            raise
        else:
            x = self.q[self.head]
            self.q[self.head] = 0

            if self.head + 1 == self.S:
                self.head = 0
            else:
                self.head += 1
            return x

    def isEmpty(self):
        return self.head == self.tail

    def isFull(self):
        return self.head == (self.tail + 1) % self.S


def main():
    n, qms = map(int, input().split())
    elapsed_time = 0
    q = My_Queue(n + 1)
    for i in range(n):
        name, time = input().split()
        time = int(time)

        q.enqueue([name, time])

    while(q.head != q.tail):
        a = q.dequeue()
        if a[1] <= qms:
            elapsed_time += a[1]
            print(a[0], elapsed_time)
        else:
            a[1] -= qms
            elapsed_time += qms
            q.enqueue(a)

if __name__ == "__main__":
    main()