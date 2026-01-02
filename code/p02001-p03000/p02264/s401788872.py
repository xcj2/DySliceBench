class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)

class Task:
    def __init__(self, name, time):
        self.name = name
        self.time = int(time)
        self.endtime = 0

    def __repr__(self):
        return '{} {}'.format(self.name, self.endtime)


def rr(queue, q):
    time = 0
    while len(queue.queue) > 0:
        task = queue.dequeue()
        if task.time > q:
            task.time -= q
            time += q
            queue.enqueue(task)
        else:
            time += task.time
            task.time = 0
            task.endtime = time
            print(task)

if __name__ == '__main__':
    nq = [int(s) for s in input().split()]
    N = nq[0]
    q = nq[1]
    queue = Queue()
    task_arr = [Task(*input().split()) for i in range(N)]
    for t in task_arr:
        queue.enqueue(t)
    rr(queue, q)