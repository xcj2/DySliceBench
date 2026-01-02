import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    s=SI()
    q=II()
    aa=deque(ord(c) for c in s)
    rev=0
    for _ in range(q):
        t=SI().split()
        if t[0]=="1":rev=1-rev
        else:
            f=int(t[1])-1
            if f^rev:aa.append(ord(t[2]))
            else:aa.appendleft(ord(t[2]))
    if rev:aa.reverse()
    print("".join(chr(a) for a in aa))

main()