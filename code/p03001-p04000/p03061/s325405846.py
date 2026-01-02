import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def gcd(a,b):
    while b>0:a,b=b,a%b
    return a

def main():
    n=int(input())
    aa=LI()
    gl=[0]*n
    gr=[0]*n
    g=aa[0]
    for i,a in enumerate(aa):
        g=gcd(g,a)
        gl[i]=g
    g=aa[-1]
    for i,a in enumerate(aa[::-1]):
        g=gcd(g,a)
        gr[n-1-i]=g
    ans=max(gl[n-2],gr[1])
    for i in range(1,n-1):
        g=gcd(gl[i-1],gr[i+1])
        if g>ans:ans=g
    print(ans)

main()