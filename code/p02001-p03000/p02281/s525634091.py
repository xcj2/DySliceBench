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

    print("Preorder")
    showPreorder(root_cand_list[0])
    print()
    print("Inorder")
    showInorder(root_cand_list[0])
    print()
    print("Postorder")
    showPostorder(root_cand_list[0])
    print()


def showPreorder(num):
    print(" ", end="")
    print(num, end="")
    if btree[num].left != -1:
        showPreorder(btree[num].left)
    if btree[num].right != -1:
        showPreorder(btree[num].right)


def showInorder(num):
    if btree[num].left != -1:
        showInorder(btree[num].left)
    print(" ", end="")
    print(num, end="")
    if btree[num].right != -1:
        showInorder(btree[num].right)


def showPostorder(num):
    if btree[num].left != -1:
        showPostorder(btree[num].left)
    if btree[num].right != -1:
        showPostorder(btree[num].right)
    print(" ", end="")
    print(num, end="")



if __name__ == '__main__':
    main()

