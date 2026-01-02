# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_B&lang=jp

class Queue(object):
    def __init__(self):
        self.list = []

    def enqueue(self, x):
        self.list.append(x)
    
    def dequeue(self):
        return self.list.pop(0)
    
    def isEmpty(self):
        return len(self.list) == 0


def main():
    n, q = map(int, input().split(" "))
    que = Queue()

    jobs = [input().split(' ') for _ in range(n)]


    for job in jobs:
        que.enqueue([job[0], int(job[1])])

    total = 0
    while not que.isEmpty():
        # print(que.list)

        name, time = que.dequeue()

        nokori = time - q
        if nokori > 0:
            total += q
            que.enqueue([name, nokori])
        else:
            total += time
            print(name, total)




main()
