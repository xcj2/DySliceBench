class Process(object):
    def __init__(self, name, s):
        self.name = name
        self.s = s

    def exec(self, q):
        if self.s <= q:
            time = self.s
            self.s = 0
            return time
        else:
            time = q
            self.s = self.s - q
            return time

def execute(processes, q):
    time = 0
    completed = []
    while processes:
        p = processes.pop()
        time += p.exec(q)
        if p.s == 0:
            completed.append((p, time))
        else:
            processes.insert(0, p)
    return completed

def run():
    n, q = list(map(int, input().split()))
    processes = []
    for _ in range(n):
        name, time = input().split()
        processes.append(Process(name, int(time)))
    processes.reverse()
    completed = execute(processes, q)
    for c in completed:
        print(c[0].name, c[1])

if __name__ == '__main__':
    run()


