

def parent(i):
    if heap[i // 2] != None:
        print(", parent key = " + str(heap[i // 2]), end = "")
    else:
        print("", end = "")

def left(i):
    if 2 * i <= n:
        print(", left key = " + str(heap[2 * i]), end = "")
    else:
        print("", end = "")

def right(i):
    if 2 * i + 1 <= n:
        print(", right key = " + str(heap[2 * i + 1]), end = "")
    else:
        print("", end = "")


n=int(input())
heap = list(map(int,input().split()))
heap.insert(0, None)

for i in range(1, n + 1):
    print("node", str(i) + ": key = " + str(heap[i]), end = "")
    parent(i)
    left(i)
    right(i)
    print(", ")
   # print("node %d: parent = %d, depth = %d, "%(i,nodes[i].parent_id,nodes[i].depth),end = "")
    
    
    
