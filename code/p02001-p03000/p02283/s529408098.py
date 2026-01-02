#! /usr/bin/env python


class NodeBintree:

    def __init__(self, key, parent=None):
        self.key = key
        # self.parent = parent
        self.left = None
        self.right = None

    def insert_node (self, n):
        if (self.key is None) or (self.key > n.key):
            if self.left is None:
                self.left = n
                # n.parent = self
            else:
                self.left.insert_node(n)
        else:
            if self.right is None:
                self.right = n
                # n.parent = self
            else:
                self.right.insert_node(n)

    def traverse_inorder (self):
        ret = ""

        if self.left is not None:
            ret += self.left.traverse_inorder()
            # for less in self.left.traverse_inorder():
            #     yield less

        if self.key is not None:
            ret += " {0}".format(self.key)
            # print(" {0}".format(self.key), end="")
            # yield
            # yield self.key
            # yield " {0}".format(self.key)

        if self.right is not None:
            ret += self.right.traverse_inorder()
            # for more in self.right.traverse_inorder():
            #     yield more
        return ret

    def traverse_preorder (self):
        ret = ""

        if self.key is not None:
            ret += " {0}".format(self.key)
            # print(" {0}".format(self.key), end="")
            # yield
            # yield self.key
            # yield " {0}".format(self.key)

        if self.left is not None:
            ret += self.left.traverse_preorder()
            # for less in self.left.traverse_preorder():
            #     yield less

        if self.right is not None:
            ret += self.right.traverse_preorder()
            # for more in self.right.traverse_preorder():
            #     yield more
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
        # return tree

    elif command["command"] == "print":
        print(tree.traverse_inorder() )
        # print()
        print(tree.traverse_preorder() )
        # print()
        #     pass
        # print("")
        # for n in tree.traverse_preorder():
        #     pass
        # print("")
        # print("".join([" {0}".format(n) for n in tree.traverse_inorder()]))
        # print("".join([" {0}".format(n) for n in tree.traverse_preorder()]))

    return


def main ():
    inputs = proc_inputs()
    # print(inputs)
    tree = NodeBintree(None)
    # map(execute_command, tree, inputs)
    for command in inputs:
        execute_command(tree, command)
    exit(0)


if __name__ == "__main__":
    main()



