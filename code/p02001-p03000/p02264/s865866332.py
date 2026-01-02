class Node:
    __slots__ = ["data", "next", "prev"]
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    __slots__ = ["head", "tail"]
    def __init__(self):
        self.head = None
        self.tail = None
    
    def appendleft(self, data):
        node = Node(data)
        self.head, node.next = node, self.head
        if self.tail:
            node.next.prev = self.head
        else:
            self.tail = node
    
    def pop(self):
        if self.tail:
            target, self.tail = self.tail, self.tail.prev
            if self.tail:
                self.tail.next = None
            return target.data

def simulate_round_robin_scheduling(x, y):
    total_time = 0
    while y.tail:
        name, time = y.pop()
        time = int(time)
        total_time += min(time, x)
        time -= x
        if time > 0:
            y.appendleft([name, time])
        else:
            print("{} {}".format(name, total_time))
if __name__ == "__main__":
    n, q = map(int, input().split())
    processes = Queue()
    for _ in range(n):
        processes.appendleft(input().split())
    simulate_round_robin_scheduling(q, processes)
