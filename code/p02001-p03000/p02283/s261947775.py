
import sys



# ---------------------------------------------------
# ---------------------------------------------------
# ---------------------------------------------------



def resolve():
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    class BST:
        def __init__(self):
            self.node = None

        def insert(self, data):
            if self.node is None:
                self.node = Node(data)
            else:
                self._insert(data, self.node)

        def _insert(self,data, cur_node):
            if data < cur_node.data:
                if cur_node.left is None:
                    cur_node.left = Node(data)
                else:
                    self._insert(data, cur_node.left)
            elif data > cur_node.data:
                if cur_node.right is None:
                    cur_node.right = Node(data)
                else:
                    self._insert(data, cur_node.right)
            else:
                print("同じ値があります。")

        def pre_order_print(self):
            if self.node:
                self._pre_order_print(self.node)

        def _pre_order_print(self, cur_node):
            if cur_node:
                print(" ", end="")
                print(cur_node.data, end="")
                self._pre_order_print(cur_node.left)
                self._pre_order_print(cur_node.right)

        def in_order_print(self):
            if self.node:
                self._in_order_print(self.node)

        def _in_order_print(self, cur_node):
            if cur_node:
                self._in_order_print(cur_node.left)
                print(" ", end="")
                print(cur_node.data, end="")
                self._in_order_print(cur_node.right)

    N = int(input())
    bst = BST()
    lines = sys.stdin.readlines()
    for line in lines:
        s = line.split()
        if s[0] == "insert":
            x = int(s[1])
            bst.insert(x)
        else:
            # 出力規定： 先頭に1つの空白もいれる
            bst.in_order_print()
            print()
            bst.pre_order_print()
            print()


if __name__ == '__main__':
    resolve()
