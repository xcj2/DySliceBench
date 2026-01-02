def init():
  global top
  top = 0

def isEmpty():
  global top
  return top == 0

def isFull():
  global top, MAX
  return top >= MAX

def push(x):
  global top, s
  if isFull():
    return False
  s[top] = x
  top += 1


def pop():
  global top, s
  if isEmpty():
    return False
  top -= 1
  return s[top]


def calc(i_1, i_2, op):
  if op == '+':
    return i_1 + i_2
  elif op == '-':
    return i_1 - i_2
  else:
    return i_1 * i_2

data = list(map(str, input().split()))
top = 0
MAX = 100
s = [0 for i in range(MAX)]
for i in data:
  if i == '+' or i == '*' or i == '-':
    a = pop()
    b = pop()
    push(calc(int(b), int(a), i))
  else:
    push(i)
print(s[0])

