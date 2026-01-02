import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    n=int(input())
    aa=LI()
    pp=[]
    mm=[]
    for a in aa:
        if a<0:mm.append(a)
        else:pp.append(a)
    if not mm:
        print(sum(pp))
        exit()
    if not pp:
        if len(mm)%2:
            print(-sum(mm)+max(mm)*2)
        else:
            print(-sum(mm))
        exit()
    if len(mm)%2:
        m=max(mm)
        p=min(pp)
        if p+m>=0:print(sum(pp)-sum(mm)+2*m)
        else:print(sum(pp)-2*p-sum(mm))
    else:
        print(sum(pp)-sum(mm))

main()
