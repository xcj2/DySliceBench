Q = []
MAX = 100000
head = 0
tail = 0

class Process:
    def __init__(self):
        self.name = ''
        self.time = 0

def enqueue(x):
    global tail
    Q[tail] = x
    if tail + 1 == MAX:
        tail = 0
    else:
        tail += 1

def dequeue():
    global head
    x = Q[head]
    if head + 1 == MAX:
        head = 0
    else:
        head += 1
    return x

def main():
    input_line = input().split(" ")
    n = int(input_line[0])
    qtime = int(input_line[1])

    for _ in range(MAX):
        Q.append(None)

    for _ in range(n):
        v = input().split(' ')
        p = Process()
        p.name = v[0]
        p.time = int(v[1])
        enqueue(p)
    
    elaps = 0
    while head != tail:
        p = dequeue()
        t = min(qtime, p.time)
        p.time -= t
        elaps += t
        if p.time > 0:
            enqueue(p)
        else:
            print(p.name + " " + str(elaps))

if __name__ == "__main__":
    main()
