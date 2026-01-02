import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def main():
    N, Q = map(int, input().split())
    E = [[] for i in range(N+1)]
    counter = [0] * (N+1)

    for i in range(N-1):
        a, b = map(int, input().split())
        E[a].append(b)
        E[b].append(a)

    for i in range(Q):
        # 頂点p を根とする部分木に含まれるカウンターにxを足す
        p, x = map(int, input().split())
        counter[p] += x

    queue = []

    parent = [1]
    def mktree(v, parent, E):
        children = E[v]
        children.remove(parent)
        for child in children:
            mktree(child, v, E)

    while parent:
        p = parent.pop()
        for child in E[p]:
            E[child].remove(p)
            parent.append(child)

    def get(v, children, counter):
        c = counter[v]
        for child in children[v]:
            counter[child] += c
            get(child, children, counter)
    """
    parent = [1]
    while parent:
        p = parent.pop()
        c = counter[p]
        for child in E[p]:
            counter[child] += c
            parent.append(child)
    """
    get(1, E, counter)
    print(" ".join(str(x) for x in counter[1:]))

main()




