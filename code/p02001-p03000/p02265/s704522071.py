# ALDS1_3_C
import sys
class Cell():
    def __init__(self, x):
        self.key = x
        self.prev = None
        self.next = None


class DoubleLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, x):
        new = Cell(x)
        tmp = self.head

        if tmp is None:
            new.next = None
            self.tail = new

        else:
            new.next = tmp
            tmp.prev = new

        self.head = new
        new.prev = None
        return

    def delete(self, x):

        if (self.head is None) & (self.tail is None):
            return

        tmp = self.head

        while tmp.key != x:
            tmp = tmp.next
            if tmp is None:  # 一番後ろまで要素　xが存在しなかったら
                return

        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif tmp is self.head:
            tmp.next.prev = None
            self.head = tmp.next
        elif tmp is self.tail:
            tmp.prev.next = None
            self.tail = tmp.prev
        else:
            tmp.prev.next = tmp.next
            tmp.next.prev = tmp.prev
        return

    def deleteFirst(self):
        if self.head:
            self.head = self.head.next

        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return

    def deleteLast(self):
        if self.tail:
            self.tail = self.tail.prev

        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return

    def show(self):
        tmp = self.head

        while tmp:
            print(tmp.key, end='')
            if tmp.next:
                print(' ', end='')
            tmp = tmp.next
        else:
            print('')
        return

    def shown(self):
        tmp = self.head
        keys = []
        while tmp:
            keys.append(tmp.key)
            tmp = tmp.next
        keys = ' '.join(keys)
        print(keys)
        return

def main():
    l = DoubleLinkedList()

    N = int(sys.stdin.readline())

    for i in range(N):
        comand = sys.stdin.readline().strip()

        if comand == 'deleteFirst':
            l.deleteFirst()
        elif comand == 'deleteLast':
            l.deleteLast()
        else:
            comand, number = comand.split()
            if comand == 'insert':
                l.insert(number)
            else:
                l.delete(number)

    l.show()


if __name__ == '__main__':
    main()
