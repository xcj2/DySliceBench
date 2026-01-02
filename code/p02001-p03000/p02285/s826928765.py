class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None

    def _get_most_left_node(self):
        x = self
        while x.left is not None:
            x = x.left
        return x
    
class Tree():
    def __init__(self, root=None):
        self.root = root
    
    def insert(self, node):
        y = None
        x = self.root
        while x is not None:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        
        node.parent = y
        if y is None:   # Tree が空だった場合
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node
    
    def print_inorder_tree_walk(self):
        def work(node):
            if node is None:
                return
            work(node.left)
            print('', node.key, end='')
            work(node.right)

        work(self.root)
        print()
    
    def print_preorder_tree_walk(self):
        def work(node):
            if node is None:
                return
            print('', node.key, end='')
            work(node.left)
            work(node.right)

        work(self.root)
        print()

    def find(self, key):
        """Tree 中に key をもつノードがあればそのノードを返す。なければ None を返す。"""
        x = self.root
        while x is not None:
            if key == x.key:
                return x
            elif key < x.key:
                x = x.left
            else:
                x = x.right
        return None

    def delete(self, key):
        """削除できたら True、存在せず削除できない場合は False を返す。"""
        x = self.find(key)
        if not x:
            return False
        y = x if x.left is None or x.right is None else x.right._get_most_left_node()
        z = y.left if y.left is not None else y.right
        if z is not None: z.parent = y.parent
        if y.parent is None:
            self.root = z
        elif y is y.parent.left:
            y.parent.left = z
        else:
            y.parent.right = z
        
        if x is not y:
            x.key = y.key
        
        return True

if __name__ == '__main__':
    import sys

    n = int(input())
    T = Tree()
    for _ in range(n):
        command, *args = sys.stdin.readline().split()
        if command[0] == 'i':   # insert key
            T.insert(Node(int(args[0])))
        elif command[0] == 'f': # find key
            if T.find(int(args[0])):
                print('yes')
            else:
                print('no')
        elif command[0] == 'd': # delete key
            T.delete(int(args[0]))
        else:   # print
            T.print_inorder_tree_walk()
            T.print_preorder_tree_walk()
