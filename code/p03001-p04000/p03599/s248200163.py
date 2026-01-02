import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

a, b, c, d, e, f = MI()

def main():
    ans_sw=100*a
    ans_s=0
    for an in range(f+1):
        if a*an*100>f:break
        for bn in range(f+1):
            w=an*a+bn*b
            if w*100>f:break
            lim=min(w*e,f-w*100)
            for cn in range(f+1):
                dn=(lim-c*cn)//d
                if dn<0:break
                s=c*cn+d*dn
                if s*ans_sw>ans_s*(s+100*w):
                    ans_sw=s+100*w
                    ans_s=s
    print(ans_sw,ans_s)

main()
