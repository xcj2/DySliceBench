#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_7_B&lang=jp
def cal_depth(binary_tree, target_index, depth, parent, sibling):
    if target_index == -1:
        return 0
    binary_tree[target_index]["depth"] = depth
    binary_tree[target_index]["parent"] = parent
    binary_tree[target_index]["sibling"] = sibling
    height_left = cal_depth(binary_tree, binary_tree[target_index]["left"], depth + 1, target_index, binary_tree[target_index]["right"])
    height_right = cal_depth(binary_tree, binary_tree[target_index]["right"], depth + 1, target_index, binary_tree[target_index]["left"])
    height = max(height_left, height_right)
    binary_tree[target_index]["height"] = height
    return height + 1

def solve(node_data, node_num):
    binary_tree = [{"left":-1, "right":-1, "depth":0, "parent":-1, "sibling":-1, "height":0, "degree":0} for a in range(node_num)]
    root_index = sum([i for i in range(node_num)])
    for node in node_data:
        binary_tree[node[0]]["left"] =  node[1]
        binary_tree[node[0]]["right"] =  node[2]

        if not node[1] == -1:
            root_index -= node[1]
            binary_tree[node[0]]["degree"] += 1
        if not node[2] == -1:
            root_index -= node[2]
            binary_tree[node[0]]["degree"] += 1
            
    cal_depth(binary_tree, root_index, 0, -1,-1)
    return binary_tree

def main():
    node_num = int(input())
    node_data = [[int(a) for a in input().split()] for i in range(node_num)]
    binary_tree = solve(node_data, node_num)

    for i, node in enumerate(binary_tree):
        node_type = "root"
        if node["left"] == -1 and node["right"] == -1 and not node["parent"] == -1:
            node_type = "leaf"
        elif not node["parent"] == -1:
            node_type = "internal node"
        print("node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}".format(i, node["parent"], node["sibling"], node["degree"], node["depth"], node["height"], node_type))
if __name__ == "__main__":
    main()
    