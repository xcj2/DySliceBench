class Node:
    def __init__(self):
        """
        parent: Parent of the node
        left: Child of the node. THe most left
        right: Sibling of the note. The node next to the node (right side)
        """
        self.parent = None
        self.left = None
        self.right = None
        self.id = None
        self.depth = None
        self.type = None
    def __str__(self):
        if self.type == 'root':
            return 'parent = ' + str(-1) + ', depth = ' + str(self.depth) + ', ' + self.type
        else:
            return 'parent = ' + str(self.parent.id) + ', depth = ' + str(self.depth) + ', ' + self.type

def getDepth(node):
    """
    :param node: node
    :return: depth of the node (int)
    """
    depth = 0
    while node.parent is not None:
        node = node.parent
        depth += 1
    return depth

def getType(node):
    """
    :param node: node
    :return: node type (string)
    """
    if node.parent is None:
        return 'root'
    elif node.left is None:
        return 'leaf'
    else:
        return 'internal node'

def getChildren(node):
    """
    :param node: node
    :return: childrent of the node (list)
    """
    children = []
    result = [] # list of ids of children
    child = node.left
    while child is not None:
        children.append(child)
        child = child.right
    if not children:
        return '[]'
    for i in children:
        result.append(i.id)
    return result

n = int(input())
nodesDic = {}

for i in range(n):
    id, k, *c = map(int, input().split())
    # id がすでにあれば既存 node, なければ新規 node 作成
    if id not in nodesDic.keys():
        node = Node()
        nodesDic[id] = node
        node.id = id
    else:
        node = nodesDic[id]

    # c が empty (children なし) のとき
    if not c:
        pass
    else:
        # c の id の node が存在しなければ作成, right, parent を設定
        for j in range(len(c)-1, -1, -1): # c を末尾から読む (right の設定がこの for loop 内で可能(
            if c[j] not in nodesDic.keys():
                childNode = Node()
                nodesDic[c[j]] = childNode
                childNode.id = c[j]

            nodesDic[c[j]].parent = node
            if len(c) == 1 or j == len(c)-1: # c が要素 1 つのみのとき or 最も右側の node のとき
                pass
            else:
                nodesDic[c[j]].right = nodesDic[c[j+1]]
        node.left = nodesDic[c[0]]

for i in range(n):
    node = nodesDic[i]
    node.depth = getDepth(node)
    node.type = getType(node)
    children = getChildren(node)
    print('node', str(i) + ':', end=' ')
    print(node, end=', ')
    print(children)
