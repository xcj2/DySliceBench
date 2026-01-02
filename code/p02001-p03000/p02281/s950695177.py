#1_7_C
N = int(input())

preorder_list = []
inorder_list = []
postorder_list = []

rooted_tree = [{} for i in range(N)]
for _ in range(N):
    row = input()
    id, left, right = list(map(int, row.split()))
    rooted_tree[id]["id"] = id
    rooted_tree[id]["right"] = right
    rooted_tree[id]["left"] = left
    #子供のparentを左右で設定する。
    if left > -1:
        left_child_id = left
        rooted_tree[left_child_id]["parent"] = id
    if right > -1:
        right_child_id = right
        rooted_tree[right_child_id]["parent"] = id
        
def preParse(node):
    preorder_list.append(node["id"])
    if node["left"] != -1:
        preParse(rooted_tree[node["left"]])
    if node["right"] != -1:
        preParse(rooted_tree[node["right"]])
    
def inParse(node):
    if node["left"] != -1:
        inParse(rooted_tree[node["left"]])
    inorder_list.append(node["id"])
    if node["right"] != -1:
        inParse(rooted_tree[node["right"]])
    
def postParse(node):
    if node["left"] != -1:
        postParse(rooted_tree[node["left"]])
    if node["right"] != -1:
        postParse(rooted_tree[node["right"]])
    postorder_list.append(node["id"])
    
def get_parent(node):
    parent = -1
    if "parent" in node:
        return node["parent"]
    return parent

for node in rooted_tree:
    if get_parent(node) == -1:
        root_id = node["id"]
        break

print("Preorder")
preParse(rooted_tree[root_id])
print(" "+" ".join(map(str, preorder_list)))
# print(*preorder_list)
print("Inorder")
inParse(rooted_tree[root_id])
# print(*inorder_list)
print(" "+" ".join(map(str, inorder_list)))
print("Postorder")
postParse(rooted_tree[root_id])
# print(*postorder_list)
print(" "+" ".join(map(str, postorder_list)))
