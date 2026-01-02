from collections import Counter
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
    n=II()
    s=SI()
    cc=Counter(s)
    if len(cc)<3:
        print(0)
        exit()
    tot=1
    for c in cc.values():tot*=c
    for i,c in enumerate(s):
        for j in range(1,min(i,n-1-i)+1):
            if s[i-j]!=c and c!=s[i+j] and s[i-j]!=s[i+j]:
                tot-=1
    print(tot)

main()