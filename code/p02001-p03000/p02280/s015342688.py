import sys
input = sys.stdin.readline


class Node():
    def __init__(self, parent, left, right):
        self.parent = parent
        self.left = left
        self.right = right


N = int(input())
btree = [Node(-1, -1, -1) for i in range(N)]
root_cand_list = [i for i in range(N)]
depth = [-1 for i in range(N)]
height = [-1 for i in range(N)]
degree = [0 for i in range(N)]
sibling = [-1 for i in range(N)]


def main():

    for i in range(N):
        num, left, right = map(int, input().split())

        if left != -1:
            btree[num].left = left
            btree[left].parent = num
            root_cand_list.remove(left)
        if right != -1:
            btree[num].right = right
            btree[right].parent = num
            root_cand_list.remove(right)

    setDepth(root_cand_list[0], 0)
    setHeight(root_cand_list[0])
    showBTree()


def setDepth(num, d):
    depth[num] = d
    node = btree[num]
    dgr = 0
    if node.left != -1:
        setDepth(node.left, d + 1)
        dgr += 1
    if node.right != -1:
        setDepth(node.right, d + 1)
        dgr += 1

    if node.parent != -1:
        parent = btree[node.parent]
        if parent.left != -1 and parent.left != num:
            sibling[num] = parent.left
        elif parent.right != -1 and parent.right != num:
            sibling[num] = parent.right

    degree[num] = dgr


def setHeight(num):
    lh = 0
    rh = 0
    if btree[num].left != -1:
        lh = setHeight(btree[num].left)
    if btree[num].right != -1:
        rh = setHeight(btree[num].right)

    if btree[num].left == -1 and btree[num].right == -1:
        # 葉についた時
        height[num] = 0
        h = 1
    else:
        height[num] = max(lh, rh)
        h = max(lh, rh) + 1
    return h


def showBTree():
    for i in range(N):
        if depth[i] == 0:
            TYPE = "root"
        elif height[i] == 0:
            TYPE = "leaf"
        else:
            TYPE = "internal node"

        print("node {0}: parent = {1}, sibling = {2}, degree = {3}, depth = {4}, height = {5}, {6}".format(i, btree[i].parent, sibling[i], degree[i], depth[i], height[i], TYPE))


if __name__ == '__main__':
    main()

