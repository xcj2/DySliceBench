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
    n,k,c=MI()
    s=SI()
    ll=[0]*n
    rr=[0]*n
    for i,m in enumerate(s):
        if m == "o":
            if i-c-1>=0:ll[i] = ll[i - c - 1] + 1
            else:ll[i]=1
        else:ll[i]=ll[i-1]
    #print(ll)
    for i in range(n-1,-1,-1):
        m=s[i]
        if m == "o":
            if i + c + 1 < n:rr[i]=rr[i+c+1]+1
            else:rr[i]=1
        else:rr[i]=rr[(i+1)%n]
    #print(rr)
    ans=[]
    if n==1:ans.append(1)
    if n>1 and rr[1]<k:ans.append(1)
    for i in range(1,n-1):
        if ll[i-1]+rr[i+1]<k:ans.append(i+1)
    if n>1 and ll[n-2]<k:ans.append(n)
    print(*ans,sep="\n")

main()