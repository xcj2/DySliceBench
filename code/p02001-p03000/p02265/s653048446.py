class Node:
    def __init__(self, key, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, key):
        node = Node(key)

        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def deleteKey(self, key):
        node = self.head

        while node:
            if node.key == key:
                if node.prev is None and node.next is None:
                    self.head = self.tail = None
                else:
                    # prevの処理
                    if node.prev is not None:  # 先頭でないなら
                        node.prev.next = node.next
                    else:  # 先頭なら
                        self.head = self.head.next

                    # nextの処理
                    if node.next is not None:  # 最後でないなら
                        node.next.prev = node.prev
                    else:  # 最後なら
                        self.tail = self.tail.prev
                break
            node = node.next

    def deleteFirst(self):
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next

    def deleteLast(self):
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev

    def createAnswerList(self):
        ret = []
        node = self.head

        while node:
            ret.append(node.key)
            node = node.next

        return " ".join(ret)


if __name__ == "__main__":
    from sys import stdin

    count = int(input())

    linked_list = DoublyLinkedList()

    for i in range(count):
        order = stdin.readline().strip().split()
        if order[0] == "insert":
            linked_list.insert(order[1])
        elif order[0] == "delete":
            linked_list.deleteKey(order[1])
        elif order[0] == "deleteFirst":
            linked_list.deleteFirst()
        elif order[0] == "deleteLast":
            linked_list.deleteLast()

    print(linked_list.createAnswerList())

