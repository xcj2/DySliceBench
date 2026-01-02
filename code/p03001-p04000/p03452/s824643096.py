from collections import defaultdict

class XUnionFind(object):

    def __init__(self):
        self.table = defaultdict(lambda:-1)
        self.dtable = defaultdict(lambda:0)

    def find(self, x):
        parent = self.table[x] 
        if parent < 0:
            return x, 0
        else:
            root, distance = self.find(parent)
            new_distance = distance + self.dtable[x]
            self.table[x] = root
            self.dtable[x] = new_distance
            return root, new_distance

    def union(self, x1, x2, d = 0):
        root1, distance1 = self.find(x1)
        root2, distance2 = self.find(x2)
        if root1 == root2:
            if distance2 - distance1 != d:
                return False
            return True
        if root1 < root2:
            self.table[root1] += self.table[root2]
            self.table[root2] = root1
            self.dtable[root2] = distance1 + d - distance2
        else:
            self.table[root2] += self.table[root1]
            self.table[root1] = root2
            self.dtable[root1] = distance2 - d - distance1
        return True

def solve(N, M, lrd):
    uf = XUnionFind()
    for l, r, d in lrd:
        rc = uf.union(l, r, d)
        if rc == False:
            return False
    return True
        

if __name__ == "__main__":
    N, M = [int(x) for x in input().split()]
    lrd = []
    for i in range(M):
        lrd.append([int(x) for x in input().split()])
    if solve(N, M, lrd):
        print("Yes")
    else:
        print("No")
