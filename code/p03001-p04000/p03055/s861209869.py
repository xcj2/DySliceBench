def getD(graph):
    # search edge
    origin=1
    d = 0
    queue = Queue()
    for it in graph[origin]:
        queue.enqueue((it, origin, d+1)) # next, coming from, depth

    while queue.size() > 0:
        leaf, origin, d = queue.dequeue()
        for it in graph[leaf]:
            if it != origin:
                queue.enqueue((it, leaf, d+1)) # next, coming from, depth
    # print(d, leaf)

    # search D
    origin=leaf
    d = 0
    queue = Queue()
    for it in graph[origin]:
        queue.enqueue((it, origin, d+1)) # next, coming from, depth

    while queue.size() > 0:
        leaf, origin, d = queue.dequeue()
        for it in graph[leaf]:
            if it != origin:
                queue.enqueue((it, leaf, d+1)) # next, coming from, depth
    # print(d, leaf)
    return d

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.last = None
        self._size = 0

    def enqueue(self, data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next
            
        self._size += 1

    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return = self.head.data
            self.head = self.head.next
            self._size -= 1
            
            if self._size == 0:
                self.head = None
                self.last = None
            return to_return
        
    def size(self):
        return self._size
    
def inside(y,x,H,W):
    if 0<=y<H and 0<=x<W:
        return True
    else:
        return False
    
def addQueueIfPossible(new_y, new_x, new_val, data, queue):
    if inside(new_y, new_x, H, W) and data[new_y][new_x]==-1:
        data[new_y][new_x] = new_val
        queue.enqueue((new_y, new_x, new_val))
        return True
    else:
        return False


n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

if n==1:
    print('First')
else:
    d = getD(graph)

    if (d+2)%3==0:
        print('Second')
    else:
        print('First')