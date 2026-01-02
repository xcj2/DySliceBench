# -*- coding: utf-8 -*-
# Queue


class Process:
    def __init__(self, line):
        self.name = line[0]
        self.time = int(line[1])


LEN = 100000
n = 0
head = 0
tail = 0
Q = [0] * LEN


def enqueue(x):
    global tail
    Q[tail] = x
    tail = (tail + 1) % LEN

def dequeue():
    global head
    x = Q[head]
    head = (head + 1) % LEN
    return x


def main():
    n, q = map(int, input().split())
    ps = [Process(input().split()) for _ in range(n)]
    for p in ps:
        enqueue(p)

    global head, tail

    elaps = 0
    while(head != tail):
        u = dequeue()
        c = min(q, u.time)
        u.time -= c
        elaps += c
        if u.time > 0:
            enqueue(u)
        else:
            print(u.name, elaps)

if __name__ == '__main__':
    main()

