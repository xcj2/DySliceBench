import sys
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()

def main():
    N, A, B, C, D = LI_()
    S = SI()
    ans = True
    # AC
    for i in range(A, C):
        if S[i: i + 2] == '##':
            ans = False
            break
    # BD
    if ans:
        for i in range(B, D):
            if S[i: i + 2] == '##':
                ans = False
                break
    # if A BD C
    if ans and D < C:
        tmp = False
        for i in range(B - 1, D):
            if S[i: i + 3] == '...':
                tmp = True
                break
        ans = ans and tmp

    ans = 'Yes' if ans else 'No'
    return ans

print(main())