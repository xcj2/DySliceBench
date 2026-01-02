class Node:
    def __init__(self, val, next_node = None):
        self.value = val
        self.next = next_node
        
class que:
    def __init__(self):
        self.start = None
        self.last = None
    def append(self, num):
        new_node = Node(num)
        if self.start == None:
            self.start = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
    def popleft(self):
        return_node = self.start
        self.start = return_node.next
        return return_node.value
    def isempty(self):
        return self.start == None
    def print_vals(self):
        node = self.start
        output =""
        while node != None:
            output += str(node.value)
            node = node.next
        print(output)
        
       
n, p = map(lambda x:int(x), input().split(' '))
processes = que()
for i in range(n):
    name, time = input().split(' ')
    time = int(time)
    processes.append((name, time))
all_time = 0
while not processes.isempty():
    name, time = processes.popleft()
    if time <= p:
        all_time += time
        print(f'{name} {all_time}')
    else:
        all_time += p
        processes.append((name, time - p))
