from sys import stdin

class Sentinel():
    def __init__(self):
        self.value = None
        self.next = None
        self.prev = None

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

def Insert(key):
    node = Node(key)
    node.next = sent.next
    sent.next.prev = node
    sent.next = node
    node.prev = sent

def Search(key):
    p = sent.next
    while p.value != None:
        if p.value == key:
            return p
        else:
            p = p.next
    return False

def Delete(key):
    p = Search(key)
    if p != False:
        p.prev.next = p.next
        p.next.prev = p.prev

def DeleteF():
    p = sent.next
    p.prev.next = p.next
    p.next.prev = p.prev

def DeleteL():
    p = sent.prev
    p.prev.next = p.next
    p.next.prev = p.prev

sent = Sentinel()
sent.next = sent
sent.prev = sent

n = int(input())
for i in range(n):
    L = stdin.readline().split()
    if L[0] == 'insert':
        Insert(int(L[1]))
    elif L[0] == 'delete':
        Delete(int(L[1]))
    elif  L[0] == 'deleteFirst':
        DeleteF()
    elif  L[0] == 'deleteLast':
        DeleteL()

p = sent.next
tl = []
while True:
    tl.append(p.value)
    p = p.next
    if p.value == None:
        break
print(' '.join(str(x) for x in tl))
