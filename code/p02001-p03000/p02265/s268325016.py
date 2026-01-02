class Node:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.nil = Node(None) # 番兵
        self.nil.prev = self.nil
        self.nil.next = self.nil # prevもnextも番兵に接続

    def insert(self, key):
        new = Node(key)
        new.next = self.nil.next   # 新しいNodeの後ろをもともと番兵の後ろにあったNodeに変更
        self.nil.next.prev = new   # もともと番兵の次にあったNodeの前を新しいNodeに変更
        self.nil.next = new        # 番兵の後ろを新しいNodeに変更
        new.prev = self.nil             # 新しいNodeの前をnilに指定

    def listSearch(self, key):
        cur = self.nil.next
        while cur != self.nil and cur.key != key:
            cur = cur.next
        return cur

    def deleteNode(self, t):
        if t == self.nil:
            return
        t.prev.next = t.next
        t.next.prev = t.prev

    def deleteFirst(self):
        self.deleteNode(self.nil.next)

    def deleteLast(self):
        self.deleteNode(self.nil.prev)

    def deleteKey(self, key):
        self.deleteNode(self.listSearch(key))


if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n = int(input())

    dll = DoublyLinkedList()

    for _ in range(n):
        com = input().rstrip()
        # keyはinsert,deleteなら[x]になり、
        # deleteFirst,deleteLastなら[]になる。
        if com[0] == 'i':
            dll.insert(com[7:])
        elif com[6] == 'F':
            dll.deleteFirst()
        elif com[6] == 'L':
            dll.deleteLast()
        else:
            dll.deleteKey(com[7:])

    cur = dll.nil.next
    ans = []
    while cur != dll.nil:
        ans.append(cur.key)
        cur = cur.next

    print(' '.join(ans))

