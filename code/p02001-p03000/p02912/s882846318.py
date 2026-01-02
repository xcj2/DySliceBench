def left(i):
  return 2 * i + 1

def right(i):
  return 2 * i + 2

def parent(i):
  return (i - 1) // 2

def swap(items, i, j):
  items[i], items[j] = items[j], items[i]
  
def bubble_up(items, i):
  p = parent(i)
  while i > 0 and items[i] > items[p]:
    swap(items, i, p)
    i = p
    p = parent(i)
    
def heappush(items, item):
  items.append(item)
  bubble_up(items, len(items) - 1)
  
def tricle_down(items, i):
  while True:
    j = -1
    r = right(i)
    if r < len(items) and items[r] > items[i]:
      l = left(i)
      if items[l] > items[r]:
        j = l
      else:
        j = r
    else:
      l = left(i)
      if l < len(items) and items[l] > items[i]:
        j = l
    if j >= 0:
      swap(items, i, j)
    i = j
    if i < 0:
      break
  
def heappop(items):    
  x = items[0]
  items[0] = items[-1]
  items.pop()
  tricle_down(items, 0)
  return x

N, M = map(int, input().split())

items = []
for x in input().split():
  heappush(items, int(x))

for _ in range(M):
  a = heappop(items)
  heappush(items, a // 2)
  
print(sum(items))  


