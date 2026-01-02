import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    def dfs(mx=0,s=[0]):
        if len(s)==n:
            ans.append(s)
            return
        for i in range(mx+2):
            dfs(max(mx,i),s+[i])

    n=II()
    ans=[]
    dfs()
    for ak in ans:
        print("".join(chr(a+97) for a in ak))

main()