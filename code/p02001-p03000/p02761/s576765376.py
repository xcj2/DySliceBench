import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
sys.setrecursionlimit(10**7)

def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

def main():
    N,M = LI()
    SC = [LI() for _ in range(M)]
    a = [0 for _ in range(N)]
    pre = [None for _ in range(N)]
    # for s,c in SC:
    #     s = s-1
    #     if (a[s]==c) or (pre[s] is None):
    #         pre[s] = a[s]
    #         a[s] = c
    #     else:
    #         print(-1)
    #         exit(0)
    # ans = int("".join(map(str,a)))
    # if len(str(ans))==N:
    #     print("{}".format(int(ans)))
    # else:
    #     print(-1)

    for i in range(1000):
        i = str(i)
        if len(i)==N:
            for s,c in SC:
                if i[s-1] == str(c):
                    # print(i[s-1], c)
                    continue
                else:
                    break
            else:
                print(i)
                exit(0)
        else:
            continue
    else:
        print(-1)

main()

