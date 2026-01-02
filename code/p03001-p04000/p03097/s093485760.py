import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]
def bit(xx):return [format(x,"b") for x in xx]
popcnt=lambda x:bin(x).count("1")

def solve(xx,a,b):
    if len(xx)==2:return [a,b]
    k=(a^b).bit_length()-1
    aa=[]
    bb=[]
    for x in xx:
        if (x>>k&1)==(a>>k&1):aa.append(x)
        else:bb.append(x)
    i=0
    mid=aa[i]
    while mid==a or (mid^1<<k)==b or popcnt(a)&1==popcnt(mid)&1:
        i+=1
        mid=aa[i]
    #print(bit(xx),a,b,k,bit(aa),bit(bb),format(mid,"b"))
    return solve(aa,a,mid)+solve(bb,mid^1<<k,b)

def main():
    n,a,b=MI()
    if (popcnt(a)&1)^(popcnt(b)&1)==0:
        print("NO")
        exit()

    print("YES")
    print(*solve(list(range(1<<n)),a,b))

main()
