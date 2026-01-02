import sys,collections,math,random;sys.setrecursionlimit(10**7)
def Is(): return [int(x) for x in sys.stdin.readline().split()]
def Ss(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

H,W = Is()
mat = [[0]*W for i in range(H)]
inp = []
for i in range(H):
    inp.append(list(S()))
for i in range(H):
    t = 0
    for j in range(W):
        if inp[i][j] == ".":
            t += 1
            if j == W-1:
                for k in range(j+1-t,j+1):
                    mat[i][k] += t
        elif inp[i][j] == "#":
            for k in range(j-t,j):
                mat[i][k] += t
            t = 0
#print(*mat)
for j in range(W):
    t = 0
    for i in range(H):
        if inp[i][j] == ".":
            t += 1
            if i == H-1:
                for k in range(i+1-t,i+1):
                    mat[k][j] += t
        elif inp[i][j] == "#":
            for k in range(i-t,i):
                mat[k][j] += t
            t = 0    
#print(*mat)
ans = 0
for e in mat:
    ans = max(ans,max(e))
print(max(0,ans-1))