# 何でこのプログラムで通らないか分からん
import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    a, b, c, d, e, f = MI()
    max_sw = a*100
    max_s = 0
    for an in range(f // (100 * a) + 1):
        for bn in range((f - 100 * a * an) // (100 * b) + 1):
            w = a * an + b * bn
            if w == 0: continue
            if 100 * w > f: break
            for cn in range(f):
                dn = (min(w * e, f - 100 * w) - c * cn) // d
                if dn < 0: break
                # print(an,bn,cn,dn)
                s = c * cn + d * dn
                if s * max_sw > max_s * (s + w * 100):
                    max_sw = s + 100 * w
                    max_s = s
    print(max_sw, max_s)

main()
