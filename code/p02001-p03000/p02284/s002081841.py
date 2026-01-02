#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_8_A
#????????????

def insert(root, insert_node):
    focus_node = root
    parent = None
    while not focus_node == None:
        parent = focus_node
        if focus_node["data"]  > insert_node["data"]:
            focus_node = focus_node["left"]
        else:
            focus_node = focus_node["right"]

    if parent["data"] > insert_node["data"]:
        parent["left"] = insert_node
    else:
        parent["right"] = insert_node

def get_preorder(node):
    if node == None:
        return []
    r = []
    r.append(str(node["data"]))
    r.extend(get_preorder(node["left"]))
    r.extend(get_preorder(node["right"]))

    return r
    
def get_inorder(node):
    if node == None:
        return []
    r = []
    r.extend(get_inorder(node["left"]))
    r.append(str(node["data"]))
    r.extend(get_inorder(node["right"]))

    return r

def find_tree(root, target):
    focus_node = root

    while not focus_node == None:
        if focus_node["data"] == target:
            print("yes")
            return
        elif focus_node["data"] < target:
            focus_node = focus_node["right"]
        else:
            focus_node = focus_node["left"]
    
    print("no")
    
def print_tree(root):
    print(" " + " ".join(get_inorder(root)))
    print(" " + " ".join(get_preorder(root)))
    
def main():
    
    n_line = int(input())
    input_list = [input() for i in range(n_line)]
    root = {"left":None, "right": None, "data":int(input_list[0].split()[1])}

    for line in input_list[1:]:
        if line == "print":
            print_tree(root)
        else:
            split_line = line.split()
            if split_line[0] == "insert":
                node = {"left":None, "right": None, "data":int(split_line[1])}
                insert(root, node)
            elif split_line[0] == "find":
                find_tree(root, int(split_line[1]))
        
        

if __name__ == "__main__":
    main()