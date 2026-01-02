head = 0
tail = 0
max_i = 200000
elapsed_time = 0

def initialize():
  global head, tail
  head = tail = 0

def isEmpty():
  global head, tail
  return head == tail

def isFull():
  global head, tail, max_i
  return head == (tail + 1) % max_i

def enqueue(x):
  if isFull():
    print('over flow')
  global head, tail
  Q[tail] = x
  if tail + 1 == max_i:
    tail = 0
  else:
    tail += 1

def dequeue():
  if isEmpty():
    print('under flow')
  global head, tail
  x = Q[head]
  if head + 1 == max_i:
    head = 0
  else:
    head += 1
  return x

initialize()

N, q = map(int, input().split())
max_i = N + 2
Q = [('', 0) for i in range(max_i)]
for i in range(N): # 値を受け取り、tailを一つずらす
  Q[i] = list(input().split())
  Q[i][1] = int(Q[i][1])
  tail += 1

while (head != tail): # headがtailに追いつくまで
  task = dequeue()
  count = min(q, task[1])
  task[1] -= count
  elapsed_time += count
  if task[1] > 0:
    enqueue(task)
  else:
    print(f"{task[0]} {elapsed_time}")
