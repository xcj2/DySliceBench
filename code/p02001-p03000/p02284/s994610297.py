#! /usr/bin/env python


class NodeBintree:

    def __init__(self, key, parent=None):
        self.key = key
        self.left = None
        self.right = None

    def insert_node (self, n):
        if (self.key is None) or (self.key > n.key):
            if self.left is None:
                self.left = n
            else:
                self.left.insert_node(n)
        else:
            if self.right is None:
                self.right = n
            else:
                self.right.insert_node(n)
    def find (self, key):
        if self.key is None:
            return self.left.find(key)
        elif self.key == key:
            return "yes"
        elif self.key > key:
            if self.left is None:
                return "no"
            else:
                return self.left.find(key)
        else:
            if self.right is None:
                return "no"
            else:
                return self.right.find(key)

    def traverse_inorder (self):
        ret = ""

        if self.left is not None:
            ret += self.left.traverse_inorder()

        if self.key is not None:
            ret += " {0}".format(self.key)

        if self.right is not None:
            ret += self.right.traverse_inorder()

        return ret

    def traverse_preorder (self):
        ret = ""

        if self.key is not None:
            ret += " {0}".format(self.key)

        if self.left is not None:
            ret += self.left.traverse_preorder()

        if self.right is not None:
            ret += self.right.traverse_preorder()

        return ret

def proc_inputs ():
    num_inputs = int(input())
    inputs = [proc_command(input().split()) for i in range(num_inputs)]
    return inputs

def proc_command (l):
    if len(l) > 1:
        arg = l[1]
    else:
        arg = None
    return {"command": l[0], "arg": arg}

def execute_command (tree, command):
    if command["command"] == "insert":
        tree.insert_node(NodeBintree(int(command["arg"])))

    elif command["command"] == "find":
        print(tree.find(int(command["arg"])))

    elif command["command"] == "print":
        print(tree.traverse_inorder() )
        print(tree.traverse_preorder() )

    return


def main ():
    inputs = proc_inputs()
    tree = NodeBintree(None)
    for command in inputs:
        execute_command(tree, command)
    exit(0)


if __name__ == "__main__":
    main()

