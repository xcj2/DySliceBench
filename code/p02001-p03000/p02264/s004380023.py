class Queue():
  def __init__(self, max=100):
    self.head = self.tail = 0
    self.max = max
    self.arr = [None for _ in range(max)]
  
  def is_empty(self):
    return self.head == self.tail

  def is_full(self):
    return self.head == (self.tail + 1) % self.max

  def enqueue(self, x):
    if self.is_full():
      raise IndexError()
    self.arr[self.tail] = x
    if self.tail + 1 == self.max:
      self.tail = 0
    else:
      self.tail += 1
  
  def dequeue(self):
    if self.is_empty():
      raise IndexError()
    x = self.arr[self.head]
    if self.head + 1 == self.max:
      self.head = 0
    else:
      self.head += 1
    return x

n, q = map(int, input().split())

ps = Queue(100000)
for _ in range(n):
  name, time = input().split()
  ps.enqueue([name, int(time)])

elasp = 0
while not ps.is_empty():
  p = ps.dequeue()
  c = min(q, p[1])
  p[1] -= c
  elasp += c
  if p[1] > 0:
    ps.enqueue(p)
  else:
    print(p[0], elasp)

