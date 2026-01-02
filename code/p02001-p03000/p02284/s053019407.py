import sys
sys.setrecursionlimit(2**20)  


class Node:
    def __init__(self, parent=None, left=None, right=None):
        self.parent = parent
        self.left = left  
        self.right = right


def pre_parse(T, u, pre_ls):
    if u == None:
        return
    pre_ls.append(u)
    pre_parse(T, T[u].left, pre_ls) 
    pre_parse(T, T[u].right, pre_ls)


def in_parse(T, u, in_ls):
    if u == None:
        return
    in_parse(T, T[u].left, in_ls)
    in_ls.append(u)
    in_parse(T, T[u].right, in_ls)


def insert(T, ROOT, z):
    if ROOT == z:
        T[z] = Node()
    else:
        T[z] = Node()  
        x = ROOT
        while x is not None:  
            next_parent = x  
            if z < x:  
                x = T[x].left
            else:
                x = T[x].right
        T[z].parent = next_parent
        if z < next_parent:
            T[next_parent].left = z
        else:
            T[next_parent].right = z


def find(T, ROOT, k):
    x = ROOT
    while x and k != x:
        if k < x:
            x = T[x].left
        else:
            x = T[x].right
    return x

def print_result(T):
    pre_ls, in_ls = [], []
    in_parse(T, ROOT, in_ls)
    pre_parse(T, ROOT, pre_ls)
    print('', *in_ls)
    print('', *pre_ls)


n = int(input())
T = {}
for i in range(n):
    tmp = input()
    if i == 0:
        ROOT = int(tmp[7:])
    if tmp[0] == "p":
        print_result(T)
    elif tmp[0] == "f":
        if find(T, ROOT, int(tmp[5:])):
            print("yes")
        else:
            print("no")
    else:
        insert(T, ROOT, int(tmp[7:]))
