def Parent(node_id):
    return int(node_id/2.0)

def LeftChild(node_id):
    return 2 * node_id

def RightChild(node_id):
    return 2 * node_id + 1

def Main():
    n = int(input())
    H = [None]*(n + 1)
    keys = [int(a) for a in input().split()]

    for i in range(1, n + 1):
        H[i] = keys[i - 1]

    for i in range(1, n + 1):
        information = "node {0}: key = {1}, ".format(i, H[i])
        
        if 1 <= Parent(i) <= n:
            information +=  "parent key = {0}, ".format(H[Parent(i)])

        if 1 <=  LeftChild(i) <= n:
            information += "left key = {0}, ".format(H[LeftChild(i)])

        if 1 <= RightChild(i) <= n:
            information += "right key = {0}, ".format(H[RightChild(i)])

        print(information)

Main()
