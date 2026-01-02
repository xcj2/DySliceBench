import random


class Cube:
    def __init__(self, u, s, e, w, n, d):
        self.u = u
        self.s = s
        self.e = e
        self.w = w
        self.n = n
        self.d = d

    def rotate(self, dic):
        if dic == "N":
            tmp = self.u
            self.u = self.s
            self.s = self.d
            self.d = self.n
            self.n = tmp
        elif dic == "E":
            tmp = self.u
            self.u = self.w
            self.w = self.d
            self.d = self.e
            self.e = tmp
        elif dic == "W":
            tmp = self.u
            self.u = self.e
            self.e = self.d
            self.d = self.w
            self.w = tmp
        else:
            tmp = self.u
            self.u = self.n
            self.n = self.d
            self.d = self.s
            self.s = tmp


def main():
    u1, s1, e1, w1, n1, d1 = map(int, input().split())
    u2, s2, e2, w2, n2, d2 = map(int, input().split())
    cube1 = Cube(u1, s1, e1, w1, n1, d1)
    cube2 = Cube(u2, s2, e2, w2, n2, d2)

    ret = "No"
    for i in range(10000):
        cube2.rotate(random.choice("NWES"))
        if cube1.u == cube2.u and cube1.n == cube2.n and cube1.w == cube2.w and cube1.e == cube2.e and cube1.s == cube2.s and cube1.d == cube2.d:
            ret = "Yes"
            break
    print(ret)


if __name__ == '__main__':
    main()

