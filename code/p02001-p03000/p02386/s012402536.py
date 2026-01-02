class Checker:
    d = {
        1: { 2: (3,4,5,6), 3: (5,2,4,6), 4: (2,5,3,6), 5: (4,3,2,6) },
        2: { 1: (4,3,6,5), 3: (1,6,4,5), 4: (6,1,3,5), 6: (3,4,1,5) },
        3: { 1: (2,5,6,4), 2: (6,1,5,4), 5: (1,6,2,4), 6: (5,2,1,4) },
        4: { 1: (5,2,6,3), 2: (1,6,5,3), 5: (6,1,2,3), 6: (2,5,1,3) },
        5: { 1: (3,4,6,2), 3: (6,1,4,2), 4: (1,6,3,2), 6: (4,3,1,2) },
        6: { 2: (4,3,5,1), 3: (2,5,4,1), 4: (5,2,3,1), 5: (3,4,2,1) }
        }

    def __init__(self, s):
        l = s.split()
        self.tbl = {}
        for c,i in zip(l, range(1,7)):
            if c in self.tbl:
                self.tbl[c].append(i)
            else:
                self.tbl[c] = [i]
        self.pip = dict(zip(range(1,7), l))

    def __call__(self, s):
        l = s.split()

        if not (l[0] in self.tbl):
            return False
        if not (l[1] in self.tbl):
            return False

        for i0 in self.tbl[l[0]]:
            for i1 in self.tbl[l[1]]:
                if i1 in self.d[i0]:
                    for i,j in zip(self.d[i0][i1], range(2,6)):
                        if self.pip[i] != l[j]:
                            break
                    else:
                        return True
        return False

def g():
    n = int(input()) - 1
    c = Checker(input())
    for _ in range(n):
        yield c(input())

if any(g()):
    print("No")
else:
    print("Yes")