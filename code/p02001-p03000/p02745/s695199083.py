from itertools import permutations
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
    def same(x,y):
        xn,yn=len(x),len(y)
        # x,yの一致する位置を調べる
        res = [True] * 4005
        for i in range(xn):
            for c0, c1 in zip(x[i:], y):
                if c0 != q and c1 != q and c0 != c1:
                    res[i] = False
                    break
        return res

    q=ord("?")
    ss=[[ord(c) for c in SI()] for _ in range(3)]
    # 一致を調べる
    eq=[[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if i==j:continue
            eq[i][j]=same(ss[i],ss[j])
    # 位置を全探索
    ans=sum(len(ss[i]) for i in range(3))
    for si,sj,sk in permutations(range(3)):
        for i in range(len(ss[si])+1):
            for j in range(max(len(ss[sj]),len(ss[si])-i)+1):
                if eq[si][sj][i] and eq[sj][sk][j] and eq[si][sk][i+j]:
                    cur=max(len(ss[si]),len(ss[sj])+i,len(ss[sk])+i+j)
                    ans=min(ans,cur)
    print(ans)

main()
