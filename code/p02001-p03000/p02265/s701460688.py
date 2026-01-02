import sys
input = sys.stdin.readline


class Node:
    def __init__(self, val):
        self.val = val
        self.prev, self.next = None, None


class DoublyLinkedList:
    def __init__(self):
        self.n = 0
        self.dummy = Node(None)
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy

    def __getitem__(self, i):
        if i < 0 or i >= self.n:
            raise IndexError()
        return self._get_node(i).val 

    def __setitem__(self, i):
        if i < 0 or i >= self.n:
            raise IndexError()
        return self._get_node(i).val

    def __len__(self):
        return self.n

    def __bool__(self):
        return self.n != 0

    def __iter__(self):
        self.p = self.dummy
        return self

    def __next__(self):
        self.p = self.p.next
        if self.p == self.dummy:
            raise StopIteration
        return self.p.val

    def append(self, val):
        ptr = self.dummy.prev
        new_ptr = Node(val)
        new_ptr.prev = ptr.prev
        new_ptr.next = ptr
        new_ptr.next.prev = new_ptr
        new_ptr.prev.next = new_ptr
        self.n += 1

    def appendleft(self, val):
        ptr = self.dummy.next
        new_ptr = Node(val)
        new_ptr.prev = ptr.prev
        new_ptr.next = ptr
        new_ptr.next.prev = new_ptr
        new_ptr.prev.next = new_ptr
        self.n += 1

    def pop(self):
        ptr = self.dummy.prev
        ptr.prev.next = ptr.next
        ptr.next.prev = ptr.prev
        self.n -= 1

    def popleft(self):
        ptr = self.dummy.next
        ptr.prev.next = ptr.next
        ptr.next.prev = ptr.prev
        self.n -= 1

    def _get_node(self, i):
        if i < self.n // 2:
            ptr = self.dummy.next
            for _ in range(i):
                ptr = ptr.next
        else:
            ptr = self.dummy
            for _ in range(i, self.n):
                ptr = ptr.prev
        return ptr

    def _remove(self, i):
        if i < 0 or i >= self.n:
            raise IndexError()
        ptr = self._get_node(i)
        ptr.prev.next = ptr.next
        ptr.next.prev = ptr.prev
        self.n -= 1
        return ptr.val

    def _add(self, i, val):
        if i < 0 or i > self.n:
            raise IndexError()
        ptr = self._get_node(i)
        new_ptr = Node(val)
        new_ptr.prev = ptr.prev
        new_ptr.next = ptr
        new_ptr.next.prev = new_ptr
        new_ptr.prev.next = new_ptr
        self.n += 1

    def delete(self, val):
        ptr = self.dummy
        for _ in range(self.n):
            ptr = ptr.next
            if ptr.val == val:
                ptr.prev.next = ptr.next
                ptr.next.prev = ptr.prev
                self.n -= 1
                return True
        return False


dls = DoublyLinkedList()
input()
for query in sys.stdin:
    if query[0] == "i":
        val = query[7:-1]
        dls.appendleft(val)
    elif query[6] == "F":
        dls.popleft()
    elif query[6] == "L":
        dls.pop()
    else:
        val = query[7:-1]
        dls.delete(val)

print(*list(dls))
