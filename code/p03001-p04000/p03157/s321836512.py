import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]
dij=[(1,0),(0,1),(-1,0),(0,-1)]

def main():
    h,w=MI()
    ss=[SI() for _ in range(h)]

    def dfs(i,j):
        stack=[(i,j)]
        bc,wc=0,0
        while stack:
            i,j=stack.pop()
            if ss[i][j]=="#":bc+=1
            else:wc+=1
            for di,dj in dij:
                ni,nj=i+di,j+dj
                if ni<0 or nj<0 or ni>=h or nj>=w:continue
                if fin[ni][nj] or ss[i][j]==ss[ni][nj]:continue
                fin[ni][nj]=True
                stack.append((ni,nj))
        return bc,wc

    ans=0
    fin=[[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if fin[i][j]:continue
            fin[i][j]=True
            bc,wc=dfs(i,j)
            ans+=bc*wc
    print(ans)

main()