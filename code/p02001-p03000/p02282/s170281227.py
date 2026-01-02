class Node():
    def __init__(self):
        self.parent = -1
        self.left = -1
        self.right = -1


def reconstruction(preo, ino):
    root = preo[0]

    ileft = ino[0:ino.index(root)]
    iright = ino[ino.index(root)+1:]

    pleft = preo[1:]
    pright = preo[1:]

    for item in iright:
        pleft.remove(item)

    for item in ileft:
        pright.remove(item)

    if len(pleft) == 0:
        pass
    elif len(pleft) == 1:
        Nodes[root-1].left = pleft[0]
    else:
        Nodes[root-1].left = reconstruction(pleft, ileft)

    if len(pright) == 0:
        pass
    elif len(pright) == 1:
        Nodes[root-1].right = pright[0]
    else:
        Nodes[root-1].right = reconstruction(pright, iright)

    return root


def postorder(id):
    if Nodes[id-1].left != -1:
        postorder(Nodes[id-1].left)

    if Nodes[id-1].right != -1:
        postorder(Nodes[id-1].right)

    ans.append(id)


def main():
    n = int(input())
    global Nodes
    Nodes = [Node() for i in range(n)]

    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))

    rootid = reconstruction(preorder, inorder)

    global ans
    ans = []
    postorder(rootid)
    print(*ans)


if __name__ == '__main__':
    main()
