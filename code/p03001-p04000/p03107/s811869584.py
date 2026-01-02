class Node:
    def __init__(self, num: str):
        self.num = num
        self.before = None
        self.next = None
    
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.before = self.tail
            self.tail.next = node
            self.tail = node

    def check(self):
        node = self.tail
        ans = 0
        while not node is self.head:
            before_node = node.before
            if node.num != before_node.num:
                ans += 2
                if before_node is self.head:
                    break
                elif node is self.tail:
                    before_node.before.next = None
                    self.tail = before_node.before
                    node = before_node.before
                else:
                    before_node.before.next = node.next
                    node.next.before = before_node.before
                    node = node.next
            else:
                node = node.before
        print(ans)

S = list(input())
cube = Linked_List()

for c in S:
    node = Node(c)
    cube.append(node)

cube.check()
