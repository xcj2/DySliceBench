class Node(object):
    root = None

    """ ????????¨????????? """
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.height = None

    @classmethod
    def insert(cls, z):
        y = None
        x = cls.root
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == None:
            cls.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        return z

    @classmethod
    def walk_preorder(cls, node):
        """ ??????????????? """
        # results = []
        # results.append(node.key)
        print(' {0}'.format(node.key), end='')
        if node.left != None:
            # results.append(cls.walk_preorder(node.left))
            cls.walk_preorder(node.left)
        if node.right != None:
            # results.append(cls.walk_preorder(node.right))
            cls.walk_preorder(node.right)
        #return results

    @classmethod
    def walk_inorder(cls, node):
        """ ??????????????? """
        # results = []
        if node.left != None:
            # results.append(cls.walk_inorder(node.left))
            cls.walk_inorder(node.left)
        # results.append(node.key)
        print(' {0}'.format(node.key), end='')
        if node.right != None:
            # results.append(cls.walk_inorder(node.right))
            cls.walk_inorder(node.right)
        # return results

    def get_type(self):
        if self.parent:
            return 'root'
        elif self.left == None and self.right == None:
            return 'leaf'
        else:
            return 'internal node'

    def get_depth(self):
        if self.parent == None:
            return 0
        else:
            depth = 1
            t = self.parent
            while t.parent != None:
                t = t.parent
                depth += 1
            return depth

    def get_height(self):
        if self.height:
            return self.height
        h_left = 0
        h_right = 0
        if self.left != None:
            h_left = self.left.get_height() + 1
        if self.right != None:
            h_right = self.right.get_height() + 1
        self.height = max(h_left, h_right)
        return self.height

    def get_degree(self):
        degree = 0
        if self.left != None:
            degree += 1
        if self.right != None:
            degree += 1
        return degree

    def get_sibling(self):
        if self.parent == None:
            return -1
        p = self.parent
        if p.left != self and p.left != None:
            return p.left
        if p.right != self and p.right != None:
            return p.right


def process_node_data(node_data):
    last = None
    for inst in node_data:
        if inst[0] == 'print':
            result = Node.walk_inorder(last.root)
            print('')
            # print(' {0}'.format(' '.join(map(str, flatten(result)))))
            result = Node.walk_preorder(last.root)
            # print(' {0}'.format(' '.join(map(str, flatten(result)))))
            print('')
        else:
            node_key = int(inst[1])
            new_node = Node(node_key)
            last = Node.insert(new_node)


def flatten(l):
    """ http://stackoverflow.com/questions/2158395/flatten-an-irregular-list-of-lists-in-python """
    import collections
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el


if __name__ == '__main__':
    # ??????????????\???
    num_of_nodes = int(input())
    node_data = [input().split(' ') for _ in range(num_of_nodes)]
    # node_data = []
    # with open('ALDS1_8_A-in4.txt') as f:
    #     for line in f:
    #        if ' ' not in line:
    #           num_of_nodes = (int(line))
    #       else:
    #           node_data.append(line.split(' '))


    # ???????????????
    # ??¨???????????????
    process_node_data(node_data)

    # ???????????????