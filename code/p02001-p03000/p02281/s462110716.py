if __name__ == "__main__":
    parent, children = {}, {}
    preorder, inorder, postorder = [], [], []
    n = int(input())
    for _ in range(n):
        i, left, right = input().split()
        children[i] = dict(right=right, left=left)
        for child in children[i].values():
            if child != "-1":
                parent[child] = i
    
    root = (set(children) - set(parent)).pop()
    parent[root] = "-1"
    
    def set_preorder(i):
        if i == "-1":
            return
        preorder.append(i)
        set_preorder(children[i]["left"])
        set_preorder(children[i]["right"])
    
    def set_inorder(i):
        if i == "-1":
            return
        set_inorder(children[i]["left"])
        inorder.append(i)
        set_inorder(children[i]["right"])

    def set_postorder(i):
        if i == "-1":
            return
        set_postorder(children[i]["left"])
        set_postorder(children[i]["right"])
        postorder.append(i)
                
    set_preorder(root)
    set_inorder(root)
    set_postorder(root)

    print("Preorder")
    print(" " + " ".join(preorder))
    print("Inorder")
    print(" " + " ".join(inorder))
    print("Postorder")
    print(" " + " ".join(postorder))
