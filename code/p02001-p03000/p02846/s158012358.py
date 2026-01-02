import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    t1,t2=MI()
    a1,a2=MI()
    b1,b2=MI()
    if a1<b1:a1,a2,b1,b2=b1,b2,a1,a2
    if a1*t1+a2*t2==b1*t1+b2*t2:
        print("infinity")
        exit()
    if a1*t1+a2*t2>b1*t1+b2*t2:
        print(0)
        exit()
    x=a1*t1-b1*t1
    y=b1*t1+b2*t2-(a1*t1+a2*t2)
    ans=(x//y)*2
    if x%y:
        ans+=1
    print(ans)


main()