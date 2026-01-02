# Nodeクラス


class Node:
    def __init__(self, k):
        self.k = k
        self.p = None
        self.l = None
        self.r = None

# BinarySearchクラス


class BinarySearch:
    root = None

    def insert(self, k):
        y = None
        x = self.root
        z = Node(k)
        while x:
            y = x
            if z.k < x.k:
                x = x.l
            else:
                x = x.r
        z.p = y

        if y == None:
            self.root = z
        else:
            if z.k < y.k:
                y.l = z
            else:
                y.r = z

    def preParse(self, u):
        if u == None:
            return
        print("", str(u.k), end="")
        self.preParse(u.l)
        self.preParse(u.r)

    def inParse(self, u):
        if u == None:
            return
        self.inParse(u.l)
        print("", str(u.k), end="")
        self.inParse(u.r)


if __name__ == '__main__':

    n = int(input().rstrip())
    x = BinarySearch()

    for i in range(n):
        com = input().rstrip()
        if com.startswith("insert"):
            k = int(com.split(" ")[1])
            x.insert(k)
        else:
            x.inParse(x.root)
            print()
            x.preParse(x.root)
            print()

