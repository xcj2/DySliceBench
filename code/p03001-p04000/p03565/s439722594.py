import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    def check(i):
        for j in range(tn):
            if s[i + j] != "?" and s[i + j] != t[j]:
                return False
        return True

    s = list(input())
    t = list(input())
    sn = len(s)
    tn = len(t)
    for i in range(sn - tn, -1, -1):
        if check(i):
            s = s[:i] + t + s[i + tn:]
            break
    else:
        print("UNRESTORABLE")
        exit()
    for i in range(sn):
        if s[i] == "?": s[i] = "a"
    print(*s, sep="")

main()
