import sys
class Node:
    def __init__(self,a:int):
        self.val = a
        self.parent = None
        self.right = None
        self.left = None

class Heap:
    def __init__(self):
        self.size = None
        self.node = None

    def push(self, a:int):
        c = Node(a)
        if self.size is None:
            self.size = 1
            self.node = c
        else:
            self.size += 1
            n = self.size
            l = []
            b = self.node
            c = Node(a)
            while n != 1:
                l.append(n % 2)
                n //= 2
            for i in range(len(l) - 1):
                if l[len(l) - 1 - i] == 1:
                    b = b.right
                else:
                    b = b.left
            if l[0] == 1:
                b.right = c
                c.parent = b
            else:
                b.left = c
                c.parent = b
            while c.parent is not None and c.parent.val < c.val:
                d = c.val
                c.val = c.parent.val
                c.parent.val = d
                c = c.parent

    def pop(self):
        aval = self.node.val
        a = self.node
        n = self.size
        l = []
        b = self.node
        while n != 1:
            l.append(n % 2)
            n //= 2
        for i in range(len(l)):
            if l[len(l) - 1 - i] == 1:
                b = b.right
                if len(l) - 1 - i == 0:
                    b.parent.right = None
            else:
                b = b.left
                if len(l) - 1 - i == 0:
                    b.parent.left = None
        self.size -= 1
        a.val = b.val

        while (a.right is not None and a.val < a.right.val) or (a.left is not None and a.val < a.left.val):
            if a.right is None and a.left is not None:
                c = a.val
                a.val = a.left.val
                a.left.val = c
                a = a.left
            elif a.left.val > a.right.val:
                c = a.val
                a.val = a.left.val
                a.left.val = c
                a = a.left
            else:
                c = a.val
                a.val = a.right.val
                a.right.val = c
                a = a.right
        return aval
def main(): 
    x, y, A, B, C = map(int, input().split())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    r = list(map(int, input().split()))
    pq = Heap()
    p.sort()
    q.sort()
    for i in range(x):
        pq.push(p[len(p) - 1 - i])
    for i in range(y):
        pq.push(q[len(q) - 1 - i])
    for i in range(len(r)):
        pq.push(r[i])
    ans = 0
    for i in range(x + y):
        ans += pq.pop()
    print(ans)

main()
