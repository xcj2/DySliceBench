n,q = map(int, input().split())
n += 1
list_queue = []
def initialize(head,tail):
    head = 0
    tail = 0
    return (head,tail)
def enqueue(Q,MAX,head,tail,x):
    Q[tail] = x
    if tail + 1 == MAX:
        tail = 0
    else:
        tail += 1
    return (head, tail)
def dequeue(Q,MAX,head,tail):
    x = Q[head]
    if head + 1 == MAX:
        head = 0
    else:
        head += 1
    return (x,head,tail)

head = 0
tail = 0
list_queue = [0] * n
for i in range(0,n-1):
    head, tail = enqueue(list_queue,n,head,tail,list((map(str, input().split()))))
ans = 0

list_zero = []
for i in range(0,n):
    list_zero.append(0)
#while True:
while (head != tail):
    x,head,tail = dequeue(list_queue,n,head,tail)
    if int(x[1]) <= q:
        ans += int(x[1])
        x[1] = 0
        print(x[0], ans)
    else:
        ans += q
        x[1] = int(x[1]) - q
        head, tail = enqueue(list_queue,n,head,tail,x)
