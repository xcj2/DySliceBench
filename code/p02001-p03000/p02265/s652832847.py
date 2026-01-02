# doubly Linked listの設計
from sys import stdin


class DoublyLinkedList():

    class Cell():
        def __init__(self, value):
            self.value = value
            self.next = None
            self.previous = None

    def __init__(self):
        self.head = DoublyLinkedList.Cell(None)
        self.tail = DoublyLinkedList.Cell(None)
        self.head.next = self.tail
        self.tail.previous = self.head

    def insert(self, v):
        new_cell = DoublyLinkedList.Cell(v)
        new_cell.next = self.head.next
        new_cell.previous = self.head
        self.head.next.previous = new_cell
        self.head.next = new_cell

    def delete(self, v):
        tmp_cell = self.head.next
        while tmp_cell.value is not None:
            if tmp_cell.value == v:
                tmp_cell_next = tmp_cell.next
                tmp_cell_previous = tmp_cell.previous
                tmp_cell_previous.next = tmp_cell_next
                tmp_cell_next.previous = tmp_cell_previous
                break
            tmp_cell = tmp_cell.next

    def deleteFirst(self):
        self.head.next = self.head.next.next
        self.head.next.previous = self.head

    def deleteLast(self):
        self.tail.previous = self.tail.previous.previous
        self.tail.previous.next = self.tail


def print_res(dl):
    res = []
    cur = dl.head.next
    while cur.next is not None:
        res.append(cur.value)
        cur = cur.next
    print(" ".join(res))


def main():
    dl = DoublyLinkedList()
    line_num = int(stdin.readline())
    for i in range(line_num):
        command = stdin.readline().strip()
        if command == "deleteFirst":
            dl.deleteFirst()
        elif command == "deleteLast":
            dl.deleteLast()
        elif command.startswith("insert"):
            dl.insert(command.split(" ")[1].strip())
        else:
            dl.delete(command.split(" ")[1].strip())
    print_res(dl)


if __name__ == '__main__':
    main()

