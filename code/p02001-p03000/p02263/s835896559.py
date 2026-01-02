import sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**10
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    S = LSS()
    stk = []
    for i in S:
        if i in ['+', '-', '*']:
            a = stk.pop()
            b = stk.pop()
            if i=='+':
                stk.append(b+a)
            elif i=='-':
                stk.append(b-a)
            elif i=='*':
                stk.append(b*a)
        else:
            stk.append(int(i))

    print(stk[0])

if __name__ == '__main__':
    resolve()
