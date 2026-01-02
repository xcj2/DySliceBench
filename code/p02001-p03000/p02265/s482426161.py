import sys

class Node:
    """
    key: Value of the node
    next: Pointer to the next node
    prev: Pointer to the previous node
    """

    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        """
        next always point to the very first node in a list
        prev always point to the last node in a list
        """
        self.next = None
        self.prev = None

    def insert(self, key):
        """
        :param key: key to insert into a list (inserted to the first place in the list)
        :return: None
        """
        newNode = Node(key)
        # First node ever added to the list
        if self.next is None:
            newNode.next = None
            newNode.prev = self
            self.next = newNode
            self.prev = newNode
        # Second nodes and forth
        else:
            newNode.next = self.next
            newNode.prev = self
            self.next.prev = newNode
            self.next = newNode

    def listSearch(self, key):
        """
        :param key: key of a note to search for
        :return: Node (the first Node from the beginning of a list)
        """
        cur = self.next
        while cur is not None and cur.key != key:
            cur = cur.next
        return cur

    def deleteNode(self, node):
        """
        :param node: Node to delete
        :return: None
        """
        if node is None:
            return
        # If the node is the last node
        elif node.next is None:
            node.prev.next = None
            self.prev = node.prev
        # If the node is not the last node
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    def delete(self, key):
        """
        Delete the first node that has the key.
        :param key: key that the node to be deleted has
        :return: None
        """
        self.deleteNode(self.listSearch(key))

    def deleteFirst(self):
        """
        Delete the first node in a list
        :return: None
        """
        cur = self.next
        self.deleteNode(cur)

    def deleteLast(self):
        """
        Delete the last node in a list
        :return: None
        """
        cur = self.prev
        self.deleteNode(cur)

    def showKeys(self):
        """
        Print keys of nodes in a list divided by a space
        :return: None
        """
        cur = self.next
        keys = []
        while cur is not None:
            keys.append(cur.key)
            cur = cur.next
        keys = map(str, keys)
        print(' '.join(keys))

n = int(input())
d = DoublyLinkedList()

# input() seems to be too slow for this (result in TLE for large inputs)
for i in sys.stdin:
    if 'insert' in i:
        x = i[7:-1]
        d.insert(x)
    elif 'deleteFirst' in i:
        d.deleteFirst()
    elif 'deleteLast' in i:
        d.deleteLast()
    elif 'delete' in i:
        x = i[7:-1]
        d.delete(x)
    else:
        pass

d.showKeys()
