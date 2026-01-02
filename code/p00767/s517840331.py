from sys import exit, stderr, stdin
input = stdin.readline
# setrecursionlimit(10**7)

def debug(var, name="hoge"):
    print(str(type(var)) + name +":" + " = " + repr(var), file=stderr)
    return

class Tri:

    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.diag = h**2 + w**2

    def __lt__(t1, t2):
        if t1.diag < t2.diag:
            return True
        elif t1.diag > t2.diag:
            return False
        else:
            return t1.h < t2.h

    def __repr__(self):
        return str(self.h) +" " + str(self.w)

    def __str__(self):
        return 0

def main():
    while(1):
        H, W = list(map(int, input().split()))
        if (H + W == 0):
            break
        diag = H**2 + W**2
        tris = []
        for h in range(1, 150):
            for w in range(h+1, 150):
                tris.append((Tri(h,w), h==H and w==W))
        # print(Tri(5, 6) < Tri(1, 8) < Tri(4, 7))
        # print(Tri(5, 6).diag,Tri(1, 8).diag, Tri(4, 7).diag)
        tris = sorted(tris, key=lambda x:x[0])
        # print(tris[:5])
        # for t in tris[:6]:
        #     print(t[0].h, t[0].w, t[0].diag)
        for i in range(len(tris)):
            if tris[i][1] == True:
                print(tris[i+1][0].h, tris[i+1][0].w)


if __name__ == "__main__":
    main()

