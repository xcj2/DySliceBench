class Node_information():
    def __init__(self):
        self.id = -1
        self.parent = -1
        self.degree = 0
        self.depth = 0
        self.height = 0
        self.type = ""
        self.left = -1
        self.right = -1
        self.sibling = -1

def get_tree_id_type(left, right):
    if left == -1 and right == -1:
        return "leaf"
    else:
        return "internal node"

def get_tree_id_degree(left, right):
    if left == -1 and right == -1:
        return 0
    elif left != -1 and right != -1:
        return 2
    else:
        return 1

def get_depth(tree_information, now_id, now_depth):
    tree_information[now_id].depth = now_depth
    if tree_information[now_id].left != -1:
        get_depth(tree_information, tree_information[now_id].left, now_depth + 1)
    if tree_information[now_id].right != -1:
        get_depth(tree_information, tree_information[now_id].right, now_depth + 1)

def get_height(tree_information, now_id):
    h1 = 0
    h2 = 0
    if tree_information[now_id].left != -1:
        h1 = get_height(tree_information, tree_information[now_id].left)
    if tree_information[now_id].right != -1:
        h2 = get_height(tree_information, tree_information[now_id].right)
    tree_information[now_id].height = max(h1,h2)
    return tree_information[now_id].height + 1

def print_tree_information(tree_information, N):
    for i in range(N):
        print("node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}"
        .format(tree_information[i].id,tree_information[i].parent,tree_information[i].sibling,tree_information[i].degree,
        tree_information[i].depth,tree_information[i].height,tree_information[i].type))

def main():
    N = int(input())
    tree_information = list()
    for i in range(N):
        tree_information.append(Node_information())
    for i in range(N):
        information = [int(i) for i in input().split()]
        tree_information[information[0]].id = information[0]
        tree_information[information[0]].left = information[1]
        tree_information[information[0]].right = information[2]
        if information[1] != -1:
            tree_information[information[1]].parent = information[0]
        if information[2] != -1:
            tree_information[information[2]].parent = information[0]
        if information[1] != -1 and information[2] != -1:
            tree_information[information[1]].sibling = information[2]
            tree_information[information[2]].sibling = information[1]
        tree_information[information[0]].type = get_tree_id_type(tree_information[information[0]].left,tree_information[information[0]].right)
        tree_information[information[0]].degree = get_tree_id_degree(tree_information[information[0]].left,tree_information[information[0]].right)
    for i in range(N):
        if tree_information[i].parent == -1:
            tree_information[i].type = "root"
            get_depth(tree_information,i,0)
            break
    for i in range(N):
        if tree_information[i].type == "root":
            get_height(tree_information,i)
            break
    print_tree_information(tree_information,N)

if __name__ == "__main__":
    main()
