class Process:
    def __init__(self, data):
        self.name = data[0]
        self.time = int(data[1])

    def process(self, quantum):
        if self.time <= quantum:
            time, self.time = self.time, 0
            return time

        self.time -= quantum
        return quantum

    def isProcessed(self):
        return self.time == 0

    def getName(self):
        return self.name

def main():
    n, q = map(int, input().split())

    queue = []
    for _ in range(n):
        queue.append(Process(input().split()))

    elapsed = 0
    while len(queue) > 0:
        p = queue.pop(0)
        elapsed += p.process(q)

        if p.isProcessed():
            print('{} {}'.format(p.getName(), elapsed))
        else:
            queue.append(p)

if __name__ == '__main__':
    main()

