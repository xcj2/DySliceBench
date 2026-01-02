"""
キューのデータ構造の定義
"""

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, num):
        self.queue.append(num)

    def dequeue(self):
        return self.queue.pop(0)

    def exist(self):
        if len(self.queue) > 0:
            return True
        else:
            return False

class Process():
    def __init__(self, name, time):
        self.name = name
        self.time = time
    
    def execute(self, q):
        self.time -= q
        if self.time <= 0:
            return True, self.time+q
        else:
            return False, q

if __name__=="__main__":
    n, q = [int(i) for i in input().split()]
    queue = Queue()
    for i in range(n):
        name, time = [s for s in input().split()]
        queue.enqueue(Process(name, int(time)))

    total_execute_time = 0
    while queue.exist():
        p = queue.dequeue()
        is_finish, execute_time = p.execute(q)
        total_execute_time += execute_time
        if is_finish:
            print("{} {}".format(p.name, total_execute_time))
        else:
            queue.enqueue(p)

