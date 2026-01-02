import sys
input = sys.stdin.readline

class Node:
  def __init__(self,key):
    self.key=key
    self.prev=None
    self.next=None

class LinkedList:
  first=None
  last=None
  current=first

  def insert(self,x):
    node=Node(x)
    self.current=node
    if self.first==None:
      self.first=node
      self.last=node
    else:
      self.first.prev=node
      node.next=self.first
      self.first=node
  
  def delete(self,x):
    if self.first==None:
      #print('Error')
      return
    if self.first==self.last and self.first.key==x:
      self.first=None
      self.current=None
      self.last=None
      return

    elif self.first.key==x:
      self.first.next.prev=None
      self.current=self.first.next
      self.first=self.first.next
      return

    tmp=self.first
    while tmp!=None:
      if self.last==tmp and tmp.key==x:
        self.last.prev.next=None
        self.last=self.last.prev
        break
      elif tmp.key==x:
        tmp.prev.next=tmp.next
        tmp.next.prev=tmp.prev
        break
      tmp=tmp.next

  def deleteFirst(self):
    if self.first==self.last:
      self.first=None
      self.last=None
      self.current=None
      return
    self.first.next.prev=None
    self.first=self.first.next
    self.current=self.first

  def deleteLast(self):
    if self.first==self.last:
      self.first=None
      self.last=None
      self.current=None
      return
    self.last.prev.next=None
    self.last=self.last.prev

  def next(self):
    if self.current==None:
      return None
    tmp=self.current
    self.current=self.current.next
    return tmp

if __name__ == '__main__':
  n=int(input())
  L=LinkedList()

  def answer():
    tmp=L.next()
    while tmp!=None:
      ans=tmp.key
      tmp=L.next()
      if tmp==None:
        print(ans)
      else:
        print(ans,end=' ')
    L.current=L.first

  for _ in range(n):
    S=input().split()
    #print('---')
    #print(*S)
    if S[0]=='insert':
      L.insert(S[1])
    elif S[0]=='delete':
      L.delete(S[1])
    elif S[0]=='deleteFirst':
      L.deleteFirst()
    elif S[0]=='deleteLast':
      L.deleteLast()
    #answer()
  answer()

