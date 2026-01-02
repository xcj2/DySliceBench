import sys

input = sys.stdin.readline


class DoublyLinkedNode(object):
    def __init__(self, front, data, back):
        self.front = front
        self.data = data
        self.back = back


class DoublyLinkedList(object):
    def __init__(self):
        self.first_node = None
        self.last_node = None

    def insert(self, data):
        if self.first_node is None:
            self.first_node = DoublyLinkedNode(None, data, None)
            self.last_node = self.first_node
        else:
            second_node = self.first_node
            self.first_node = DoublyLinkedNode(None, data, second_node)
            second_node.front = self.first_node

    def delete(self, data):
        node = self.first_node
        while node:
            if node.data == data:
                if node == self.first_node:
                    self.delete_first()
                    break
                elif node == self.last_node:
                    self.delete_last()
                    break
                else:
                    node.front.back = node.back
                    node.back.front = node.front
                    break
            else:
                node = node.back

    def delete_first(self):
        if self.first_node.back is None:
            self.__init__()
        else:
            self.first_node = self.first_node.back
            self.first_node.front = None

    def delete_last(self):
        if self.last_node.front is None:
            self.__init__()
        else:
            self.last_node = self.last_node.front
            self.last_node.back = None

    def show_all(self):
        data_list = []
        node = self.first_node
        while node:
            data_list.append(node.data)
            node = node.back
        print(" ".join(map(str, data_list)))


def main():
    n = int(input())
    link = DoublyLinkedList()
    for _ in range(n):
        command = input().rstrip()
        if command == "deleteFirst":
            link.delete_first()
        elif command == "deleteLast":
            link.delete_last()
        else:
            command = command.split()
            command, data = command[0], int(command[1])
            if command == "insert":
                link.insert(data)
            elif command == "delete":
                link.delete(data)
            else:
                raise ValueError
    link.show_all()


if __name__ == "__main__":
    main()

