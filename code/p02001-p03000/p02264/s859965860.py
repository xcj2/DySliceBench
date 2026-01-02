# -*- coding: utf 8 -*-
# Queue
# 2019. 4/25

LEN = 100005
Q = [0] * LEN
head = 0
tail = 0

class Queue:
    def __init__(self):
        self.name = 0
        self.t = 0

def enqueue(x):
    global tail
    Q[tail] = x
    tail = (tail + 1) % LEN

def dequeue():
    global head
    x = Q[head]
    head = (head + 1) % LEN
    return x

if __name__ == '__main__':
    elaps = 0
    n, q = map(int, input().split())
    for i in range(1, n + 1):
        u = Queue()
        name , time = input().split()
        u.name = name
        u.t = int(time)
        Q[i] = u

    head = 1
    tail = n + 1

    while(head != tail):
        u = dequeue()
        c = min(q, u.t)
        u.t -= c
        elaps += c
        if( u.t > 0):
            enqueue(u)
        else:
            print("{} {}".format(u.name, elaps))

