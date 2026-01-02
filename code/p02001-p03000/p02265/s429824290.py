class Node:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.nil = Node(None)
        self.nil.prev = self.nil
        self.nil.next = self.nil

    def insert(self,key):
        new = Node(key)
        new.next = self.nil.next
        self.nil.next.prev = new
        self.nil.next = new
        new.prev = self.nil

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
    input = sys.stdin.readline  # 入力の高速化

    n = int(input())

    dll = DoublyLinkedList()

    for _ in range(n):
        '''
        以下のようにcomとkeyに分けるとTimeLimitExceededになるので、comだけで処理しました
        (別のいい方法があれば教えて欲しいです)
        com, *key = input().split()
        この場合keyがリストになるので、com[7:]をkey[0]で置き換える必要があります。
        (xがない命令ではkey=[]となるだけ)
        '''
        com = input().rstrip()
        # 以下、本と順番など多少異なります
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
