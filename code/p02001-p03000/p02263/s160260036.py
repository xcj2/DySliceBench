class Stack():
  def __init__(self, max=100):
    self.max = max
    self.top = 0
    self.arr = [None for _ in range(max)]
  
  def is_empty(self):
    return self.top == 0

  def is_full(self):
    return self.top >= self.max - 1

  def push(self, x):
    if self.is_full():
      raise IndexError()
    self.top += 1
    self.arr[self.top] = x

  def pop(self):
    if self.is_empty():
      raise IndexError()
    self.top -= 1
    return self.arr[self.top + 1]

s = input().split()

stack = Stack(300)

for x in s:
  if x == "+":
    a = int(stack.pop())
    b = int(stack.pop())
    stack.push(b + a)
  elif x == "-":
    a = int(stack.pop())
    b = int(stack.pop())
    stack.push(b - a)
  elif x == "*":
    a = int(stack.pop())
    b = int(stack.pop())
    stack.push(b * a)
  else:
    stack.push(int(x))

print(stack.pop())
