import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
sys.setrecursionlimit(10**7)

def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())


def isBingoYoko(ans):
    for bool_i_list in ans:
        for bj in bool_i_list:
            if bj==False:
                break
            else:
                pass
        else:
            print("Yes")
            exit(0)

def isBingoNaname(ans):
    if (ans[0][0] and ans[1][1] and ans[2][2]) or ((ans[0][2] and ans[1][1] and ans[2][0])):
        print("Yes")
        exit(0)
    else:
        pass

def main():
    A = [LI() for _ in range(3)]
    N = I()
    B = [I() for _ in range(N)]
    ans = [[False for _ in range(3)] for _ in range(3)]
    for b in B:
        for i in range(len(A)):
            if b in A[i]:
                j = A[i].index(b)
                ans[i][j] = True

    isBingoYoko(ans)
    isBingoYoko(list(numpy.array(ans).T))
    isBingoNaname(ans)
    print("No")

main()

