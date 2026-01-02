S = [0 for _ in range(1000)]
A = list(input().split())
top = 0

def initialize():
  global top
  top = 0

def isEmpty():
  global top
  return top == 0

def isFull():
  global top
  return top > 1000

def push(x):
  if isFull():
    print('over flow')
  global top
  top += 1
  S[top] = x

def pop():
  if isEmpty():
    print('under flow')
  global top
  top -= 1
  return S[top+1]

for i in range(len(A)):
  if A[i] == '*':
    b = pop()
    a = pop()
    result = a * b
    push(result)
  elif A[i] == '+':
    b = pop()
    a = pop()
    result = a + b
    push(result)
  elif A[i] == '-':
    b = pop()
    a = pop()
    result = a - b
    push(result)
  else:
    push(int(A[i]))

print(S[1])

