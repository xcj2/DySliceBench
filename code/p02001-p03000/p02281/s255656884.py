def print_preorder(node: int) -> None:
    global trees
    print(f" {node}", end="")
    left_child = trees[node]['left-child']
    right_child = trees[node]['right-child']
    if -1 != left_child:
        print_preorder(left_child)
    if -1 != right_child:
        print_preorder(right_child)


def print_inorder(node: int) -> None:
    global trees
    left_child = trees[node]['left-child']
    right_child = trees[node]['right-child']
    if -1 != left_child:
        print_inorder(left_child)
    print(f" {node}", end="")
    if -1 != right_child:
        print_inorder(right_child)


def print_postorder(node: int) -> None:
    global trees
    left_child = trees[node]['left-child']
    right_child = trees[node]['right-child']
    if -1 != left_child:
        print_postorder(left_child)
    if -1 != right_child:
        print_postorder(right_child)
    print(f" {node}", end="")


if __name__ == "__main__":
    node_num = int(input())
    trees = {idx:
             {"parent": -1, "left-child": -1, "right-child": -1}
             for idx in range(node_num)}

    for _ in range(0, node_num):
        node, left_child, right_child = map(lambda x: int(x), input().split())
        if -1 != left_child:
            trees[node]["left-child"] = left_child
            trees[left_child]["parent"] = node
        if -1 != right_child:
            trees[node]["right-child"] = right_child
            trees[right_child]["parent"] = node

    root_node = [k for k, v in trees.items() if v["parent"] == -1][0]

    print("Preorder")
    print_preorder(root_node)
    print("")
    print("Inorder")
    print_inorder(root_node)
    print("")
    print("Postorder")
    print_postorder(root_node)
    print("")

