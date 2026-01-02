from sys import stdin

class Node:
    def __init__(self):
        self.children = [-1, -1]

###

def initNode(t_pre, t_in):
    global nodes
    if len(t_in) == 1:
        nodes[t_in[0]].children = [-1, -1]
        return t_in[0]
    else:
        r = t_in.index(t_pre[0])
        if r == 0: # 左部分木はなし
            rr = initNode(t_pre[1:], t_in[1:])
            nodes[t_in[r]].children = [-1, rr]
        elif r == len(t_in)-1: # 右部分木はなし
            lr = initNode(t_pre[1:r+1], t_in[:r])
            nodes[t_in[r]].children = [lr, -1]
        else:
            lr = initNode(t_pre[1:r+1], t_in[:r])
            rr = initNode(t_pre[r+1:], t_in[r+1:])
            nodes[t_in[r]].children = [lr, rr]

        return t_in[r]

def postorder(i):
    global nodes, res
    if i != -1:
        c = nodes[i].children
        postorder(c[0])
        postorder(c[1])
        res.append(i)

n = int(stdin.readline().rstrip())
t_pre = [int(x) for x in stdin.readline().rstrip().split()]
t_in = [int(x) for x in stdin.readline().rstrip().split()]

nodes = [Node() for _ in range(n+1)]
initNode(t_pre, t_in)

res = []
postorder(t_pre[0])
print(*res)
