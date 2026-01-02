
nil = -1

class Node:
    def __init__(self):
        self.parent = nil
        self.left = nil
        self.right = nil

def post_tw(node, ans):
    if tree[node].left != nil:
        post_tw(tree[node].left, ans)

    if tree[node].right != nil:
        post_tw(tree[node].right, ans)

    ans.append(node + 1)

def reconst_tree(node, pretw_itr, subt):
    n_i = subt.index(node)

    left_subt = subt[:n_i]
    right_subt = subt[n_i + 1:]

    if left_subt:
        left = next(pretw_itr)
        tree[node].left = left
        reconst_tree(left, pretw_itr, left_subt)

    if right_subt:
        right = next(pretw_itr)
        tree[node].right = right
        reconst_tree(right, pretw_itr, right_subt)


n = int(input())
tree = [Node() for i in range(n)]

pretw = [int(i) - 1 for i in input().split()]
intw = [int(i) - 1 for i in input().split()]

pretw_itr = iter(pretw)

root = next(pretw_itr)

reconst_tree(root, pretw_itr, intw)

ans = []

post_tw(root, ans)

print(*ans)