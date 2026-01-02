from bisect import bisect_left as bl
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
    bb = LI()
    cc = LI()
    aa.sort()
    bb.sort()
    #print(aa)
    #print(bb)
    ans=0
    bi_to_a_cnt=[0]
    for b in bb:
        bi_to_a_cnt.append(bl(aa,b)+bi_to_a_cnt[-1])
    for c in cc:
        bi=bl(bb,c)
        ans+=bi_to_a_cnt[bi]
    print(ans)

main()