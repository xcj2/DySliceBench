
class Node_information():
    def __init__(self):
        self.id = -1
        self.parent = -1
        self.depth = 0
        self.type = ""
        self.child = list()

def get_tree_id_child_and_parent(tree_id, tree_k, tree_information, node_information):
    for j in range(tree_k):
        tree_information[tree_id].child.append(node_information[j+2])
        tree_information[node_information[j+2]].parent = tree_id

def get_tree_id_type(number_of_child):
    if number_of_child == 0:
        return "leaf"
    else:
        return "internal node"

def depth_search(tree_information, now_depth, now_id):
    tree_information[now_id].depth = now_depth
    for i in range(len(tree_information[now_id].child)):
        depth_search(tree_information, now_depth+1,tree_information[now_id].child[i])
    
def print_tree_information(tree_information, N):
    for i in range(N):
        print("node {}: parent = {}, depth = {}, {}, [".format(tree_information[i].id,tree_information[i].parent,tree_information[i].depth,tree_information[i].type),end="")
        for j in range(len(tree_information[i].child)):
            if j != len(tree_information[i].child) - 1:
                print("{},".format(tree_information[i].child[j]),end=" ")
            else: 
                print("{}".format(tree_information[i].child[j]),end="")
        print("]")


def main():
    N = int(input())
    tree_information = list()
    for i in range(N):
        tree_information.append(Node_information())
    for i in range(N):
        node_information = [int(i) for i in input().split()]
        tree_id = node_information[0]
        tree_k = node_information[1]
        tree_information[tree_id].id = node_information[0]
        get_tree_id_child_and_parent(tree_id, tree_k, tree_information, node_information)
        tree_information[tree_id].type = get_tree_id_type(len(tree_information[tree_id].child))
    for i in range(N):
        if tree_information[i].parent == -1:
            tree_information[i].type = "root"
            depth_search(tree_information,0,i)
    print_tree_information(tree_information, N)

if __name__ == "__main__":
    main()
