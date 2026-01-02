import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

def main():
    S = _S()
    Q = I()
    Querys = [LS() for _ in range(Q)]
    rev_flg = -1
    dq = collections.deque(S)
    for q in Querys:
        if q[0]=='1':
            rev_flg *= -1
        else:
            ti,fi,ci = q
            if int(fi)*rev_flg in (1,-2):
                dq.append(ci)
            else:
                dq.appendleft(ci)

    print("".join(dq)[::-1] if rev_flg==1 else "".join(dq))

main()

