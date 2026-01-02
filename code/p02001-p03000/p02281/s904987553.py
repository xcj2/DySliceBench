class Node:
    def __init__(self, parent=-1, left=-1, right=-1):
        self.parent = parent
        self.left = left
        self.right = right


n = int(input())
binary_tree = [Node() for i in range(n)]
pre_lst, in_lst, post_lst = [], [], []


def pre_order(u):
    if u == -1:
        return

    pre_lst.append(u)
    pre_order(binary_tree[u].left)
    pre_order(binary_tree[u].right)


def in_order(u):
    if u == -1:
        return

    in_order(binary_tree[u].left)
    in_lst.append(u)
    in_order(binary_tree[u].right)


def post_order(u):
    if u == -1:
        return

    post_order(binary_tree[u].left)
    post_order(binary_tree[u].right)
    post_lst.append(u)


def main():
    for i in range(n):
        idx, left, right = map(int, input().split())
        binary_tree[idx].left = left
        binary_tree[idx].right = right
        if left != -1:
            binary_tree[left].parent = idx
        if right != -1:
            binary_tree[right].parent = idx

    root_idx = 0
    for i in range(n):
        if binary_tree[i].parent == -1:
            root_idx = i
            break

    pre_order(root_idx)
    in_order(root_idx)
    post_order(root_idx)

    print("Preorder")
    print("", " ".join([str(i) for i in pre_lst]))
    print("Inorder")
    print("", " ".join([str(i) for i in in_lst]))
    print("Postorder")
    print("", " ".join([str(i) for i in post_lst]))


if __name__ == '__main__':
    main()

