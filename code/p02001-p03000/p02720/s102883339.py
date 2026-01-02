import sys

MAX = 1000000
Q = [0] * MAX
head = 0
tail = 0

def isEmpty():
    return head == tail

def isFull():
    return head == (tail + 1) % MAX

def enqueue(x):
    global tail
    if isFull():
        print("オーバーフロー")
        sys.exit()
    Q[tail] = x
    if tail + 1 == MAX:
        tail = 0
    else:
        tail += 1

def dequeue():
    global head
    if isEmpty():
        print("アンダーフロー")
        sys.exit()
    x = Q[head]
    if head + 1 == MAX:
        head = 0
    else:
        head += 1
    return x

k = int(input())

for i in range(1,10):
    enqueue(i)

for i in range(k):
    x = dequeue()
    b = x % 10
    if b != 0:
        enqueue(10 * x + b - 1)
    enqueue(10 * x + b)
    if b != 9:
        enqueue(10 * x + b + 1)
print(x)