import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    while 1:
        n=int(input())
        if n==0:break
        ans=[]
        for _ in range(n):
            l,*num=input().split()
            p,a,b,c,d,e,f,s,m=map(int,num)
            ans.append([(f*s*m-p)/(a+b+c+(d+e)*m),l])
        ans.sort(key=lambda x:(-x[0],x[1]))
        for _,l in ans:
            print(l)
        print("#")

main()

