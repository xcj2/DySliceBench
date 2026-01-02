def Initialize(head, tail):
    head, tail = 0, 0
    return head, tail

def IsEnpty(head, tail):
    return head == tail

def IsFull(head, tail):
    global MAX
    return head == (tail + 1) % MAX

def Enqueue(Q, x, y, head, tail):
    global MAX
    if IsFull(head, tail):
        return None
    Q[tail][0], Q[tail][1] = x, y
    if tail + 1 == MAX:
        tail = 0
    else:
        tail += 1
    return head, tail

def Dequeue(Q, head, tail):
    global MAX
    if IsEnpty(head, tail):
        return None
    x, y = Q[head][0], Q[head][1]
    if head + 1 == MAX:
        head = 0
    else:
        head += 1
    return x, y, head, tail

n, q = map(int, input().split())
MAX = n + 2
Q = [['', 0] for _ in range(MAX)]
head, tail = 0, 0
result = []
z = 0
for i in range(n):
    x, y = input().split()
    head, tail = Enqueue(Q, x, int(y), head, tail)
while IsEnpty(head, tail) != True:
    if Q[head][1] <= q:
        x, y, head, tail = Dequeue(Q, head, tail)
        result.append([x, y + z])
        z += y
    else:
        Q[head][1] -= q
        x, y, head, tail = Dequeue(Q, head, tail)
        head, tail = Enqueue(Q, x, y, head, tail)
        z += q
for i in range(n):
    print(*result[i], sep=' ')
