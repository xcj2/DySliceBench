import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def factor(n):
    res=[]
    for d in range(1,n+1):
        if d*d>n:break
        if n%d==0:
            res.append(d)
            res.append(n//d)
        if res[-1]==res[-2]:res.pop()
    return res[1:]

def main():
    n=II()
    ff=factor(n)
    ans=len(factor(n-1))
    for k in ff:
        for b in range(1,40):
            pw=pow(k,b)
            if n%pw==0 and (n//pw-1)%k==0:
                ans+=1
                #print(k,(n//pw-1)%k,b)
    print(ans)

main()