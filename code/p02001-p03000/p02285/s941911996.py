#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_8_A
#???????????? 15??? 8A????????????

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
        insert_node["parent"] = parent
    else:
        parent["right"] = insert_node
        insert_node["parent"] = parent

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

def delete_tree(root, target):
    
    delete_node = find_tree(root, target)
    parent = delete_node["parent"]
    if parent["left"] == delete_node:
        parent_direction = "left"
    else:
        parent_direction = "right"
    
    while True:
        if delete_node["left"] == None and delete_node["right"] == None:
            parent[parent_direction] = None
            break
        elif delete_node["left"] and delete_node["right"]:
            p = get_inorder(root)
            next_num = int(p[p.index(str(delete_node["data"])) + 1])
            tmp_delete_node = find_tree(root, next_num)
            delete_node["data"] = next_num
            delete_node = tmp_delete_node
            parent = delete_node["parent"]
            if parent == None:
                parent_direction = None
            elif parent["left"] == delete_node:
                parent_direction = "left"
            else:
                parent_direction = "right"
        else:
            if delete_node["left"]:
                parent[parent_direction] = delete_node["left"]
                delete_node["left"]["parent"] = parent
            else:
                parent[parent_direction] = delete_node["right"]
                delete_node["right"]["parent"] = parent
            break

    
def find_tree(root, target):
    focus_node = root

    while not focus_node == None:
        if focus_node["data"] == target:
            return focus_node
        elif focus_node["data"] < target:
            focus_node = focus_node["right"]
        else:
            focus_node = focus_node["left"]
    
    return None
    
def print_tree(root):
    print(" " + " ".join(get_inorder(root)))
    print(" " + " ".join(get_preorder(root)))
    
def main():
    
    n_line = int(input())
    input_list = [input() for i in range(n_line)]
    root = {"left":None, "right": None, "data":int(input_list[0].split()[1]), "parent": None}

    for line in input_list[1:]:
        if line == "print":
            print_tree(root)
        else:
            split_line = line.split()
            target = int(split_line[1])
            if split_line[0] == "insert":
                node = {"left":None, "right": None, "data":int(split_line[1]), "parent":None}
                insert(root, node)
            elif split_line[0] == "find":
                if find_tree(root, target):
                    print("yes")
                else:
                    print("no")
            elif split_line[0] == "delete":
                delete_tree(root, target)
        
        

if __name__ == "__main__":
    main()