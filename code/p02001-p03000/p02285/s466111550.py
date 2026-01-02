import sys
import os

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def insert_node(self, node):
        if node.value <= self.value:
            if self.left is None:
                self.left = node
            else:
                self.left.insert_node(node)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right.insert_node(node)

    def find_node_by_value(self, value):
        if self.value == value:
            return self
        elif value < self.value:
            if self.left is None:
                return None
            else:
                return self.left.find_node_by_value(value)
        elif value > self.value:
            if self.right is None:
                return None
            else:
                return self.right.find_node_by_value(value)
        else:
            assert(False)   

    def next_node_in_inorder(self):
        if self.right is not None:
            return self.right.smallest_offspring(self)
        else:
            return None

    def smallest_offspring(self, parent):
        if self.left is not None:
            return self.left.smallest_offspring(self)
        else:
            return (self, parent)

    def get_parent_of(self, value, parent_cand=None, is_left_child=None):
        if self.value == value:
            return parent_cand, is_left_child
        else:
            if value < self.value and self.left is not None:
                return self.left.get_parent_of(value, self, True)
            elif value > self.value and self.right is not None:
                return self.right.get_parent_of(value, self, False)
            else:
                assert(False)

    def delete_child(self, node):
        if self.left == node:
            self.left = None
        elif self.right == node:
            self.right = None
        else:
            assert(False)
            
    def delete_node(self, parent, value):
        # recursive
        if value < self.value and self.left is not None:
            self.left.delete_node(self, value)
        elif self.value < value and self.right is not None:
            self.right.delete_node(self, value)
        # delete
        elif self.left is None and self.right is None:
            # no children
            parent.delete_child(self)
        elif self.left is not None and self.right is not None:
            n, p = self.next_node_in_inorder()
            self.value = n.value
            n.delete_node(p, n.value)
        elif self.left is not None:
            self.value = self.left.value
            self.right = self.left.right
            self.left = self.left.left
        elif self.right is not None:
            self.value = self.right.value
            self.left = self.right.left
            self.right = self.right.right
    
#     def delete_node_by_value(self, value):
#         node = self.find_node_by_value(value)
#         parent, node_is_left_child = self.get_parent_of(value)
#         if node.left is None and node.right is None:
#             # hard delete
#             if parent is not None:
#                 if node_is_left_child:
#                     parent.left = None
#                 else:
#                     parent.right = None
#             else:
#                 return 'DELETE_BST'
#         else:
#         self.forcedelete(node, parent, node_is_left_child)

                
    def print_node_by_preorder(self):
        print('', self.value, end='')
        if self.left is not None:
            self.left.print_node_by_preorder()
        if self.right is not None:
            self.right.print_node_by_preorder()


    def print_node_by_inorder(self):
        if self.left is not None:
            self.left.print_node_by_inorder()
        print('', self.value, end='')
        if self.right is not None:
            self.right.print_node_by_inorder()

class BST:
    def __init__(self):
        self.root = None

    def cmd_insert(self, k):
        if self.root is None:
            self.root = Node(k)
        else:
            self.root.insert_node(Node(k))

    def cmd_find(self, k):
        if self.root is None:
            return False
        else:
            return (self.root.find_node_by_value(k) is not None)

    def cmd_delete(self, k):
        if self.root is None:
            pass
        else:
            self.root.delete_node(parent=self, value=k)

    def delete_child(self, node):
        assert(self.root == node)
        self.root = None

    def cmd_print(self):
        if self.root is not None:
            self.root.print_node_by_inorder()
            print()
            self.root.print_node_by_preorder()
            print()


if __name__ == '__main__':
    bst = BST()

    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip())
    num_cmds = int(lines[0])
    for line in lines[1:1+num_cmds]:
        line_split = line.split(' ')
        cmd = line_split[0]

        try:
            val = int(line_split[1])
        except:
            pass
        if cmd == 'insert':
            bst.cmd_insert(val)
        elif cmd == 'find':
            if bst.cmd_find(val):
                print('yes')
            else:
                print('no')
        elif cmd == 'print':
            bst.cmd_print()
        elif cmd == 'delete':
            bst.cmd_delete(val)
        else:
            assert(False)
        
        
        