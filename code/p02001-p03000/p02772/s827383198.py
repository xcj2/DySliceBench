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
    def ok():
        for a in aa:
            if a%2==0:
                if a%3 and a%5:return False
        return True

    n=II()
    aa=LI()
    if ok():print("APPROVED")
    else:print("DENIED")

main()