import sys
readline = sys.stdin.readline

x, y, z, k = map(int, readline().split())
a = list(map(int, readline().split()))
b = list(map(int, readline().split()))
c = list(map(int, readline().split()))

a.sort(); a.reverse()
b.sort(); b.reverse()
c.sort(); c.reverse()

added = [[0,0,0]]
heap = [[a[0]+b[0]+c[0],0,0,0]]
n = 1

def print_heap(heap):
	m=0
	while m<len(heap):
		m2=m*2+1
		print(heap[m:min(m2,len(heap))])
		m=m2

def upheap(heap,n):
	i = n-1
	while i > 0:
		parent = (i-1)//2
		if heap[i][0] > heap[parent][0]:
			tmp = heap[parent]
			heap[parent] = heap[i]
			heap[i] = tmp
			i = parent
		else:
			break
	#print("up", n)
	#print_heap(heap)

def downheap(heap, n):
	if n <= 1:
		heap.pop()
		n -= 1
	else:
		heap[0] = heap.pop()
		n -= 1
		i = 0
		while True:
			child = 2 * i + 1
			if child > n-1:
				break
			if child < n-1 and heap[child][0] < heap[child+1][0]:
				child += 1
			if heap[i][0] < heap[child][0]:
				tmp = heap[child]
				heap[child] = heap[i]
				heap[i] = tmp
				i = child
			else:
				break
	#print("down", n)
	#print_heap(heap)
	return n

for _ in range(k):
	#print(n, heap)
	v, pa, pb, pc = map(int, heap[0])
	print(v)
	n = downheap(heap, n)
	if pa+1 < x and not [pa+1, pb, pc] in added:
		added.append([pa+1, pb, pc])
		n += 1
		heap.append([a[pa+1] + b[pb] + c[pc], pa+1, pb, pc])
		upheap(heap, n)
	if pb+1 < y and not [pa, pb+1, pc] in added:
		added.append([pa, pb+1, pc])
		n += 1
		heap.append([a[pa] + b[pb+1] + c[pc], pa, pb+1, pc])
		upheap(heap, n)
	if pc+1 < z and not [pa, pb, pc+1] in added:
		added.append([pa, pb, pc+1])
		n += 1
		heap.append([a[pa] + b[pb] + c[pc+1], pa, pb, pc+1])
		upheap(heap, n)
