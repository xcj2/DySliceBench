class Node:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev


class Que:
    def __init__(self):
        self.head = None
        self.last = None

    def add(self, value):
        new_node = Node(value, None, self.last)
        if not self.head:
            self.head = new_node
        else:
            self.last.next = new_node
        self.last = new_node

    def popleft(self):
        if not self.head:
            return -1
        v = self.head.value

        self.head = self.head.next
        return v

    def isempty(self):
        return not self.head


n, q = map(int, input().split())
a = []
for i in range(n):
    p, t = input().split()
    a.append([p, int(t)])

que = Que()

for e in a:
    que.add(e)

sum_t = 0
while not que.isempty():
    p, t = que.popleft()
    if t > q:
        que.add([p, t - q])
        sum_t += q
    else:
        sum_t += t
        print(p, sum_t)






