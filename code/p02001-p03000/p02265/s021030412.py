import sys
n = int(sys.stdin.readline())
lines = sys.stdin.readlines()
#n = int(input())
#import collections
#dll = collections.deque()
class Node:
  def __init__(self,v):
    self.val = v
    self.prev = None
    self.next = None
class DLL():
  def __init__(self):
    self.tail = Node(None)
    self.tail.next = self.tail
    self.tail.prev = self.tail
  def insert(self,x):
    n = Node(x)
    pre = self.tail.next
    n.next = pre
    n.prev = self.tail
    pre.prev = n
    self.tail.next = n
  def delete(self,x):
    node = self.tail.next
    while node != self.tail:
      if node.val == x:
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        return
      node = node.next
  def deleteFirst(self):
    pre = self.tail.next
    if pre == self.tail:
      return
    node = self.tail.next
    p = node.prev
    n = node.next
    p.next = n
    n.prev = p
  def deleteLast(self):
    if self.tail.next == self.tail:
      return
    node = self.tail.prev
    p = node.prev
    n = node.next
    p.next = n
    n.prev = p
  def inspect(self):
    node = self.tail.next
    ret = []
    while node != self.tail:
      ret.append(str(node.val))
      node = node.next
    print(" ".join(ret))
dll=DLL()
for i in range(n):
  q = lines[i]
  if q[0] == "i":
      dll.insert(int(q.split()[1]))
  elif q[6] == " ":
      dll.delete(int(q.split()[1]))
  elif q[6] == "L":
      dll.deleteLast()
  elif q[6] == "F":
      dll.deleteFirst()
dll.inspect()
#print(" ".join(map(str,dll)))
