import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
INF = 10 ** 18
MOD = 10 ** 9 + 7

debug = True
debug = False

def dprint(*objects):
    if debug == True:
        print(*objects)


def solve():
    nodedict = {}

    preorder_list = []

    class Node:
        def __init__(self, id):
            self.id = id
            self.childlist = []
            self.p = 0
            self.walked = False

        def __repr__(self):
            return str(self.__dict__)

        def preorder(self, p):
            if self.walked:
                return 0

            self.p = self.p + p

            self.walked = True
            preorder_list.append(self.id)

            for child in self.childlist:
                child.preorder(self.p)

            return 0


    N, Q = LI()

    for i in range(1, N+1):
        nodedict[i] = Node(i)

    for i in range(N-1):
        a, b = LI()
        nodedict[a].childlist.append(nodedict[b])

    for i in range(Q):
        p, x = LI()
        nodedict[p].p += x

    # preorder
    nodedict[1].preorder(0)

    dprint(preorder_list)
    print(' '.join([str(nodedict[i].p) for i in range(1, N+1)]))

solve()