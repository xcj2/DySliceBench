n = int(input())
T = [list(map(int,input().split())) for i in range(n)]

T.sort(key = lambda x: x[0])

def calc_parent(T,data):
    for i in range(n):
        if T[i][1] == data or T[i][2] == data:
            return T[i][0]
    return -1

def calc_sibling(T,data):
    if T[calc_parent(T,data)][1] == data:
        return T[calc_parent(T,data)][2]
    elif T[calc_parent(T,data)][2] == data:
        return T[calc_parent(T,data)][1]
    else:
        return -1

def calc_degree(T,data):
    count = 0
    if T[data][1] != -1:
        count += 1
    if T[data][2] != -1:
        count += 1
    return count

def calc_depth(T,data):
    depth = 0
    while calc_parent(T,data) != -1:
        data = calc_parent(T,data)
        depth += 1
    return depth

def calc_height(T,data):
    if data == -1:
        return -1
    else:
        return max(1+calc_height(T,T[data][1]),
                    1+calc_height(T,T[data][2]))

def calc_type(T,data):
    if calc_parent(T,data) == -1:
        return "root"
    elif calc_degree(T,data) == 0:
        return "leaf"
    else:
        return "internal node"

for i in range(n):
    print("node "+str(i), end="")
    print(": parent = "+str(calc_parent(T,i)),end="")
    print(", sibling = "+str(calc_sibling(T,i)), end="")
    print(", degree = "+str(calc_degree(T,i)), end="")
    print(", depth = "+str(calc_depth(T,i)), end="")
    print(", height = "+str(calc_height(T,i)), end="")
    print(", "+str(calc_type(T,i)))

