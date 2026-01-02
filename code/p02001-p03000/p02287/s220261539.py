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
    H = I()
    A = [0]
    tmp = LI()
    for i in tmp:
        A.append(i)

    for i in range(1, H+1):
        ans = ''
        ans += 'node ' + str(i) + ': '
        ans += 'key = ' + str(A[i]) + ', '
        if 1 <= i//2 < H+1:
            ans += 'parent key = ' + str(A[i//2]) + ', '
        if 1 <= 2*i < H+1:
            ans += 'left key = ' + str(A[2*i]) + ', '
        if 1 <= 2*i+1 < H+1:
            ans += 'right key = ' + str(A[2*i+1]) + ', '
        print(ans)

if __name__ == '__main__':
    resolve()

