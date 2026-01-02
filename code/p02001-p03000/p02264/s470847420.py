n,qtm = map(int, input().split())

class Process:
  def __init__(self, name, time):
    self.name = name
    self.time = time

class Queue:
  def __init__(self, length):
    self.q = [Process('p0', 0)]*length
    self.MAX = length
    self.head = 0
    self.tail = 0
  
  def enqueue(self, x):
    self.q[self.tail] = x
    if self.tail+1 == self.MAX:
      self.tail = 0
    else:
      self.tail += 1 
  
  def dequeue(self):
    x = self.q[self.head]
    if self.head + 1 == self.MAX:
      self.head = 0
    else: 
      self.head += 1
    return x
  
  def isEmpty(self):
    if self.head == self.tail:
      return True
    else:
      return False

  def isFull(self):
    if self.head == (self.tail+1)%self.MAX:
      return True
    else:
      False


Q = Queue(100000) 

for _ in range(n):
  x,y = map(str, input().split())
  tmp = Q.enqueue(Process(x,int(y)))

time = 0
while not Q.isEmpty():
  qtop = Q.dequeue()
  if qtop.time > qtm:
    time += qtm
    qtop.time -= qtm
    Q.enqueue(qtop) 
  else:
    time += qtop.time
    qtop.time = 0
    print(qtop.name + ' ' + str(time))


