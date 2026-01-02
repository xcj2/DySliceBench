#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_7_A&lang=jp
"""
class RootedTree:
    def __init__(self):
        self.id = None
        self.child = []
        self.parent = -1
        self.node_type = "root"
        self.depth = 0

    def show(self):
        print("node {}: parent = {}, depth = {}, {}, {}".format(self.id, self.parent, self.depth, self.node_type, self.child))

def cal_depth(tree, node, cur_depth):
    node.depth += cur_depth
    #node.show()
    for index in node.child:
        cal_depth(tree, tree[index], cur_depth + 1)
        
def make_tree(tree_data):#?????????,?¨???????n^2
    tree = [RootedTree() for i in range(len(tree_data))]
    
    for data in tree_data:
        focus = tree[data[0]]
        focus.id = data[0]
        
        if data[2:]:
            focus.child = data[2:]
            
            for child_index in data[2:]:
                tree[child_index].parent = data[0]
                
                if tree_data[[a[0] for a in tree_data].index(child_index)][2:]:
                    tree[child_index].node_type = "internal node"
                else:
                    tree[child_index].node_type = "leaf"
            
    root_index = [n.node_type for n in tree].index("root")
    cal_depth(tree, tree[root_index], 0)
    return tree
"""
def set_tree_data(tree, target, parent, depth):
    tree[target]["depth"] += depth
    tree[target]["parent"] = parent

    for c in tree[target]["child"]:
        set_tree_data(tree, c, target, depth + 1)

def make_tree_revision(tree_data, n_tree):#??????????¨???????n + n?
    tree = [{"parent": None, "depth":0, "child" : None} for i in range(n_tree)]
    root = sum(range(n_tree))
    
    for node_data in tree_data:
        tree[node_data[0]]["child"] = node_data[2:]
        root -= sum(node_data[2:])

    set_tree_data(tree, root, -1, 0)
    return tree

def main():
    n_tree = int(input())
    tree_data = [[int(a) for a in input().split()] for i in range(n_tree)]
    
    for i, node in enumerate(make_tree_revision(tree_data, n_tree)):
        category = "root"
        if (not node["parent"] == -1) and node["child"]:
            category = "internal node"
        elif not node["parent"] == -1:
            category = "leaf"

        print("node {}: parent = {}, depth = {}, {}, {}".format(i, node["parent"], node["depth"], category, node["child"]))
if __name__ == "__main__":
    main()