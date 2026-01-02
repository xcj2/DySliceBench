import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, A, B, C, D = mapint()
S = list(input())

def exp(idx, goal):
    while 1:
        if idx==goal:
            return True
        if idx+1<N and S[idx+1]==".":
            idx += 1
        elif idx+2<N and S[idx+2]=='.':
            idx += 2
        else:
            return False

if C<D:
    if exp(A-1, C-1) and exp(B-1, D-1):
        print('Yes')
    else:
        print('No')
else:
    for i in range(B-2, min(N-2, D-1)):
        if S[i]=="." and S[i+1]=="." and S[i+2]==".":
            if exp(A-1, C-1) and exp(B-1, D-1):
                print('Yes')
            else:
                print('No')
            break
    else:
        print('No')