def parse(l):
    name, time = l.split()
    a = [name, int(time)]
    return a


n, quantum = map(int, input().split())
queue = []
for i in range(n):
    queue.append(parse(input()))
head = 0


def enqueue(x):
    global queue
    queue.append(x)


def dequeue():
    global head
    head += 1


total_time, count = 0, 0
while count < n:
    y = queue[head][1] - quantum
    if y <= 0:
        print(str(queue[head][0]) + " " + str(total_time + queue[head][1]))
        dequeue()
        total_time += y
        count += 1
    else:
        queue[head][1] -= quantum
        enqueue(queue[head])
        dequeue()

    total_time += quantum

