from collections import defaultdict
def inpl(): return list(map(int,input().split()))

class increment:
    def __init__(self, start=0):
        self.index = start-1

    def __call__(self):
        self.index += 1
        return self.index

ui = defaultdict(increment())
plist = []
clists = []
Np = 0

N, M = inpl()
P = [0]*M
Y = [0]*M
for i in range(M):
    P[i], Y[i] = inpl()
    p = ui[P[i]]
    if p >= Np:
        plist.append(P[i])
        clists.append([[i,Y[i]]])
        Np += 1
    else:
        clists[p].append([i,Y[i]])

ids = ['']*M
for p in range(Np):
    clists[p].sort(key=lambda x: x[1])
    for c in range(len(clists[p])):
        cid = "{0:06d}".format(plist[p]) + "{0:06d}".format(c+1)
        ids[clists[p][c][0]] = cid

for i in range(M):
    print(ids[i])