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

H, W = map(int,input().split())

data = []
for _ in range(H):
    data.append([0 if it=='#' else -1 for it in input()])



queue = Queue()
for y in range(H):
    for x in range(W):
        if data[y][x] == 0:
            queue.enqueue((y,x,0))

while queue.size() > 0:
    y, x, val = queue.dequeue()
    # up
    addQueueIfPossible(y-1, x, val+1, data, queue)
    # down
    addQueueIfPossible(y+1, x, val+1, data, queue)
    # right
    addQueueIfPossible(y, x+1, val+1, data, queue)
    # down
    addQueueIfPossible(y, x-1, val+1, data, queue)

print(val)