input_list = list(map(int, input().split()))
n, q = input_list

LEN = 100005
process_list = [None] * LEN
head = 1
tail = n + 1
elaps = 0

class Process:
    def __init__(self, name, time):
        self.name = name
        self.t = time
        
def enqueue(x):
    global process_list, tail
    process_list[tail] = x
    tail = (tail + 1) % LEN
    
def dequeue():
    global process_list, head
    x = process_list[head]
    head = (head + 1) % LEN
    return x
    
def min(a, b):
    a = int(a)
    b = int(b)
    return a if a <= b else b

for i in range(1, n + 1):
    input_list = list(input().split())
    name, time = input_list
    process_list[i] = Process(name, time)

# start simulationing
while head != tail:
    u = dequeue()
    c = min(q, u.t)
    u.t = int(u.t) - c
    elaps += c
    if int(u.t) > 0:
        enqueue(u);
    else:
        print('{} {}'.format(u.name, elaps))
