s = input().split(" ")
n = int(s[0])
q = int(s[1])

class Process:
    def __init__(self, name, time):
        self.name = name
        self.time = time

queue = []

for i in range(n):
    t = input().split(" ")
    queue.append(Process(t[0], int(t[1])))
   
head = 0
tail = n-1

def dequeue():
    global head
    x = queue[head]
    head = (head + 1) % n
    return x
    
def enqueue(x):
    global tail
    tail = (tail + 1) % n
    queue[tail] = x

time = 0

while head != tail:
    w = dequeue()
    if w.time > q:
        w.time = w.time - q
        time = time + q
        enqueue(w)
    else:
        time = time + w.time
        print("{0} {1}".format(w.name, time))
print("{0} {1}".format(queue[head].name, time+queue[head].time))