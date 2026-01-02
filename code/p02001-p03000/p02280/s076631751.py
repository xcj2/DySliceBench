if __name__ == "__main__":
    parent, children, depths, sibling, heights = {}, {}, {}, {}, {}
    n = int(input())
    for _ in range(n):
        i, left, right = input().split()
        if left == "-1" and right == "-1":
            children[i] = None
            continue
        if left == "-1" or right == "-1":
            child = left if right == "-1" else right
            children[i] = [child]
        else:
            children[i] = [left, right]
        for child in children[i]:
            parent[child] = i
    
    root = (set(children) - set(parent)).pop()
    parent[root] = "-1"
    sibling[root] = "-1"
    
    def get_degree(i):
        if children[i] is None:
            return 0
        return len(children[i])

    def get_type(i):
        if parent[i] == "-1":
            return "root"
        if children[i] is None:
            return "leaf"
        return "internal node"
    
    def set_depth(i, depth):
        depths[i] = depth
        if children[i] is not None:
            for child in children[i]:
                set_depth(child, depth+1)

    def set_sibling(i, s):
        sibling[i] = s
        childs = children[i]
        if childs is not None:
            if len(childs) == 1:
                set_sibling(childs[0], "-1")
            else:
                set_sibling(childs[0], childs[1])
                set_sibling(childs[1], childs[0])
    
    def set_height(i):
        if children[i] is None:
            heights[i] = 0
            return 0
        childs = children[i]
        if len(childs) == 1:
            heights[i] = set_height(childs[0])+1
            return heights[i]
        heights[i] = max(set_height(childs[0]), set_height(childs[1]))+1
        return heights[i]

    set_depth(root, 0)
    set_sibling(root, "-1")
    set_height(root)
    for i in map(str, range(n)):
        print("node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}".format(i, parent[i], sibling[i], get_degree(i), depths[i], heights[i], get_type(i)))
