N = int(2e5+3)
heap_arr, heap_size = [0] * N, 0

def heap_push(x):
    global heap_size
    heap_arr[heap_size] = x
    i = heap_size
    while i > 0 and heap_arr[i] > heap_arr[(i-1)//2]:
        heap_arr[i], heap_arr[(i-1)//2] = heap_arr[(i-1)//2], heap_arr[i]
        i = (i-1)//2
    heap_size += 1

def get_max():
    global heap_size
    if heap_size == 0:
        return -2e9
    return heap_arr[0]

def heap_pop():
    global heap_size
    if heap_size == 0:
        return
    heap_size -= 1
    heap_arr[0], heap_arr[heap_size] = heap_arr[heap_size], heap_arr[0]
    i, j = 0, -1
    while i != j:
      j = i
      l = 2*i+1
      r = 2*i+2
      if l < heap_size and heap_arr[l] > heap_arr[i]:
          i = l
      if r < heap_size and heap_arr[r] > heap_arr[i]:
          i = r
      heap_arr[i], heap_arr[j] = heap_arr[j], heap_arr[i]

n, m = map(int, input().split())
arr = list(map(int, input().split()))
for i in arr:
    heap_push(i)
while m >= 1:
    x = get_max() // 2
    heap_pop()
    heap_push(x)
    m -= 1    
print(sum(heap_arr))