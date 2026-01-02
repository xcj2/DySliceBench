# Queue キュー
class Queue():
    def __init__(self, size):
        self.size = size
        self.Q = [None for i in range(size)]
        self.top = 0
        self.btm = 0
    
    def enqueue(self, x):
        self.Q[self.btm] = x;
        self.btm += 1;
        if self.btm >= self.size:
            self.btm = 0
    
    def dequeue(self):
        ret = self.Q[self.top]
        self.Q[self.top] = None
        self.top += 1
        if self.top >= self.size:
            self.top = 0
        return ret
    
    def __repr__(self):
        list(self.Q)
    
class Process():
    def __init__(self, name, time):
        self.name = name
        self.time = time
    
    def getname(self):
        return self.name
    
    def proceed(self, q):
        if q <= self.time:
            self.time -= q
            return q;
        elif q > self.time:
            ret = self.time
            self.time = 0
            return ret
    
    def isFinished(self):
        return self.time == 0
    
    def __repr__(self):
        return self.name + " " + str(self.time)

n, q = (int(i) for i in input().split())
Q = Queue(n)
for i in range(0,n):
    data = input().split()   
    name = data[0]
    time = int(data[1])
    Q.enqueue(Process(name, time))
timeelapsed = 0
while True:
    p = Q.dequeue()
    if p == None:
        break
    timeelapsed += p.proceed(q)
    if p.isFinished():
        print(p.getname(), timeelapsed)
    else:
        Q.enqueue(p)

