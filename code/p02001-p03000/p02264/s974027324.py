import sys
MAX = 100005
n, q = map(int, input().split())

def initialize():
    head = tail = 0
    return head, tail

def isEmpty(head, tail):
    return head == tail

def isFull(head, tail):
    return head == (tail + 1) % MAX

def enqueue(x, head, tail):
    if isFull(head, tail):
        print('Error')
        sys.exit()
    Q[tail] = x
    if tail + 1 == MAX:
        tail = 0
    else:
        tail += 1
    return tail

def dequeue(head, tail):
    if isEmpty(head, tail):
        sys.exit()
    x = Q[head]
    if head + 1 == MAX:
        head = 0
    else:
        head += 1
    return x, head

head, tail = initialize()
Q = [0] * MAX
for _ in range(n):
    name, time = map(str, input().split())
    time = int(time)
    tail = enqueue([name, time], head, tail)
T = 0
while True:
    Qi, head = dequeue(head, tail)
    name = Qi[0]
    time = Qi[1]
    if time <= q:
        T += time
        print(name, T)
    else:
        T += q
        time -= q
        tail = enqueue([name, time], head, tail)

