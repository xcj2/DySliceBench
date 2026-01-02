class a(object):
    def __init__(self, buf_size=10000000):
        self.m = [None for _ in range(buf_size)]
        self.ind = 0
        self.cur = 0

    def enqueue(self, elem):
        self.m[self.ind] = elem
        self.ind += 1

    def dequeue(self):
        if self.is_empty(): raise EOFError('this queue is empty')
        result = self.m[self.cur]
        self.cur += 1
        return result

    def is_empty(self):
        return self.ind <= self.cur

n, q = input().split()
qe = a()
cur_time = 0

for _ in range(int(n)):
    name, time = input().split()
    qe.enqueue((name, int(time)))

while not qe.is_empty():
    name, time = qe.dequeue()
    if time > int(q):
        cur_time += int(q)
        time -= int(q)
        qe.enqueue((name, time))
    else:
        cur_time += int(time)
        print('{} {}'.format(name, cur_time))
