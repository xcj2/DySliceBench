import sys,collections,math;sys.setrecursionlimit(10**7)
def Is(): return [int(x) for x in sys.stdin.readline().split()]
def Ss(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

H,W = Is()
mat = ["."*(W+2)]
for i in range(H):
    mat.append("." + S() + ".")
mat.append("."*(W+2))
for h in range(1,H+1):
    for w in range(1,W+1):
        t = mat[h][w]
        if t == "#" and  (mat[h-1][w]+mat[h+1][w]+mat[h][w-1]+mat[h][w+1]).count("#") == 0 :
            print("No")
            exit()
print("Yes")