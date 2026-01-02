def parent_id(id, H):
    if 1 <= id // 2 and id // 2 <= H:
        return id// 2
    return None

def left_id(id, H):
    if 1 <= id  *2 and id * 2 <= H:
        return id* 2
    return None

def right_id(id, H):
    if 1 <= (id * 2) + 1 and (id * 2) + 1 <= H:
        return (id * 2) + 1
    return None

H = int(input())
A = list(map(int, input().split()))

T = [{} for _ in range(H)]

for i in range(H):
    T[i]["id"] = i + 1
    T[i]["key"] = A[i]
    T[i]["parent_id"] = parent_id(T[i]["id"], H)
    T[i]["left_id"] = left_id(T[i]["id"], H)
    T[i]["right_id"] = right_id(T[i]["id"], H)

for i in range(H):
    parent_str, left_str, right_str = "", "", ""
    node_str = "node {}: ".format(T[i]["id"])
    key_str = "key = {}, ".format(T[i]["key"])
    if T[i]["parent_id"] != None:
        parent_str = "parent key = {}, ".format(T[int(T[i]["parent_id"])-1]["key"])
    if T[i]["left_id"] != None:
        left_str = "left key = {}, ".format(T[int(T[i]["left_id"])-1]["key"])
    if T[i]["right_id"] != None:
        right_str = "right key = {}, ".format(T[int(T[i]["right_id"])-1]["key"])
    print(node_str + key_str + parent_str + left_str + right_str)
