from collections import defaultdict
import sys
import time

sys.setrecursionlimit(2000)
N, M, K = [int(i) for i in input().split(" ")]

t = time.time()
class UnionNode():
    def __init__(self, number):
        self.number = number
        self.volume = 1
        self.master = None

    @property
    def root(self):
        if self.master:
            self.master = self.master.root
            return self.master
        else:
            return self

    def unite(self, target):
        seroot = self.root
        taroot = target.root
        if seroot.number == taroot.number:
            pass
        else:
            #print(f"unite {target.rootnum}({target.root.volume}), {self.rootnum}({self.root.volume})")
            if seroot.volume > taroot.volume:
                seroot.volume += taroot.volume
                taroot.master = seroot
            else:
                taroot.volume += seroot.volume
                seroot.master = taroot

nodes = [UnionNode(i) for i in range(N)]

outlist = defaultdict(lambda :[])

for i in range(M):
    s = input()
    a, b = s.split(" ")
    a = int(a) - 1
    b = int(b) - 1
    nodes[a].unite(nodes[b])
    outlist[a].append(b)
    outlist[b].append(a)

for i in range(K):
    s = input()
    a, b = s.split(" ")
    a = int(a) - 1
    b = int(b) - 1
    outlist[a].append(b)
    outlist[b].append(a)

result = []
for i in range(N):
    rootnode = nodes[i].root
    ret = rootnode.volume - 1
    for out in outlist[i]:
        if nodes[out].root.number == rootnode.number:
            ret -=1
    result.append(ret)

#for i in range(100):
#    print(result[i])

print(" ".join([str(i) for i in result]))

#print(time.time() - t)