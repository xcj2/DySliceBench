class Node(object):
  def __init__(self, num, prv = None, next = None):
    self.num = num
    self.prv = prv
    self.next = next

class DoublyLinkedList(object):
  def __init__(self):
    self.start = self.last = None

  def insert(self, num):
    new_element = Node(num)

    if self.start is None: # 空の場合
      self.start = self.last = new_element
    else:
      new_element.next = self.start
      self.start.prv = new_element
      self.start = new_element

  def delete(self, target):
    it = self.start
    while it is not None: # 該当する最初のノードを見つける
      if it.num == target:
        if it.prv is None and it.next is None: # ノードが一つだけの時
          self.start = self.last = None
        else:
          if it.prv is not None: # 先頭ではない
            it.prv.next = it.next
          else: # 先頭の場合、先頭の次をstartにする
            self.start = self.start.next
          if it.next is not None:  # 最後ではない場合
            it.next.prv = it.prv
          else: # 最後の場合、最後の一つ前をlastにする
            self.last = self.last.prv
        break
      it = it.next

  def deleteFirst(self):
    if self.start is self.last:
      self.start = self.last = None
    else:
      self.start.next.prv = None
      self.start = self.start.next

  def deleteLast(self):
    if self.start is self.last:
      self.start = self.last = None
    else:
      self.last.prv.next = None
      self.last = self.last.prv

  def contentToArray(self):
    n_list = []
    it  = self.start
    while it is not None:
      n_list.append(it.num)
      it = it.next
    return ' '.join(n_list)

def main():
  from sys import stdin
  N = int(input())

  linkedList = DoublyLinkedList() # インスタンス作成

  for i in range(N):
    command = stdin.readline().rstrip().split()
    if command[0] == 'insert':
      linkedList.insert(command[1])
    elif command[0] == 'delete':
      linkedList.delete(command[1])
    elif command[0] == 'deleteFirst':
      linkedList.deleteFirst()
    elif command[0] == 'deleteLast':
      linkedList.deleteLast()

  print(linkedList.contentToArray())

if __name__ == "__main__":
  main()
