import sys,collections;sys.setrecursionlimit(10**7)
def Is(): return [int(x) for x in sys.stdin.readline().split()]
def Ss(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

mat = []
for i in range(3):
    mat.append(Is())
if mat[0][0] - mat[0][1] == mat[1][0] - mat[1][1] == mat[2][0] - mat[2][1]:
    if mat[0][1] - mat[0][2] == mat[1][1] - mat[1][2] == mat[2][1] - mat[2][2]:
        if mat[0][0] - mat[1][0] == mat[0][1] - mat[1][1] == mat[0][2] - mat[1][2]:
            if mat[1][0] - mat[2][0] == mat[1][1] - mat[2][1] == mat[1][2] - mat[2][2]:
                print("Yes")
                exit()
print("No")