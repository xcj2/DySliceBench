# reffer to http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=2968766#1
class Node(object):
  def __init__(self, num, prv = None, nxt = None):
    self.num = num
    self.prv = None
    self.nxt = None

class DoublyLinkedList(object):
  def __init__(self):
    self.start = self.last = None

  def insert(self, num):
    new_elem = Node(num)

    if self.start is None:
      # 最初と最後にnew_elemをセット
      self.start = self.last = new_elem
    else:
      # 前に追加していくのでnew_elemの次にself.startをセット
      new_elem.nxt = self.start
      self.start.prv = new_elem
      self.start = new_elem

  def delete_num(self, target):
    it = self.start
    while it is not None:
      if it.num == target:
        # nodeが1つしか無いかのチェック
        if it.prv is None and it.nxt is None:
          self.start = self.last = new_elem
        else:
          # 先頭かどうかのチェック
          if it.prv is not None:
            it.prv.nxt = it.nxt
          else:
            self.start = self.start.nxt

          # 最後かどうかのチェック
          if it.nxt is not None:
            it.nxt.prv = it.prv
          else:
            self.last = self.last.prv

        break

      # 対象nodeを次に回す
      it = it.nxt

  def delete_start(self):
    if self.start is self.last:
      self.start = self.last = None
    else:
      self.start.nxt.prv = None
      self.start = self.start.nxt

  def delete_last(self):
    if self.start is self.last:
      self.start = self.last = None
    else:
      self.last.prv.nxt = None
      self.last = self.last.prv

  def get_content(self):
    ret = []
    it = self.start

    while it is not None:
      ret.append(it.num)
      it = it.nxt

    return ' '.join(ret)

def _main():
  from sys import stdin

  n = int(input())

  lst = DoublyLinkedList()

  for _ in range(n):
    cmd = stdin.readline().strip().split()
    if cmd[0] == 'insert':
      lst.insert(cmd[1])
    elif cmd[0] == 'delete':
      lst.delete_num(cmd[1])
    elif cmd[0] == 'deleteFirst':
      lst.delete_start()
    elif cmd[0] == 'deleteLast':
      lst.delete_last()


  print(lst.get_content())

if __name__ == '__main__':
  _main()
